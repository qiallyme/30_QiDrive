---
layout: page
title: "Video to Speech Pipeline"
slug: "video_to_speech_pipeline"
created_at: "2026-03-30 08:35:44"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-03-30
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69ca7bc9-2d90-8325-a749-897e38fb58bd"
canonical_ref: ""
---

# Video to Speech Pipeline

## Overview
- **Date**: 2026-03-30 08:35:44
- **Conversation ID**: `69ca7bc9-2d90-8325-a749-897e38fb58bd`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> I need a python script to recursively go through a path that it will ask me for and look for all video file, isolate the audio, try to clean it up to prepare it for speech to text or produce the speech to text it self, the language is english

### Assistant
> I’m going to give you a working local script, not hand-wavy pseudocode. I’m checking the current recommended tooling for audio extraction and English transcription so I don’t bake in stale package assumptions.

### Assistant
> I have the stack pinned now. Best practical route is **FFmpeg for extraction/cleanup** plus **faster-whisper** for local English transcription, because it’s current, fast, and doesn’t force the older Whisper install path.

### Assistant
> Use this version.
> 
> It does the full pipeline locally: prompts for a root folder, walks it recursively, finds common video formats, extracts a **16 kHz mono WAV**, applies a **speech-first cleanup chain**, and can also generate **English `.txt` and `.srt` transcripts** with `faster-whisper`. FFmpeg is built for media conversion and filtering, and its filters include things like highpass, lowpass, denoise, loudness normalization, and silence removal; `faster-whisper` currently supports Python 3.9+ and installs from PyPI. citeturn842696view2turn842696view3turn390603view0turn441921view3turn441921view0turn842696view0
> 
> ## Install
> 
> ```bash
> pip install faster-whisper
> ```
> 
> Make sure `ffmpeg` and `ffprobe` are installed and available on your PATH, because this script uses them directly for extraction and cleanup. citeturn842696view2
> 
> ## Script
> 
> ```python
> #!/usr/bin/env python3
> """
> Recursive video -> cleaned audio -> optional English STT pipeline.
> 
> What it does:
> 1. Prompts for a root folder (unless --path is passed)
> 2. Recursively finds video files
> 3. Extracts audio to 16 kHz mono WAV
> 4. Applies conservative speech-focused cleanup with FFmpeg
> 5. Optionally transcribes to English .txt and .srt using faster-whisper
> 
> Outputs go into:
> <root>/_stt_output/audio_clean/...
> <root>/_stt_output/transcripts/...
> <root>/_stt_output/manifest.json
> """
> 
> from __future__ import annotations
> 
> import argparse
> import json
> import shutil
> import subprocess
> import sys
> from dataclasses import asdict, dataclass
> from pathlib import Path
> from typing import Optional
> 
> VIDEO_EXTENSIONS = {
>     ".mp4", ".mov", ".mkv", ".avi", ".wmv", ".m4v", ".webm",
>     ".flv", ".mpeg", ".mpg", ".ts", ".mts", ".m2ts", ".3gp"
> }
> 
> # Conservative cleanup chain for speech prep:
> # - highpass: remove low rumble
> # - lowpass: remove useless very high frequencies for speech STT
> # - afftdn: light spectral denoise
> # - loudnorm: stabilize volume
> DEFAULT_FILTER_CHAIN = (
>     "highpass=f=80,"
>     "lowpass=f=7500,"
>     "afftdn=nr=12:nf=-30,"
>     "loudnorm=I=-16:LRA=11:TP=-1.5"
> )
> 
> 
> @dataclass
> class FileResult:
>     video: str
>     status: str
>     audio_path: Optional[str] = None
>     txt_path: Optional[str] = None
>     srt_path: Optional[str] = None
>     error: Optional[str] = None
> 
> 
> def run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
>     return subprocess.run(
>         cmd,
>         stdout=subprocess.PIPE,
>         stderr=subprocess.PIPE,
>         text=True,
>         check=False
>     )
> 
> 
> def require_binary(name: str) -> str:
>     path = shutil.which(name)
>     if not path:
>         print(f"ERROR: '{name}' was not found on PATH.")
>         sys.exit(1)
>     return path
> 
> 
> def prompt_path() -> Path:
>     while True:
>         raw = input("Enter the folder path to scan: ").strip().strip('"').strip("'")
>         path = Path(raw).expanduser()
>         if path.is_dir():
>             return path.resolve()
>         print("That path is not a valid folder. Try again.")
> 
> 
> def prompt_yes_no(question: str, default: bool = True) -> bool:
>     suffix = " [Y/n]: " if default else " [y/N]: "
>     raw = input(question + suffix).strip().lower()
>     if not raw:
>         return default
>     return raw in {"y", "yes"}
> 
> 
> def prompt_text(question: str, default: str) -> str:
>     raw = input(f"{question} [{default}]: ").strip()
>     return raw or default
> 
> 
> def discover_videos(root: Path) -> list[Path]:
>     return sorted(
>         p for p in root.rglob("*")
>         if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS
>     )
> 
> 
> def has_audio_stream(ffprobe_bin: str, video_path: Path) -> bool:
>     cmd = [
>         ffprobe_bin,
>         "-v", "error",
>         "-select_streams", "a:0",
>         "-show_entries", "stream=codec_type",
>         "-of", "default=nw=1:nk=1",
>         str(video_path),
>     ]
>     result = run_cmd(cmd)
>     return result.returncode == 0 and "audio" in result.stdout.lower()
> 
> 
> def ensure_parent(path: Path) -> None:
>     path.parent.mkdir(parents=True, exist_ok=True)
> 
> 
> def extract_and_clean_audio(
>     ffmpeg_bin: str,
>     video_path: Path,
>     output_wav: Path,
>     cleanup: bool,
>     filter_chain: str,
> ) -> None:
>     ensure_parent(output_wav)
> 
>     cmd = [
>         ffmpeg_bin,
>         "-y",
>         "-hide_banner",
>         "-loglevel", "error",
>         "-i", str(video_path),
>         "-vn",
>         "-map", "0:a:0",
>         "-ac", "1",
>         "-ar", "16000",
>         "-c:a", "pcm_s16le",
>     ]
> 
>     if cleanup:
>         cmd += ["-af", filter_chain]
> 
>     cmd.append(str(output_wav))
> 
>     result = run_cmd(cmd)
>     if result.returncode != 0:
>         raise RuntimeError(result.stderr.strip() or "ffmpeg failed")
> 
> 
> def format_srt_timestamp(seconds: float) -> str:
>     total_ms = int(round(seconds * 1000))
>     hours = total_ms // 3_600_000
>     total_ms %= 3_600_000
>     minutes = total_ms // 60_000
>     total_ms %= 60_000
>     secs = total_ms // 1000
>     millis = total_ms % 1000
>     return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
> 
> 
> def write_transcript_files(txt_path: Path, srt_path: Path, segments: list) -> None:
>     ensure_parent(txt_path)
>     ensure_parent(srt_path)
> 
>     text_lines = []
>     srt_blocks = []
> 
>     for idx, seg in enumerate(segments, start=1):
>         text = (seg.text or "").strip()
>         if not text:
>             continue
> 
>         text_lines.append(text)
> 
>         start_ts = format_srt_timestamp(seg.start)
>         end_ts = format_srt_timestamp(seg.end)
>         srt_blocks.append(f"{idx}\n{start_ts} --> {end_ts}\n{text}\n")
> 
>     txt_path.write_text("\n".join(text_lines).strip() + "\n", encoding="utf-8")
>     srt_path.write_text("\n".join(srt_blocks).strip() + "\n", encoding="utf-8")
> 
> 
> def transcribe_audio(
>     audio_path: Path,
>     txt_path: Path,
>     srt_path: Path,
>     model_size: str,
>     device: str,
> ) -> None:
>     try:
>         from faster_whisper import WhisperModel
>     except ImportError as exc:
>         raise RuntimeError(
>             "faster-whisper is not installed. Run: pip install faster-whisper"
>         ) from exc
> 
>     compute_type = "float16" if device == "cuda" else "int8"
> 
>     model = WhisperModel(
>         model_size,
>         device=device,
>         compute_type=compute_type,
>     )
> 
>     segments_iter, info = model.transcribe(
>         str(audio_path),
>         language="en",
>         beam_size=5,
>         vad_filter=True,
>         condition_on_previous_text=False,
>     )
> 
>     segments = list(segments_iter)
>     if not segments:
>         ensure_parent(txt_path)
>         txt_path.write_text("", encoding="utf-8")
>         ensure_parent(srt_path)
>         srt_path.write_text("", encoding="utf-8")
>         return
> 
>     write_transcript_files(txt_path, srt_path, segments)
> 
> 
> def choose_default_device() -> str:
>     return "cuda" if shutil.which("nvidia-smi") else "cpu"
> 
> 
> def build_output_paths(root: Path, video_path: Path, out_root: Path) -> tuple[Path, Path, Path]:
>     rel = video_path.relative_to(root)
>     base_rel = rel.with_suffix("")  # remove only final suffix
> 
>     audio_out = (out_root / "audio_clean" / base_rel).with_suffix(".clean.wav")
>     txt_out = (out_root / "transcripts" / base_rel).with_suffix(".txt")
>     srt_out = (out_root / "transcripts" / base_rel).with_suffix(".srt")
>     return audio_out, txt_out, srt_out
> 
> 
> def parse_args() -> argparse.Namespace:
>     parser = argparse.ArgumentParser(
>         description="Recursively extract/clean audio from video files and optionally transcribe to English."
>     )
>     parser.add_argument("--path", type=str, help="Root folder to scan")
>     parser.add_argument("--no-stt", action="store_true", help="Only extract/clean audio; do not transcribe")
>     parser.add_argument("--no-cleanup", action="store_true", help="Extract audio without cleanup filters")
>     parser.add_argument("--model", type=str, default=None, help="Whisper model size (tiny, base, small, medium, large-v3, etc.)")
>     parser.add_argument("--device", type=str, default=None, choices=["cpu", "cuda"], help="Transcription device")
>     parser.add_argument("--filter-chain", type=str, default=DEFAULT_FILTER_CHAIN, help="Custom FFmpeg audio filter chain")
>     return parser.parse_args()
> 
> 
> def main() -> None:
>     args = parse_args()
> 
>     ffmpeg_bin = require_binary("ffmpeg")
>     ffprobe_bin = require_binary("ffprobe")
> 
>     root = Path(args.path).expanduser().resolve() if args.path else prompt_path()
>     if not root.is_dir():
>         print("ERROR: Provided path is not a folder.")
>         sys.exit(1)
> 
>     do_stt = not args.no_stt
>     cleanup = not args.no_cleanup
> 
>     if args.path is None:
>         do_stt = prompt_yes_no("Produce speech-to-text too?", default=True)
>         cleanup = prompt_yes_no("Apply cleanup filters before STT?", default=True)
> 
>     model_size = args.model
>     if do_stt and not model_size:
>         model_size = prompt_text("Whisper model to use", "small")
> 
>     device = args.device or choose_default_device()
> 
>     video_files = discover_videos(root)
>     if not video_files:
>         print("No video files found.")
>         return
> 
>     out_root = root / "_stt_output"
>     out_root.mkdir(parents=True, exist_ok=True)
> 
>     print(f"\nRoot: {root}")
>     print(f"Found {len(video_files)} video file(s).")
>     print(f"Output: {out_root}")
>     print(f"Cleanup: {'ON' if cleanup else 'OFF'}")
>     print(f"STT: {'ON' if do_stt else 'OFF'}")
>     if do_stt:
>         print(f"Model: {model_size}")
>         print(f"Device: {device}")
>     print()
> 
>     results: list[FileResult] = []
> 
>     for index, video_path in enumerate(video_files, start=1):
>         print(f"[{index}/{len(video_files)}] {video_path}")
> 
>         audio_out, txt_out, srt_out = build_output_paths(root, video_path, out_root)
> 
>         try:
>             if not has_audio_stream(ffprobe_bin, video_path):
>                 msg = "Skipped: no audio stream found"
>                 print(f"  - {msg}")
>                 results.append(FileResult(
>                     video=str(video_path),
>                     status="skipped_no_audio",
>                     error=msg,
>                 ))
>                 continue
> 
>             extract_and_clean_audio(
>                 ffmpeg_bin=ffmpeg_bin,
>                 video_path=video_path,
>                 output_wav=audio_out,
>                 cleanup=cleanup,
>                 filter_chain=args.filter_chain,
>             )
>             print(f"  - Audio written: {audio_out}")
> 
>             txt_path_str = None
>             srt_path_str = None
> 
>             if do_stt:
>                 transcribe_audio(
>                     audio_path=audio_out,
>                     txt_path=txt_out,
>                     srt_path=srt_out,
>                     model_size=model_size,
>                     device=device,
>                 )
>                 txt_path_str = str(txt_out)
>                 srt_path_str = str(srt_out)
>                 print(f"  - Transcript written: {txt_out}")
>                 print(f"  - Subtitles written:  {srt_out}")
> 
>             results.append(FileResult(
>                 video=str(video_path),
>                 status="ok",
>                 audio_path=str(audio_out),
>                 txt_path=txt_path_str,
>                 srt_path=srt_path_str,
>             ))
> 
>         except Exception as exc:
>             print(f"  - ERROR: {exc}")
>             results.append(FileResult(
>                 video=str(video_path),
>                 status="error",
>                 error=str(exc),
>             ))
> 
>     manifest_path = out_root / "manifest.json"
>     manifest_path.write_text(
>         json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False),
>         encoding="utf-8",
>     )
> 
>     print("\nDone.")
>     print(f"Manifest: {manifest_path}")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ## Run it
> 
> Interactive:
> 
> ```bash
> python video_stt_pipeline.py
> ```
> 
> Or pass the folder directly:
> 
> ```bash
> python video_stt_pipeline.py --path "D:\Your\Folder\Here"
> ```
> 
> Extract/clean only, no transcription:
> 
> ```bash
> python video_stt_pipeline.py --path "D:\Your\Folder\Here" --no-stt
> ```
> 
> ## Straight truth
> 
> A few things matter here:
> 
> - **Cleanup helps, but too much cleanup can make STT worse.** That’s why I used a conservative chain instead of some aggressive “AI denoise everything” mess.
> - **`small` is a good default** if you want sane speed/accuracy locally.
> - If your videos are long and your CPU is weak, this will be slow. That’s normal.
> - If you have an NVIDIA GPU, the script will try to use `cuda` when `nvidia-smi` is present. Otherwise it falls back to CPU.
> 
> Best next upgrade would be turning this into a **Windows double-click launcher** with auto-venv setup so you don’t babysit it.

### User
> does this do anything to the source file or just read only?

### Assistant
> Read-only on the **source video files**.
> 
> It does **not** modify, rename, move, trim, or overwrite the originals.
> 
> What it does:
> - scans the folder recursively
> - reads each video
> - extracts audio from it
> - writes new files into:
>   - `<root>/_stt_output/audio_clean/...`
>   - `<root>/_stt_output/transcripts/...`
>   - `<root>/_stt_output/manifest.json`
> 
> The only files it writes are the **new output files** in that `_stt_output` folder.
> 
> One technical note:
> - `ffmpeg -y` means **overwrite output files if they already exist**
> - that applies to the generated `.wav`, `.txt`, `.srt`, and manifest files
> - **not** the source videos
> 
> So: **source files are untouched; outputs can be replaced on rerun.**
> 
> If you want, I can give you a slightly safer version that also skips files already processed instead of overwriting outputs.

### User
> what wisper model to use?

### Assistant
> I’m checking the current model options so I don’t steer you into an outdated pick. The answer depends mostly on whether you care more about speed, accuracy, or weak-audio recovery.

### Assistant
> For **your use case**, use:
> 
> ## Best default
> **`small`** if you want the safest balance of speed and accuracy on normal hardware. OpenAI lists `small` at about **~2 GB VRAM** and roughly **~4x** the speed of the large model, and notes that English-only variants exist for the smaller models. citeturn702391view1
> 
> ## If audio is messy and accuracy matters more
> **`medium.en`** for English-only work when the recordings are rough, quiet, noisy, or inconsistent. OpenAI says the `.en` models tend to perform better for English-only tasks, though the gain is much more noticeable on `tiny.en` and `base.en` than on `small.en` and `medium.en`. `medium` is also a step up in capacity, but needs about **~5 GB VRAM** and is slower than `small`. citeturn702391view1
> 
> ## If you want the best quality and have real hardware
> **`large-v3`** if you have a decent GPU and care more about accuracy than speed. `faster-whisper` explicitly supports loading `large-v3`, and OpenAI’s large family is the high-accuracy end of the lineup. citeturn702391view0turn702391view1
> 
> ## My actual recommendation for you
> Use this order:
> 
> 1. **Start with `small`**
> 2. If the transcripts are missing words or mangling speech, move to **`medium.en`**
> 3. If you have GPU headroom and want the strongest output, move to **`large-v3`**
> 
> ## What I would not do
> - **`tiny` / `base`** unless speed matters more than quality. They are fast, but that is where quality drops hardest. OpenAI specifically notes the English-only boost is strongest there, which is another way of saying those smaller models need the help. citeturn702391view1
> - **`turbo`** unless you switch to a workflow that explicitly supports it the way you want. OpenAI says `turbo` is an optimized `large-v3` with minimal accuracy loss and good English transcription performance, but your current script path is built around `faster-whisper`, whose documented direct model examples center on `large-v3` and its converted/distilled variants. citeturn702391view1turn702391view0turn702391view2
> 
> ## Clean answer
> For your script **right now**: set the default to **`small`**.
> 
> If you want, I’ll patch your script so it:
> - defaults to `small`
> - automatically switches to `medium.en` for English
> - skips already-processed files
> - writes a failure log instead of just printing errors

### User
> lets see what we can get fast then we can identify videos that need rechecked.

### Assistant
> You want a triage pass, not perfection. I’m verifying the model tradeoff against current docs and I’ll give you the blunt pick plus the rerun rule.

### Assistant
> Yes. For a **fast first-pass triage**, use **`base.en`**. The English-only variants exist for `tiny`, `base`, `small`, and `medium`, and they’re the right fit when your source language is only English. OpenAI’s model table also makes clear the smaller models trade accuracy for speed, while `faster-whisper` is designed specifically to run Whisper faster and with lower memory use than the original Python implementation. citeturn327910search0turn327910search1turn327910search14
> 
> ## My recommendation
> - **Phase 1 / fast sweep:** `base.en`
> - **Phase 2 / recheck bad videos:** `medium.en`
> - **Phase 3 / only the worst problem files:** `large-v3`
> 
> That gives you a practical funnel instead of wasting hours over-processing everything. OpenAI documents `base` as much lighter than `small`/`medium`, while `medium.en` is the stronger English-only step up when you need a cleaner second pass. citeturn327910search0turn327910search2
> 
> ## Why not start with `small`?
> You *can*, but if the goal is **speed first, identify failures later**, `small` is slower than `base` and defeats your triage logic a bit. Start cheap, then escalate only where the transcript looks obviously weak. The model lineup is explicitly a speed/accuracy tradeoff. citeturn327910search0turn327910search2
> 
> ## Clean operating rule
> Use this:
> - If transcript is **mostly readable** → keep it
> - If it has **missing chunks, speaker confusion, heavy gibberish, or obvious dropped words** → rerun that file with `medium.en`
> - If audio is **truly nasty** and still bad after that → rerun with `large-v3`
> 
> ## Change this in your script
> Set the default prompt from:
> 
> ```python
> model_size = prompt_text("Whisper model to use", "small")
> ```
> 
> to:
> 
> ```python
> model_size = prompt_text("Whisper model to use", "base.en")
> ```
> 
> And if you want the blunt truth: for your “scan a pile of videos and flag the ugly ones” workflow, **`base.en` is the correct first move**. `tiny.en` is faster, but that starts getting too sloppy unless the audio is already pretty clean. OpenAI’s model table shows `tiny` and `base` at the smallest end of the range, where the speed gain is bought with reduced accuracy. citeturn327910search0turn327910search2
> 
> I can also patch the script so it automatically writes a **“needs_recheck” CSV** based on transcript confidence signals.

### User
> Requirement already satisfied: idna<4,>=2.5 in C:\Users\codyr\AppData\Roaming\Python\Python314\site-packages (from requests->huggingface-hub>=0.21->faster-whisper) (3.11)

> Requirement already satisfied: urllib3<3,>=1.21.1 in C:\Users\codyr\AppData\Roaming\Python\Python314\site-packages (from requests->huggingface-hub>=0.21->faster-whisper) (2.5.0)

> Requirement already satisfied: certifi>=2017.4.17 in C:\Users\codyr\AppData\Roaming\Python\Python314\site-packages (from requests->huggingface-hub>=0.21->faster-whisper) (2025.10.5)

> Requirement already satisfied: mpmath<1.4,>=1.1.0 in C:\Users\codyr\AppData\Roaming\Python\Python314\site-packages (from sympy->onnxruntime<2,>=1.14->faster-whisper) (1.3.0)

> Using cached faster_whisper-1.2.1-py3-none-any.whl (1.1 MB)

> Using cached ctranslate2-4.7.1-cp314-cp314-win_amd64.whl (19.1 MB)

> Using cached onnxruntime-1.24.4-cp314-cp314-win_amd64.whl (12.9 MB)

> Using cached av-17.0.0-cp311-abi3-win_amd64.whl (28.9 MB)

> Using cached flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)

> Installing collected packages: flatbuffers, ctranslate2, av, onnxruntime, faster-whisper

> Successfully installed av-17.0.0 ctranslate2-4.7.1 faster-whisper-1.2.1 flatbuffers-25.12.19 onnxruntime-1.24.4

> PS C:\QiLabstranscriber> python video_stt_pipeline.py

> Enter the folder path to scan: G:\My Drive\QiVault\04_Projects\3.3_cases\30.06_CASE_FCFCU\content\1_Evidence\03_Video\2025-12-09_Removal_Day

> Produce speech-to-text too? [Y/n]: y

> Apply cleanup filters before STT? [Y/n]: y

> Whisper model to use [small]: base.en

> 

> Root: G:\My Drive\QiVault\04_Projects\3.3_cases\30.06_CASE_FCFCU\content\1_Evidence\03_Video\2025-12-09_Removal_Day

> Found 174 video file(s).

> Output: G:\My Drive\QiVault\04_Projects\3.3_cases\30.06_CASE_FCFCU\content\1_Evidence\03_Video\2025-12-09_Removal_Day\_stt_output

> Cleanup: ON

> STT: ON

> Model: base.en

> Device: cpu

> 

> [1/174] G:\My Drive\QiVault\04_Projects\3.3_cases\30.06_CASE_FCFCU\content\1_Evidence\03_Video\2025-12-09_Removal_Day\08-56-18_2a.mkv

>   - Audio written: G:\My Drive\QiVault\04_Projects\3.3_cases\30.06_CASE_FCFCU\content\1_Evidence\03_Video\2025-12-09_Removal_Day\_stt_output\audio_clean\08-56-18_2a.clean.wav

> Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`

