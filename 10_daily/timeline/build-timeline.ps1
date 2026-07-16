# PowerShell Build Script for Timeline
# Alternative to Node.js version

Write-Host "`n🔨 Building timeline from markdown files...`n" -ForegroundColor Cyan

$eventsDir = Join-Path $PSScriptRoot "events"
$outputFile = Join-Path $PSScriptRoot "timeline.json"

# Check if events directory exists
if (-not (Test-Path $eventsDir)) {
    Write-Host "❌ Error: events/ directory not found!" -ForegroundColor Red
    exit 1
}

# Function to parse front matter
function Parse-FrontMatter {
    param([string]$content)
    
    if ($content -notmatch '(?s)^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$') {
        return $null
    }
    
    $frontMatter = $Matches[1]
    $body = $Matches[2].Trim()
    
    $data = @{}
    $currentKey = $null
    $currentArray = @()
    
    $frontMatter -split "`n" | ForEach-Object {
        $line = $_.Trim()
        if ([string]::IsNullOrWhiteSpace($line)) { return }
        
        # Array items
        if ($line -match '^- (.+)$') {
            if ($currentKey) {
                $currentArray += $Matches[1].Trim()
            }
            return
        }
        
        # Key-value pairs
        if ($line -match '^([^:]+):\s*(.*)$') {
            $key = $Matches[1].Trim()
            $value = $Matches[2].Trim()
            
            if ([string]::IsNullOrWhiteSpace($value)) {
                # Array key
                if ($currentKey -and $currentArray.Count -gt 0) {
                    $data[$currentKey] = $currentArray
                }
                $currentKey = $key
                $currentArray = @()
            } else {
                # Regular key-value
                if ($currentKey -and $currentArray.Count -gt 0) {
                    $data[$currentKey] = $currentArray
                }
                $currentKey = $null
                $currentArray = @()
                
                # Parse boolean
                if ($value -eq 'true') {
                    $data[$key] = $true
                } elseif ($value -eq 'false') {
                    $data[$key] = $false
                } else {
                    $data[$key] = $value
                }
            }
        }
    }
    
    # Add last array if exists
    if ($currentKey -and $currentArray.Count -gt 0) {
        $data[$currentKey] = $currentArray
    }
    
    return @{
        frontMatter = $data
        content = $body
    }
}

# Get all markdown files
$files = Get-ChildItem -Path $eventsDir -Filter "*.md" | Where-Object { $_.Name -notlike "_*" }

Write-Host "📂 Found $($files.Count) markdown file(s)`n" -ForegroundColor Gray

$events = @()
$successCount = 0
$errorCount = 0

# Parse each file
foreach ($file in $files) {
    try {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        $parsed = Parse-FrontMatter -content $content
        
        if ($parsed) {
            $event = @{
                id = $file.BaseName
                date = $parsed.frontMatter.date
                title = $parsed.frontMatter.title
                category = $parsed.frontMatter.category
                critical = if ($parsed.frontMatter.critical) { $true } else { $false }
                tags = if ($parsed.frontMatter.tags) { $parsed.frontMatter.tags } else { @() }
                description = $parsed.content
            }
            
            $events += $event
            Write-Host "  ✓ $($file.Name)" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "  ✗ $($file.Name) - Invalid front matter" -ForegroundColor Yellow
            $errorCount++
        }
    } catch {
        Write-Host "  ✗ $($file.Name) - $($_.Exception.Message)" -ForegroundColor Red
        $errorCount++
    }
}

# Sort events by date (newest first)
$events = $events | Sort-Object { [DateTime]$_.date } -Descending

# Convert to JSON and save
$json = $events | ConvertTo-Json -Depth 10
Set-Content -Path $outputFile -Value $json -Encoding UTF8

Write-Host "`n$('=' * 50)" -ForegroundColor Cyan
Write-Host "✅ Successfully built timeline.json" -ForegroundColor Green
Write-Host "   Total events: $($events.Count)" -ForegroundColor Gray
Write-Host "   Success: $successCount" -ForegroundColor Gray
if ($errorCount -gt 0) {
    Write-Host "   Errors: $errorCount" -ForegroundColor Yellow
}
Write-Host "   Output: $outputFile" -ForegroundColor Gray
Write-Host "$('=' * 50)`n" -ForegroundColor Cyan

# Statistics
$criticalCount = ($events | Where-Object { $_.critical }).Count
$categories = $events | Group-Object category

Write-Host "📊 Statistics:" -ForegroundColor Cyan
Write-Host "   Critical events: $criticalCount" -ForegroundColor Gray
Write-Host "   By category:" -ForegroundColor Gray
$categories | Sort-Object Name | ForEach-Object {
    Write-Host "     - $($_.Name): $($_.Count)" -ForegroundColor Gray
}
Write-Host ""

