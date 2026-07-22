import os
import glob
import email
from email import policy
import subprocess
import fitz  # PyMuPDF
from html import escape

# Constants
DIR_PATH = r"C:\QiLabs\40_QiVault\60_cases\HERTZ"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
FINAL_PDF = os.path.join(DIR_PATH, "HERTZ_Emails_Merged.pdf")
TEMP_DIR = os.path.join(DIR_PATH, "temp_pdf_gen")

def setup_temp_dir():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

def extract_email_content(eml_path):
    with open(eml_path, 'r', encoding='utf-8', errors='replace') as f:
        msg = email.message_from_file(f, policy=policy.default)
    
    subject = msg.get("Subject", "(No Subject)")
    from_ = msg.get("From", "(Unknown)")
    to_ = msg.get("To", "(Unknown)")
    date_ = msg.get("Date", "(Unknown)")
    
    body = ""
    # Try to find HTML part first
    html_part = msg.get_body(preferencelist=('html',))
    if html_part:
        body = html_part.get_content()
    else:
        # Fallback to plain text
        text_part = msg.get_body(preferencelist=('plain',))
        if text_part:
            body = f"<pre style='font-family: sans-serif; white-space: pre-wrap;'>{escape(text_part.get_content())}</pre>"
            
    # Wrap in a clean HTML structure with metadata header
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .email-header {{ 
                border-bottom: 2px solid #333; 
                margin-bottom: 20px; 
                padding-bottom: 10px;
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
            }}
            .email-header p {{ margin: 5px 0; }}
            .email-body {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="email-header">
            <p><strong>From:</strong> {escape(str(from_))}</p>
            <p><strong>To:</strong> {escape(str(to_))}</p>
            <p><strong>Date:</strong> {escape(str(date_))}</p>
            <p><strong>Subject:</strong> {escape(str(subject))}</p>
        </div>
        <div class="email-body">
            {body}
        </div>
    </body>
    </html>
    """
    return html_content

def convert_html_to_pdf(html_path, pdf_path):
    # Call Edge headless to print to PDF
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    setup_temp_dir()
    eml_files = sorted(glob.glob(os.path.join(DIR_PATH, "*.eml")))
    pdf_files = []
    
    print(f"Found {len(eml_files)} .eml files to process.")
    
    for i, eml in enumerate(eml_files):
        print(f"Processing ({i+1}/{len(eml_files)}): {os.path.basename(eml)}")
        
        # 1. Extract HTML
        html_content = extract_email_content(eml)
        base_name = os.path.splitext(os.path.basename(eml))[0]
        
        html_path = os.path.join(TEMP_DIR, f"{base_name}.html")
        pdf_path = os.path.join(TEMP_DIR, f"{base_name}.pdf")
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        # 2. Convert to PDF
        convert_html_to_pdf(html_path, pdf_path)
        
        if os.path.exists(pdf_path):
            pdf_files.append(pdf_path)
            
    print("All individual PDFs generated. Merging and compressing...")
    
    # 3. Merge and Compress
    master_doc = fitz.open()
    for pdf in pdf_files:
        try:
            doc = fitz.open(pdf)
            master_doc.insert_pdf(doc)
            doc.close()
        except Exception as e:
            print(f"Error merging {pdf}: {e}")
            
    # Save with compression and garbage collection
    master_doc.save(FINAL_PDF, deflate=True, garbage=4)
    master_doc.close()
    
    final_size = os.path.getsize(FINAL_PDF) / (1024 * 1024)
    print(f"Merged PDF created successfully at: {FINAL_PDF}")
    print(f"Final Size: {final_size:.2f} MB")

if __name__ == "__main__":
    main()