> config.json: 2.23kB [00:00, 5.22MB/s]

> vocabulary.txt: 0.00B [00:00, ?B/s]C:\Users\codyr\AppData\Roaming\Python\Python314\site-packages\huggingface_hub\file_download.py:143: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\Users\codyr\.cache\huggingface\hub\models--Systran--faster-whisper-base.en. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.

> To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development

>   warnings.warn(message)

> vocabulary.txt: 422kB [00:00, 617kB/s]

> tokenizer.json: 2.13MB [00:01, 1.87MB/s]

> model.bin:  79%|█████████████████████████████████████████████████████████████████▉                 | 115M/145M [01:17<00:22, 1.30MB/s]

### Assistant
> That’s normal. Nothing is broken.
> 
> ## What’s happening
> 
> Your script successfully:
> 
> - found the folder
> - found **174 videos**
> - extracted audio from the first file
> - started downloading the **`base.en` model** for the first transcription run
> 
> That `model.bin: 79% ...` line means it is still downloading the model. After that finishes, it should start transcribing.
> 
> ## The warnings mean this
> 
> ### 1. `hf_xet` not installed
> Not a problem. That is just an **optional faster download backend** for Hugging Face.
> 
> Effect:
> - model still downloads
> - just maybe not as efficiently
> 
> You can ignore it, or install later:
> 
> ```bash
> pip install hf_xet
> ```
> 
> ### 2. symlink warning on Windows
> Also not fatal.
> 
> Effect:
> - Hugging Face cache will use **more disk space**
> - downloads/transcription still work fine
> 
> This happens because Windows symlink support is not fully enabled for your current environment.
> 
> You can ignore it, or reduce the warning by:
> - enabling **Developer Mode** in Windows
> - or running terminal as admin
> 
> But again: **not required**
> 
> ## What to expect next
> 
> Once the model finishes downloading the first time:
> 
> - it gets cached
> - later files will **not** redownload the model
> - processing continues file by file
> 
> So the first transcription is always the slow, annoying one.
> 
> ## Important reality check
> 
> You are on:
> 
> - **174 files**
> - **CPU**
> - **cleanup ON**
> - **STT ON**
> 
> That will take a while. Not broken. Just slow.
> 
> ## Best move right now
> 
> Let it finish the first file.
> 
> If it completes and writes:
> - `.txt`
> - `.srt`
> 
> then the pipeline is working.
> 
> ## If you want less friction later
> 
> Install this too:
> 
> ```bash
> pip install hf_xet
> ```
> 
> And if you want, I can give you a patched version that:
> - skips already processed files
> - writes a `needs_recheck.csv`
> - logs timing per file
> - avoids redoing work if the run gets interrupted

### User
> ok i got it down to tlike 40 videos that need like really really detailed, like clean up and try again.

### Assistant
> I’m checking the current model support and the best levers for second-pass recovery so I can give you a real upgrade path, not folklore.

### Assistant
> Good. That’s the right workflow.
> 
> ## What to use for the 40 problem files
> 
> ### Default second pass
> Use **`medium.en`**. For English-only jobs, the `.en` variants are intended for English, and `medium.en` is the next serious step up from `base.en`; OpenAI’s model table lists `medium` as slower and larger than `base`, but materially stronger. citeturn296339view1
> 
> ### Third pass for the real garbage
> Use **`large-v3`** only on the worst leftovers. `faster-whisper` supports loading `large-v3` directly, but it is heavier than the smaller models. citeturn296339view0turn296339view1
> 
> ## Do not just do one rerun
> For bad files, do **two reruns**:
> 
> 1. **`medium.en` with cleanup ON**
> 2. **`medium.en` with cleanup OFF**
> 
> Why: FFmpeg filters are literally transforming the signal in a filtergraph, and denoisers/normalizers can help one file while hurting another. That is an inference, but it is exactly the kind of tradeoff you should expect once you start chaining denoise and loudness filters. citeturn296339view2turn296339view3turn314962view3
> 
> ## Best retry ladder
> 
> ### Pass A
> `medium.en` + your current cleanup chain
> 
> ### Pass B
> `medium.en` + no cleanup
> 
> ### Pass C
> `large-v3` + whichever audio sounded more intelligible between A and B
> 
> That keeps you from wasting time polishing already-lost audio.
> 
> ## Better cleanup chain for retry work
> Your current chain is decent, but for ugly evidence audio I’d switch to this as the **stronger retry preset**:
> 
> ```text
> highpass=f=90,lowpass=f=7000,afftdn=nr=18:nf=-40:tn=1,loudnorm=I=-16:LRA=7:TP=-1.5
> ```
> 
> Why this is reasonable:
> - `highpass` / `lowpass` trim junk outside the speech-useful band. FFmpeg includes both as native filters. citeturn314962view4turn314962view5
> - `afftdn` is FFmpeg’s FFT denoiser, and it supports `nr`, `nf`, and automatic noise tracking via `tn=1`. citeturn296339view3
> - `loudnorm` is FFmpeg’s loudness normalization filter. citeturn314962view3
> 
> ## Optional extra for long dead air
> If some clips have huge stretches of silence before or after speech, you can add `silenceremove`, because FFmpeg supports removing silence from the beginning, middle, or end. citeturn314962view0
> 
> Example:
> 
> ```text
> silenceremove=stop_periods=-1:stop_duration=1:stop_threshold=-50dB
> ```
> 
> Do **not** blindly apply that to everything if timing/context matters. It is useful for STT prep, but it changes the audio timeline.
> 
> ## One thing not to overcomplicate
> FFmpeg also has `arnndn`, which is speech-noise reduction using recurrent neural networks, but it requires a separate model file. That is real, but it adds setup friction. I would not start there unless the 40 files are truly awful. citeturn314962view1
> 
> ## Blunt recommendation
> Given you’re on CPU, do this:
> 
> - rerun the 40 with **`medium.en`**
> - first with **cleanup ON**
> - then only rerun failures with **cleanup OFF**
> - reserve **`large-v3`** for the final handful
> 
> That is the best time-vs-quality trade.
> 
> ## Change these commands
> 
> ### Strong retry pass
> ```bash
> python video_stt_pipeline.py --path "G:\path\to\retry_folder" --model medium.en --filter-chain "highpass=f=90,lowpass=f=7000,afftdn=nr=18:nf=-40:tn=1,loudnorm=I=-16:LRA=7:TP=-1.5"
> ```
> 
> ### Control pass with no cleanup
> ```bash
> python video_stt_pipeline.py --path "G:\path\to\retry_folder" --model medium.en --no-cleanup
> ```
> 
> ### Final salvage pass
> ```bash
> python video_stt_pipeline.py --path "G:\path\to\retry_folder" --model large-v3 --no-cleanup
> ```
> 
> ## One script fix you should make
> Change the default prompt from:
> 
> ```python
> model_size = prompt_text("Whisper model to use", "small")
> ```
> 
> to:
> 
> ```python
> model_size = prompt_text("Whisper model to use", "base.en")
> ```
> 
> and for second-pass work, manually enter `medium.en`.
> 
> The real bottleneck now is not discovery. It’s **triage discipline**. Don’t reprocess all 174. Hammer the 40 with a structured retry ladder and move on.
> 
> I can patch the script next so it accepts a **CSV or text file of specific videos to retry** instead of forcing you to make a separate folder.

### User
> ok i have put the cleaned up files in the folder so it said no files found because those are .wav files.

### Assistant
> Yep. That’s expected.
> 
> Your current script is only looking for **video extensions**, so when you point it at a folder full of `.wav` files it says **no files found**.
> 
> ## Why
> 
> This line is the reason:
> 
> ```python
> VIDEO_EXTENSIONS = {
>     ".mp4", ".mov", ".mkv", ".avi", ".wmv", ".m4v", ".webm",
>     ".flv", ".mpeg", ".mpg", ".ts", ".mts", ".m2ts", ".3gp"
> }
> ```
> 
> And this function only scans for those:
> 
> ```python
> def discover_videos(root: Path) -> list[Path]:
>     return sorted(
>         p for p in root.rglob("*")
>         if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS
>     )
> ```
> 
> ## What you need now
> 
> You need the script to support **audio input files** too, especially:
> - `.wav`
> - maybe `.mp3`
> - `.m4a`
> - `.aac`
> - `.flac`
> 
> ## Best fix
> 
> Change the script so it can process:
> - video files → extract audio first
> - audio files → skip extraction and go straight to cleanup/transcription
> 
> ---
> 
> # Patch it like this
> 
> ## 1. Replace your extension block with this
> 
> ```python
> VIDEO_EXTENSIONS = {
>     ".mp4", ".mov", ".mkv", ".avi", ".wmv", ".m4v", ".webm",
>     ".flv", ".mpeg", ".mpg", ".ts", ".mts", ".m2ts", ".3gp"
> }
> 
> AUDIO_EXTENSIONS = {
>     ".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".wma"
> }
> 
> SUPPORTED_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS
> ```
> 
> ---
> 
> ## 2. Replace `discover_videos()` with this
> 
> ```python
> def discover_media(root: Path) -> list[Path]:
>     return sorted(
>         p for p in root.rglob("*")
>         if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
>     )
> ```
> 
> ---
> 
> ## 3. Add this helper
> 
> ```python
> def is_audio_file(path: Path) -> bool:
>     return path.suffix.lower() in AUDIO_EXTENSIONS
> ```
> 
> ---
> 
> ## 4. Add this function for audio cleanup/conversion
> 
> ```python
> def clean_audio_file(
>     ffmpeg_bin: str,
>     input_audio: Path,
>     output_wav: Path,
>     cleanup: bool,
>     filter_chain: str,
> ) -> None:
>     ensure_parent(output_wav)
> 
>     cmd = [
>         ffmpeg_bin,
>         "-y",
>         "-hide_banner",
>         "-loglevel", "error",
>         "-i", str(input_audio),
>         "-ac", "1",
>         "-ar", "16000",
>         "-c:a", "pcm_s16le",
>     ]
> 
>     if cleanup:
>         cmd += ["-af", filter_chain]
> 
>     cmd.append(str(output_wav))
> 
>     result = run_cmd(cmd)
>     if result.returncode != 0:
>         raise RuntimeError(result.stderr.strip() or "ffmpeg audio cleanup failed")
> ```
> 
> ---
> 
> ## 5. Change this line in `main()`
> 
> Replace:
> 
> ```python
> video_files = discover_videos(root)
> if not video_files:
>     print("No video files found.")
>     return
> ```
> 
> with:
> 
> ```python
> media_files = discover_media(root)
> if not media_files:
>     print("No supported media files found.")
>     return
> ```
> 
> ---
> 
> ## 6. Change the print count
> 
> Replace:
> 
> ```python
> print(f"Found {len(video_files)} video file(s).")
> ```
> 
> with:
> 
> ```python
> print(f"Found {len(media_files)} media file(s).")
> ```
> 
> ---
> 
> ## 7. Replace the main processing loop
> 
> Replace your current loop with this:
> 
> ```python
> for index, media_path in enumerate(media_files, start=1):
>     print(f"[{index}/{len(media_files)}] {media_path}")
> 
>     audio_out, txt_out, srt_out = build_output_paths(root, media_path, out_root)
> 
>     try:
>         txt_path_str = None
>         srt_path_str = None
> 
>         if is_audio_file(media_path):
>             clean_audio_file(
>                 ffmpeg_bin=ffmpeg_bin,
>                 input_audio=media_path,
>                 output_wav=audio_out,
>                 cleanup=cleanup,
>                 filter_chain=args.filter_chain,
>             )
>         else:
>             if not has_audio_stream(ffprobe_bin, media_path):
>                 msg = "Skipped: no audio stream found"
>                 print(f"  - {msg}")
>                 results.append(FileResult(
>                     video=str(media_path),
>                     status="skipped_no_audio",
>                     error=msg,
>                 ))
>                 continue
> 
>             extract_and_clean_audio(
>                 ffmpeg_bin=ffmpeg_bin,
>                 video_path=media_path,
>                 output_wav=audio_out,
>                 cleanup=cleanup,
>                 filter_chain=args.filter_chain,
>             )
> 
>         print(f"  - Audio written: {audio_out}")
> 
>         if do_stt:
>             transcribe_audio(
>                 audio_path=audio_out,
>                 txt_path=txt_out,
>                 srt_path=srt_out,
>                 model_size=model_size,
>                 device=device,
>             )
>             txt_path_str = str(txt_out)
>             srt_path_str = str(srt_out)
>             print(f"  - Transcript written: {txt_out}")
>             print(f"  - Subtitles written:  {srt_out}")
> 
>         results.append(FileResult(
>             video=str(media_path),
>             status="ok",
>             audio_path=str(audio_out),
>             txt_path=txt_path_str,
>             srt_path=srt_path_str,
>         ))
> 
>     except Exception as exc:
>         print(f"  - ERROR: {exc}")
>         results.append(FileResult(
>             video=str(media_path),
>             status="error",
>             error=str(exc),
>         ))
> ```
> 
> ---
> 
> ## 8. Optional but smart: rename `video` in `FileResult`
> 
> Change:
> 
> ```python
> @dataclass
> class FileResult:
>     video: str
> ```
> 
> to:
> 
> ```python
> @dataclass
> class FileResult:
>     source: str
> ```
> 
> And update references accordingly. Not required, but cleaner.
> 
> ---
> 
> # Fast answer
> 
> Right now your script only handles **video input**.
> 
> You now need it to handle **audio input too**.
> 
> ## Easiest path
> Patch it with the changes above, then point it at your `.wav` folder.
> 
> ## Dirty workaround
> Put the original videos back in and let the script redo extraction.  
> That works, but it’s stupid if you already cleaned the WAVs.
> 
> The patch is the correct move.
> 
> If you want, I can give you the **fully rewritten script** in one clean block so you can just replace the whole file instead of doing surgery.

### User
> PS C:\QiLabs> & C:/Users/codyr/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe c:/QiLabs/_QiOne_MonoRepo_v0.4/_App_Experiments/video-transcriber/video_stt_pipeline.py

> Enter the folder path to scan: G:\My Drive\QiVault\04_Projects\3.3_cases\30.06_CASE_FCFCU\content\1_Evidence\03_Video\2025-12-09_Removal_Day\redo

> Produce speech-to-text too? [Y/n]: y

> Apply cleanup filters before STT? [Y/n]: y

> Whisper model to use [small]: medium.en

> Traceback (most recent call last):

>   File "c:\QiLabs\_QiOne_MonoRepo_v0.4\_App_Experiments\video-transcriber\video_stt_pipeline.py", line 372, in <module>

>     main()

>     ~~~~^^

>   File "c:\QiLabs\_QiOne_MonoRepo_v0.4\_App_Experiments\video-transcriber\video_stt_pipeline.py", line 284, in main

>     video_files = discover_videos(root)

>                   ^^^^^^^^^^^^^^^

> NameError: name 'discover_videos' is not defined. Did you mean: 'discover_media'?

> PS C:\QiLabs> , just redo the whole thing and have it interactive for pass selection small, medium etc. #!/usr/bin/env python3

> """

> Recursive video -> cleaned audio -> optional English STT pipeline.

> 

> What it does:

> 1. Prompts for a root folder (unless --path is passed)

> 2. Recursively finds video files

> 3. Extracts audio to 16 kHz mono WAV

> 4. Applies conservative speech-focused cleanup with FFmpeg

> 5. Optionally transcribes to English .txt and .srt using faster-whisper

> 

> Outputs go into:

> <root>/_stt_output/audio_clean/...

> <root>/_stt_output/transcripts/...

> <root>/_stt_output/manifest.json

> """

> 

> from __future__ import annotations

> 

> import argparse

> import json

> import shutil

> import subprocess

> import sys

> from dataclasses import asdict, dataclass

> from pathlib import Path

> from typing import Optional

> 

> VIDEO_EXTENSIONS = {

>     ".mp4", ".mov", ".mkv", ".avi", ".wmv", ".m4v", ".webm",

>     ".flv", ".mpeg", ".mpg", ".ts", ".mts", ".m2ts", ".3gp"

> }

> 

> AUDIO_EXTENSIONS = {

>     ".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".wma"

> }

> 

> SUPPORTED_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS

> 

> # Conservative cleanup chain for speech prep:

> # - highpass: remove low rumble

> # - lowpass: remove useless very high frequencies for speech STT

> # - afftdn: light spectral denoise

> # - loudnorm: stabilize volume

> DEFAULT_FILTER_CHAIN = (

>     "highpass=f=80,"

>     "lowpass=f=7500,"

>     "afftdn=nr=12:nf=-30,"

>     "loudnorm=I=-16:LRA=11:TP=-1.5"

> )

> 

> 

> @dataclass

> class FileResult:

>     video: str

>     status: str

>     audio_path: Optional[str] = None

>     txt_path: Optional[str] = None

>     srt_path: Optional[str] = None

>     error: Optional[str] = None

> 

> 

> def run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:

>     return subprocess.run(

>         cmd,

>         stdout=subprocess.PIPE,

>         stderr=subprocess.PIPE,

>         text=True,

>         check=False

>     )

> 

> 

> def require_binary(name: str) -> str:

>     path = shutil.which(name)

>     if not path:

>         print(f"ERROR: '{name}' was not found on PATH.")

>         sys.exit(1)

>     return path

> 

> 

> def prompt_path() -> Path:

>     while True:

>         raw = input("Enter the folder path to scan: ").strip().strip('"').strip("'")

>         path = Path(raw).expanduser()

>         if path.is_dir():

>             return path.resolve()

>         print("That path is not a valid folder. Try again.")

> 

> 

> def prompt_yes_no(question: str, default: bool = True) -> bool:

>     suffix = " [Y/n]: " if default else " [y/N]: "

>     raw = input(question + suffix).strip().lower()

>     if not raw:

>         return default

>     return raw in {"y", "yes"}

> 

> 

> def prompt_text(question: str, default: str) -> str:

>     raw = input(f"{question} [{default}]: ").strip()

>     return raw or default

> 

> 

> def discover_media(root: Path) -> list[Path]:

>     return sorted(

>         p for p in root.rglob("*")

>         if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS

>     )

> 

> 

> def has_audio_stream(ffprobe_bin: str, video_path: Path) -> bool:

>     cmd = [

>         ffprobe_bin,

>         "-v", "error",

>         "-select_streams", "a:0",

>         "-show_entries", "stream=codec_type",

>         "-of", "default=nw=1:nk=1",

>         str(video_path),

>     ]

>     result = run_cmd(cmd)

>     return result.returncode == 0 and "audio" in result.stdout.lower()

> 

> 

> def ensure_parent(path: Path) -> None:

>     path.parent.mkdir(parents=True, exist_ok=True)

> 

> 

> def extract_and_clean_audio(

>     ffmpeg_bin: str,

>     video_path: Path,

>     output_wav: Path,

>     cleanup: bool,

>     filter_chain: str,

> ) -> None:

>     ensure_parent(output_wav)

> 

>     cmd = [

>         ffmpeg_bin,

>         "-y",

>         "-hide_banner",

>         "-loglevel", "error",

>         "-i", str(video_path),

>         "-vn",

>         "-map", "0:a:0",

>         "-ac", "1",

>         "-ar", "16000",

>         "-c:a", "pcm_s16le",

>     ]

> 

>     if cleanup:

>         cmd += ["-af", filter_chain]

> 

>     cmd.append(str(output_wav))

> 

>     result = run_cmd(cmd)

>     if result.returncode != 0:

>         raise RuntimeError(result.stderr.strip() or "ffmpeg failed")

> 

> 

> def format_srt_timestamp(seconds: float) -> str:

>     total_ms = int(round(seconds * 1000))

>     hours = total_ms // 3_600_000

>     total_ms %= 3_600_000

>     minutes = total_ms // 60_000

>     total_ms %= 60_000

>     secs = total_ms // 1000

>     millis = total_ms % 1000

>     return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

> 

> 

> def write_transcript_files(txt_path: Path, srt_path: Path, segments: list) -> None:

>     ensure_parent(txt_path)

>     ensure_parent(srt_path)

> 

>     text_lines = []

>     srt_blocks = []

> 

>     for idx, seg in enumerate(segments, start=1):

>         text = (seg.text or "").strip()

>         if not text:

>             continue

> 

>         text_lines.append(text)

> 

>         start_ts = format_srt_timestamp(seg.start)

>         end_ts = format_srt_timestamp(seg.end)

>         srt_blocks.append(f"{idx}\n{start_ts} --> {end_ts}\n{text}\n")

> 

>     txt_path.write_text("\n".join(text_lines).strip() + "\n", encoding="utf-8")

>     srt_path.write_text("\n".join(srt_blocks).strip() + "\n", encoding="utf-8")

> 

> 

> def transcribe_audio(

>     audio_path: Path,

>     txt_path: Path,

>     srt_path: Path,

>     model_size: str,

>     device: str,

> ) -> None:

>     try:

>         from faster_whisper import WhisperModel

>     except ImportError as exc:

>         raise RuntimeError(

>             "faster-whisper is not installed. Run: pip install faster-whisper"

>         ) from exc

> 

>     compute_type = "float16" if device == "cuda" else "int8"

> 

>     model = WhisperModel(

>         model_size,

>         device=device,

>         compute_type=compute_type,

>     )

> 

>     segments_iter, info = model.transcribe(

>         str(audio_path),

>         language="en",

>         beam_size=5,

>         vad_filter=True,

>         condition_on_previous_text=False,

>     )

> 

>     segments = list(segments_iter)

>     if not segments:

>         ensure_parent(txt_path)

>         txt_path.write_text("", encoding="utf-8")

>         ensure_parent(srt_path)

>         srt_path.write_text("", encoding="utf-8")

>         return

> 

>     write_transcript_files(txt_path, srt_path, segments)

> 

> 

> def choose_default_device() -> str:

>     return "cuda" if shutil.which("nvidia-smi") else "cpu"

> 

> 

> def build_output_paths(root: Path, video_path: Path, out_root: Path) -> tuple[Path, Path, Path]:

>     rel = video_path.relative_to(root)

>     base_rel = rel.with_suffix("")  # remove only final suffix

> 

>     audio_out = (out_root / "audio_clean" / base_rel).with_suffix(".clean.wav")

>     txt_out = (out_root / "transcripts" / base_rel).with_suffix(".txt")

>     srt_out = (out_root / "transcripts" / base_rel).with_suffix(".srt")

>     return audio_out, txt_out, srt_out

> 

> 

> def parse_args() -> argparse.Namespace:

>     parser = argparse.ArgumentParser(

>         description="Recursively extract/clean audio from video files and optionally transcribe to English."

>     )

>     parser.add_argument("--path", type=str, help="Root folder to scan")

>     parser.add_argument("--no-stt", action="store_true", help="Only extract/clean audio; do not transcribe")

>     parser.add_argument("--no-cleanup", action="store_true", help="Extract audio without cleanup filters")

>     parser.add_argument("--model", type=str, default=None, help="Whisper model size (tiny, base, small, medium, large-v3, etc.)")

>     parser.add_argument("--device", type=str, default=None, choices=["cpu", "cuda"], help="Transcription device")

>     parser.add_argument("--filter-chain", type=str, default=DEFAULT_FILTER_CHAIN, help="Custom FFmpeg audio filter chain")

>     return parser.parse_args()

> 

> 

> def main() -> None:

>     args = parse_args()

> 

>     ffmpeg_bin = require_binary("ffmpeg")

>     ffprobe_bin = require_binary("ffprobe")

> 

>     root = Path(args.path).expanduser().resolve() if args.path else prompt_path()

>     if not root.is_dir():

>         print("ERROR: Provided path is not a folder.")

>         sys.exit(1)

> 

>     do_stt = not args.no_stt

>     cleanup = not args.no_cleanup

> 

>     if args.path is None:

>         do_stt = prompt_yes_no("Produce speech-to-text too?", default=True)

>         cleanup = prompt_yes_no("Apply cleanup filters before STT?", default=True)

> 

>     model_size = args.model

>     if do_stt and not model_size:

>         model_size = prompt_text("Whisper model to use", "small")

> 

>     device = args.device or choose_default_device()

> 

>     video_files = discover_videos(root)

>     if not video_files:

>         print("No video files found.")

>         return

> 

>     out_root = root / "_stt_output"

>     out_root.mkdir(parents=True, exist_ok=True)

> 

>     print(f"\nRoot: {root}")

>     print(f"Found {len(video_files)} video file(s).")

>     print(f"Output: {out_root}")

>     print(f"Cleanup: {'ON' if cleanup else 'OFF'}")

>     print(f"STT: {'ON' if do_stt else 'OFF'}")

>     if do_stt:

>         print(f"Model: {model_size}")

>         print(f"Device: {device}")

>     print()

> 

>     results: list[FileResult] = []

> 

>     for index, video_path in enumerate(video_files, start=1):

>         print(f"[{index}/{len(video_files)}] {video_path}")

> 

>         audio_out, txt_out, srt_out = build_output_paths(root, video_path, out_root)

> 

>         try:

>             if not has_audio_stream(ffprobe_bin, video_path):

>                 msg = "Skipped: no audio stream found"

>                 print(f"  - {msg}")

>                 results.append(FileResult(

>                     video=str(video_path),

>                     status="skipped_no_audio",

>                     error=msg,

>                 ))

>                 continue

> 

>             extract_and_clean_audio(

>                 ffmpeg_bin=ffmpeg_bin,

>                 video_path=video_path,

>                 output_wav=audio_out,

>                 cleanup=cleanup,

>                 filter_chain=args.filter_chain,

>             )

>             print(f"  - Audio written: {audio_out}")

> 

>             txt_path_str = None

>             srt_path_str = None

> 

>             if do_stt:

>                 transcribe_audio(

>                     audio_path=audio_out,

>                     txt_path=txt_out,

>                     srt_path=srt_out,

>                     model_size=model_size,

>                     device=device,

>                 )

>                 txt_path_str = str(txt_out)

>                 srt_path_str = str(srt_out)

>                 print(f"  - Transcript written: {txt_out}")

>                 print(f"  - Subtitles written:  {srt_out}")

> 

>             results.append(FileResult(

>                 video=str(video_path),

>                 status="ok",

>                 audio_path=str(audio_out),

>                 txt_path=txt_path_str,

>                 srt_path=srt_path_str,

>             ))

> 

>         except Exception as exc:

>             print(f"  - ERROR: {exc}")

>             results.append(FileResult(

>                 video=str(video_path),

>                 status="error",

>                 error=str(exc),

>             ))

> 

>     manifest_path = out_root / "manifest.json"

>     manifest_path.write_text(

>         json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False),

>         encoding="utf-8",

>     )

> 

>     print("\nDone.")

>     print(f"Manifest: {manifest_path}")

> 

> 

> if __name__ == "__main__":

>     main()

### Assistant
> The failure is exactly what it looks like: the script got half-converted to `discover_media()` but `main()` still called the dead `discover_videos()`. I’m replacing the whole thing cleanly so it handles both video and WAV retry folders without this Frankenstein drift.

### Assistant
> Yep. That broke because the script was in an **in-between state**.
> 
> You replaced part of it, but `main()` was still calling the old function:
> 
> ```python
> video_files = discover_videos(root)
> ```
> 
> That function no longer existed, so it died.
> 
> Below is a **full replacement**. Drop it in as the entire file and stop patching pieces.
> 
> ## What this version fixes
> 
> - handles **video and audio** files
> - works on folders full of **`.wav` retry files**
> - interactive **pass selection**
> - interactive **cleanup strength selection**
> - loads the Whisper model **once**, not once per file
> - can **skip already-processed** transcripts
> - writes outputs into a **named pass folder**
> - supports:
>   - fast triage
>   - balanced
>   - detailed
>   - max recovery
>   - custom model
> 
> ---
> 
> # Full replacement script
> 
> ```python
> #!/usr/bin/env python3
> """
> Recursive media -> cleaned audio -> optional English STT pipeline.
> 
> Features:
> - Recursively finds video AND audio files
> - Extracts audio from video or normalizes/cleans existing audio
> - Writes cleaned 16 kHz mono WAV files
> - Produces English .txt and .srt transcripts with faster-whisper
> - Interactive pass selection:
>     1) Fast triage      -> base.en
>     2) Balanced         -> small.en
>     3) Detailed retry   -> medium.en
>     4) Max recovery     -> large-v3
>     5) Custom model
> - Interactive cleanup selection:
>     1) None
>     2) Light
>     3) Strong
>     4) Custom FFmpeg filter chain
> - Optional skip of already-processed files
> - Outputs stored under a pass-specific folder:
>     <root>/_stt_output/<pass_name>/audio_clean/...
>     <root>/_stt_output/<pass_name>/transcripts/...
>     <root>/_stt_output/<pass_name>/manifest.json
> """
> 
> from __future__ import annotations
> 
> import argparse
> import json
> import shutil
> import subprocess
> import sys
> import time
> from dataclasses import asdict, dataclass
> from pathlib import Path
> from typing import Optional
> 
> VIDEO_EXTENSIONS = {
>     ".mp4", ".mov", ".mkv", ".avi", ".wmv", ".m4v", ".webm",
>     ".flv", ".mpeg", ".mpg", ".ts", ".mts", ".m2ts", ".3gp"
> }
> 
> AUDIO_EXTENSIONS = {
>     ".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".wma"
> }
> 
> SUPPORTED_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS
> 
> LIGHT_FILTER_CHAIN = (
>     "highpass=f=80,"
>     "lowpass=f=7500,"
>     "afftdn=nr=12:nf=-30,"
>     "loudnorm=I=-16:LRA=11:TP=-1.5"
> )
> 
> STRONG_FILTER_CHAIN = (
>     "highpass=f=90,"
>     "lowpass=f=7000,"
>     "afftdn=nr=18:nf=-40:tn=1,"
>     "loudnorm=I=-16:LRA=7:TP=-1.5"
> )
> 
> PASS_PRESETS = {
>     "1": {"label": "fast_triage", "model": "base.en"},
>     "2": {"label": "balanced", "model": "small.en"},
>     "3": {"label": "detailed_retry", "model": "medium.en"},
>     "4": {"label": "max_recovery", "model": "large-v3"},
> }
> 
> CLEANUP_PRESETS = {
>     "1": {"label": "none", "cleanup": False, "filter_chain": ""},
>     "2": {"label": "light", "cleanup": True, "filter_chain": LIGHT_FILTER_CHAIN},
>     "3": {"label": "strong", "cleanup": True, "filter_chain": STRONG_FILTER_CHAIN},
> }
> 
> 
> @dataclass
> class FileResult:
>     source: str
>     status: str
>     source_type: str
>     audio_path: Optional[str] = None
>     txt_path: Optional[str] = None
>     srt_path: Optional[str] = None
>     elapsed_seconds: Optional[float] = None
>     error: Optional[str] = None
> 
> 
> def run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
>     return subprocess.run(
>         cmd,
>         stdout=subprocess.PIPE,
>         stderr=subprocess.PIPE,
>         text=True,
>         check=False,
>     )
> 
> 
> def require_binary(name: str) -> str:
>     path = shutil.which(name)
>     if not path:
>         print(f"ERROR: '{name}' was not found on PATH.")
>         sys.exit(1)
>     return path
> 
> 
> def prompt_path() -> Path:
>     while True:
>         raw = input("Enter the folder path to scan: ").strip().strip('"').strip("'")
>         path = Path(raw).expanduser()
>         if path.is_dir():
>             return path.resolve()
>         print("That path is not a valid folder. Try again.")
> 
> 
> def prompt_yes_no(question: str, default: bool = True) -> bool:
>     suffix = " [Y/n]: " if default else " [y/N]: "
>     raw = input(question + suffix).strip().lower()
>     if not raw:
>         return default
>     return raw in {"y", "yes"}
> 
> 
> def prompt_text(question: str, default: str) -> str:
>     raw = input(f"{question} [{default}]: ").strip()
>     return raw or default
> 
> 
> def prompt_choice(question: str, choices: set[str], default: str) -> str:
>     while True:
>         raw = input(f"{question} [{default}]: ").strip()
>         if not raw:
>             return default
>         if raw in choices:
>             return raw
>         print(f"Invalid choice. Valid options: {', '.join(sorted(choices))}")
> 
> 
> def choose_default_device() -> str:
>     return "cuda" if shutil.which("nvidia-smi") else "cpu"
> 
> 
> def discover_media(root: Path) -> list[Path]:
>     return sorted(
>         p for p in root.rglob("*")
>         if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
>     )
> 
> 
> def is_audio_file(path: Path) -> bool:
>     return path.suffix.lower() in AUDIO_EXTENSIONS
> 
> 
> def sanitize_name(value: str) -> str:
>     safe = "".join(c if c.isalnum() or c in {"-", "_"} else "_" for c in value.strip())
>     safe = "_".join(part for part in safe.split("_") if part)
>     return safe or "run"
> 
> 
> def ensure_parent(path: Path) -> None:
>     path.parent.mkdir(parents=True, exist_ok=True)
> 
> 
> def has_audio_stream(ffprobe_bin: str, video_path: Path) -> bool:
>     cmd = [
>         ffprobe_bin,
>         "-v", "error",
>         "-select_streams", "a:0",
>         "-show_entries", "stream=codec_type",
>         "-of", "default=nw=1:nk=1",
>         str(video_path),
>     ]
>     result = run_cmd(cmd)
>     return result.returncode == 0 and "audio" in result.stdout.lower()
> 
> 
> def build_output_paths(root: Path, source_path: Path, out_root: Path) -> tuple[Path, Path, Path]:
>     rel = source_path.relative_to(root)
>     base_rel = rel.with_suffix("")
>     audio_out = (out_root / "audio_clean" / base_rel).with_suffix(".clean.wav")
>     txt_out = (out_root / "transcripts" / base_rel).with_suffix(".txt")
>     srt_out = (out_root / "transcripts" / base_rel).with_suffix(".srt")
>     return audio_out, txt_out, srt_out
> 
> 
> def extract_or_clean_to_wav(
>     ffmpeg_bin: str,
>     input_path: Path,
>     output_wav: Path,
>     cleanup: bool,
>     filter_chain: str,
>     treat_as_audio: bool,
> ) -> None:
>     ensure_parent(output_wav)
> 
>     cmd = [
>         ffmpeg_bin,
>         "-y",
>         "-hide_banner",
>         "-loglevel", "error",
>         "-i", str(input_path),
>     ]
> 
>     if not treat_as_audio:
>         cmd += ["-vn"]
> 
>     cmd += [
>         "-ac", "1",
>         "-ar", "16000",
>         "-c:a", "pcm_s16le",
>     ]
> 
>     if cleanup and filter_chain:
>         cmd += ["-af", filter_chain]
> 
>     cmd.append(str(output_wav))
> 
>     result = run_cmd(cmd)
>     if result.returncode != 0:
>         raise RuntimeError(result.stderr.strip() or "ffmpeg failed")
> 
> 
> def format_srt_timestamp(seconds: float) -> str:
>     total_ms = int(round(seconds * 1000))
>     hours = total_ms // 3_600_000
>     total_ms %= 3_600_000
>     minutes = total_ms // 60_000
>     total_ms %= 60_000
>     secs = total_ms // 1000
>     millis = total_ms % 1000
>     return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
> 
> 
> def write_transcript_files(txt_path: Path, srt_path: Path, segments: list) -> None:
>     ensure_parent(txt_path)
>     ensure_parent(srt_path)
> 
>     text_lines = []
>     srt_blocks = []
> 
>     for idx, seg in enumerate(segments, start=1):
>         text = (seg.text or "").strip()
>         if not text:
>             continue
> 
>         text_lines.append(text)
>         start_ts = format_srt_timestamp(seg.start)
>         end_ts = format_srt_timestamp(seg.end)
>         srt_blocks.append(f"{idx}\n{start_ts} --> {end_ts}\n{text}\n")
> 
>     txt_content = "\n".join(text_lines).strip()
>     srt_content = "\n".join(srt_blocks).strip()
> 
>     txt_path.write_text((txt_content + "\n") if txt_content else "", encoding="utf-8")
>     srt_path.write_text((srt_content + "\n") if srt_content else "", encoding="utf-8")
> 
> 
> def load_whisper_model(model_size: str, device: str):
>     try:
>         from faster_whisper import WhisperModel
>     except ImportError as exc:
>         raise RuntimeError(
>             "faster-whisper is not installed. Run: pip install faster-whisper"
>         ) from exc
> 
>     compute_type = "float16" if device == "cuda" else "int8"
> 
>     return WhisperModel(
>         model_size,
>         device=device,
>         compute_type=compute_type,
>     )
> 
> 
> def transcribe_audio_with_model(
>     model,
>     audio_path: Path,
>     txt_path: Path,
>     srt_path: Path,
> ) -> None:
>     segments_iter, info = model.transcribe(
>         str(audio_path),
>         language="en",
>         beam_size=5,
>         vad_filter=True,
>         condition_on_previous_text=False,
>     )
> 
>     segments = list(segments_iter)
> 
>     if not segments:
>         ensure_parent(txt_path)
>         ensure_parent(srt_path)
>         txt_path.write_text("", encoding="utf-8")
>         srt_path.write_text("", encoding="utf-8")
>         return
> 
>     write_transcript_files(txt_path, srt_path, segments)
> 
> 
> def parse_args() -> argparse.Namespace:
>     parser = argparse.ArgumentParser(
>         description="Recursively extract/clean audio from media files and optionally transcribe to English."
>     )
>     parser.add_argument("--path", type=str, help="Root folder to scan")
>     parser.add_argument("--no-stt", action="store_true", help="Only extract/clean audio; do not transcribe")
>     parser.add_argument("--device", type=str, default=None, choices=["cpu", "cuda"], help="Transcription device")
>     parser.add_argument("--model", type=str, default=None, help="Whisper model name")
>     parser.add_argument("--no-cleanup", action="store_true", help="Do not apply cleanup filters")
>     parser.add_argument("--filter-chain", type=str, default=None, help="Custom FFmpeg filter chain")
>     parser.add_argument("--pass-label", type=str, default=None, help="Custom output pass label")
>     parser.add_argument("--skip-existing", action="store_true", help="Skip files whose .txt and .srt already exist")
>     return parser.parse_args()
> 
> 
> def interactive_pass_selection() -> tuple[str, str]:
>     print("\nChoose transcription pass:")
>     print("  1) Fast triage     -> base.en")
>     print("  2) Balanced        -> small.en")
>     print("  3) Detailed retry  -> medium.en")
>     print("  4) Max recovery    -> large-v3")
>     print("  5) Custom model")
> 
>     choice = prompt_choice("Select pass", {"1", "2", "3", "4", "5"}, "1")
> 
>     if choice == "5":
>         model = prompt_text("Enter custom model name", "medium.en")
>         label = sanitize_name(prompt_text("Enter pass label", model))
>         return model, label
> 
>     preset = PASS_PRESETS[choice]
>     return preset["model"], preset["label"]
> 
> 
> def interactive_cleanup_selection() -> tuple[bool, str, str]:
>     print("\nChoose cleanup level:")
>     print("  1) None")
>     print("  2) Light speech cleanup")
>     print("  3) Strong retry cleanup")
>     print("  4) Custom FFmpeg filter chain")
> 
>     choice = prompt_choice("Select cleanup", {"1", "2", "3", "4"}, "2")
> 
>     if choice == "4":
>         custom = prompt_text("Enter custom FFmpeg filter chain", STRONG_FILTER_CHAIN)
>         return True, custom, "custom"
> 
>     preset = CLEANUP_PRESETS[choice]
>     return preset["cleanup"], preset["filter_chain"], preset["label"]
> 
> 
> def main() -> None:
>     args = parse_args()
> 
>     ffmpeg_bin = require_binary("ffmpeg")
>     ffprobe_bin = require_binary("ffprobe")
> 
>     root = Path(args.path).expanduser().resolve() if args.path else prompt_path()
>     if not root.is_dir():
>         print("ERROR: Provided path is not a folder.")
>         sys.exit(1)
> 
>     do_stt = not args.no_stt
>     device = args.device or choose_default_device()
> 
>     if do_stt:
>         if args.model:
>             model_size = args.model
>             pass_label = sanitize_name(args.pass_label or args.model)
>         else:
>             model_size, default_pass_label = interactive_pass_selection()
>             pass_label = sanitize_name(args.pass_label or default_pass_label)
>     else:
>         model_size = ""
>         pass_label = sanitize_name(args.pass_label or "audio_only")
> 
>     if args.no_cleanup:
>         cleanup = False
>         filter_chain = ""
>         cleanup_label = "none"
>     elif args.filter_chain:
>         cleanup = True
>         filter_chain = args.filter_chain
>         cleanup_label = "custom"
>     else:
>         cleanup, filter_chain, cleanup_label = interactive_cleanup_selection()
> 
>     skip_existing = args.skip_existing
>     if not args.skip_existing:
>         skip_existing = prompt_yes_no("Skip files that already have both .txt and .srt outputs?", default=True)
> 
>     media_files = discover_media(root)
>     if not media_files:
>         print("No supported media files found.")
>         return
> 
>     out_root = root / "_stt_output" / f"{pass_label}__cleanup_{cleanup_label}"
>     out_root.mkdir(parents=True, exist_ok=True)
> 
>     print(f"\nRoot: {root}")
>     print(f"Found {len(media_files)} media file(s).")
>     print(f"Output: {out_root}")
>     print(f"Cleanup: {'ON' if cleanup else 'OFF'}")
>     if cleanup:
>         print(f"Cleanup profile: {cleanup_label}")
>     print(f"STT: {'ON' if do_stt else 'OFF'}")
>     if do_stt:
>         print(f"Model: {model_size}")
>         print(f"Device: {device}")
>     print(f"Skip existing: {'ON' if skip_existing else 'OFF'}")
>     print()
> 
>     model = None
>     if do_stt:
>         print("Loading Whisper model once...")
>         model = load_whisper_model(model_size=model_size, device=device)
>         print("Model loaded.\n")
> 
>     results: list[FileResult] = []
>     processed = 0
>     skipped = 0
>     errors = 0
> 
>     for index, source_path in enumerate(media_files, start=1):
>         start_time = time.perf_counter()
>         source_type = "audio" if is_audio_file(source_path) else "video"
>         print(f"[{index}/{len(media_files)}] {source_path}")
> 
>         audio_out, txt_out, srt_out = build_output_paths(root, source_path, out_root)
> 
>         try:
>             if skip_existing and do_stt and txt_out.exists() and srt_out.exists():
>                 print("  - Skipped: transcript outputs already exist")
>                 skipped += 1
>                 results.append(FileResult(
>                     source=str(source_path),
>                     status="skipped_existing",
>                     source_type=source_type,
>                     audio_path=str(audio_out) if audio_out.exists() else None,
>                     txt_path=str(txt_out),
>                     srt_path=str(srt_out),
>                     elapsed_seconds=round(time.perf_counter() - start_time, 3),
>                 ))
>                 continue
> 
>             if source_type == "video" and not has_audio_stream(ffprobe_bin, source_path):
>                 msg = "Skipped: no audio stream found"
>                 print(f"  - {msg}")
>                 skipped += 1
>                 results.append(FileResult(
>                     source=str(source_path),
>                     status="skipped_no_audio",
>                     source_type=source_type,
>                     error=msg,
>                     elapsed_seconds=round(time.perf_counter() - start_time, 3),
>                 ))
>                 continue
> 
>             extract_or_clean_to_wav(
>                 ffmpeg_bin=ffmpeg_bin,
>                 input_path=source_path,
>                 output_wav=audio_out,
>                 cleanup=cleanup,
>                 filter_chain=filter_chain,
>                 treat_as_audio=(source_type == "audio"),
>             )
>             print(f"  - Audio written: {audio_out}")
> 
>             txt_path_str = None
>             srt_path_str = None
> 
>             if do_stt:
>                 transcribe_audio_with_model(
>                     model=model,
>                     audio_path=audio_out,
>                     txt_path=txt_out,
>                     srt_path=srt_out,
>                 )
>                 txt_path_str = str(txt_out)
>                 srt_path_str = str(srt_out)
>                 print(f"  - Transcript written: {txt_out}")
>                 print(f"  - Subtitles written:  {srt_out}")
> 
>             elapsed = round(time.perf_counter() - start_time, 3)
>             processed += 1
> 
>             results.append(FileResult(
>                 source=str(source_path),
>                 status="ok",
>                 source_type=source_type,
>                 audio_path=str(audio_out),
>                 txt_path=txt_path_str,
>                 srt_path=srt_path_str,
>                 elapsed_seconds=elapsed,
>             ))
> 
>         except Exception as exc:
>             elapsed = round(time.perf_counter() - start_time, 3)
>             errors += 1
>             print(f"  - ERROR: {exc}")
>             results.append(FileResult(
>                 source=str(source_path),
>                 status="error",
>                 source_type=source_type,
>                 error=str(exc),
>                 elapsed_seconds=elapsed,
>             ))
> 
>     manifest_path = out_root / "manifest.json"
>     manifest_path.write_text(
>         json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False),
>         encoding="utf-8",
>     )
> 
>     print("\nDone.")
>     print(f"Processed: {processed}")
>     print(f"Skipped:   {skipped}")
>     print(f"Errors:    {errors}")
>     print(f"Manifest:  {manifest_path}")
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> # What to do now
> 
> Save that as:
> 
> ```text
> video_stt_pipeline.py
> ```
> 
> Then run:
> 
> ```bash
> python video_stt_pipeline.py
> ```
> 
> When it asks:
> 
> ## For your WAV retry folder
> Use:
> 
> - **Pass**: `3` → `medium.en`
> - **Cleanup**:
>   - try `3` = strong
>   - if that overcooks the audio, rerun the bad ones with `1` = none
> 
> ## For a fast first sweep
> Use:
> 
> - **Pass**: `1` → `base.en`
> - **Cleanup**: `2` = light
> 
> ---
> 
> # Important improvement in this version
> 
> Your old script loaded the model **inside every file transcription call**.
> 
> That’s dumb and slow.
> 
> This version loads it **once**:
> 
> ```python
> model = load_whisper_model(...)
> ```
> 
> then reuses it for every file.
> 
> That matters a lot.
> 
> ---
> 
> # Why your redo folder will work now
> 
> Because this script scans for:
> 
> - video files
> - audio files
> 
> including:
> 
> - `.wav`
> - `.mp3`
> - `.m4a`
> - `.flac`
> - etc.
> 
> So a folder full of cleaned retry WAVs is now valid input.
> 
> ---
> 
> # Blunt recommendation
> 
> For the 40 difficult files:
> 
> 1. run `medium.en` + strong cleanup
> 2. review output
> 3. rerun only the still-bad ones with:
>    - `medium.en` + no cleanup
> 4. only use `large-v3` on the true disasters
> 
> That is the sane ladder.
> 
> If this script throws a real error next, paste the traceback and I’ll cut straight to the bad line.
