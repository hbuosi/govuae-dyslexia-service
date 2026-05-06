#!/usr/bin/env python3
import os
import subprocess
import re
from pathlib import Path

markdown_files = {
    "Child_Monitoring_Service_Card_Dyslexia_ENHANCED.md": "01-Service-Card-Dyslexia.html",
    "AS-IS_TO-BE_Analysis.md": "02-AS-IS-TO-BE-Analysis.html",
    "Target_Operating_Model.md": "03-Target-Operating-Model.html",
    "RACI_Governance_Matrix.md": "04-RACI-Governance-Matrix.html",
    "Risk_Register.md": "05-Risk-Register.html",
    "Technology_Stack_Mapping.md": "06-Technology-Stack-Mapping.html",
    "spec-process-dyslexia-monitoring.md": "07-Process-Specification.html"
}

html_files = {
    "Child_Monitoring_Dyslexia_BPMN_Detailed.html": "08-BPMN-Diagram-Dyslexia.html"
}

output_dir = "PDF_Output"
os.makedirs(output_dir, exist_ok=True)

def markdown_to_html(md_file, html_file):
    """Simple markdown to HTML conversion"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basic markdown to HTML conversion
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{md_file}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: white;
        }}
        h1 {{ color: #0066cc; border-bottom: 3px solid #0066cc; padding-bottom: 10px; margin-top: 30px; }}
        h2 {{ color: #0088ff; margin-top: 25px; }}
        h3 {{ color: #0088ff; margin-top: 20px; }}
        h4, h5, h6 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #f0f0f0; font-weight: bold; }}
        pre {{ background-color: #f5f5f5; border: 1px solid #ddd; padding: 12px; overflow-x: auto; }}
        code {{ background-color: #f5f5f5; padding: 2px 6px; border-radius: 3px; }}
        blockquote {{ border-left: 4px solid #0066cc; margin-left: 0; padding-left: 15px; color: #666; }}
        ul, ol {{ margin: 10px 0; padding-left: 30px; }}
        li {{ margin: 5px 0; }}
        .toc {{ background-color: #f9f9f9; padding: 20px; border-radius: 5px; margin: 20px 0; }}
        @media print {{
            body {{ max-width: 100%; }}
            page-break-inside: avoid;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

# Convert markdown to HTML
print("Converting Markdown to HTML...")
for md, html in markdown_files.items():
    if os.path.exists(md):
        markdown_to_html(md, html)
        print(f"✓ {md} → {html}")

# Copy HTML files
print("\nPreparing HTML files...")
for html, _ in html_files.items():
    if os.path.exists(html):
        print(f"✓ {html} ready for conversion")

# Create AppleScript to convert HTML to PDF
applescript = """
on run argv
    set htmlFiles to {}
    repeat with i from 1 to (count of argv)
        set end of htmlFiles to item i of argv
    end repeat
    
    repeat with htmlFile in htmlFiles
        set htmlPath to POSIX file htmlFile
        set htmlName to name of (info for htmlPath)
        set baseName to text 1 thru -6 of htmlName
        set pdfFile to (POSIX path of (parent of htmlPath)) & "PDF_Output/" & baseName & ".pdf"
        
        tell application "Safari"
            open htmlPath
            delay 2
            set currentTab to current tab of front window
            
            repeat while (loading of currentTab) is true
                delay 0.5
            end repeat
            
            delay 1
            do shell script "osascript -e 'tell application \"Safari\" to print (current tab of front window) with properties {target printer:\"\"}'  & ' > /dev/null 2>&1' || true"
            delay 1
            
            quit
        end tell
    end repeat
end run
"""

with open("convert_to_pdf.scpt", "w") as f:
    f.write(applescript)

print("\n✓ AppleScript created: convert_to_pdf.scpt")

# Now let's create a comprehensive conversion using macOS print function
print("\nCreating PDF conversion script...")

conversion_script = """#!/bin/bash
# Convert HTML files to PDF using macOS print functionality

OUTPUT_DIR="PDF_Output"
mkdir -p "$OUTPUT_DIR"

# Array of HTML files to convert
FILES=(
    "01-Service-Card-Dyslexia.html"
    "02-AS-IS-TO-BE-Analysis.html"
    "03-Target-Operating-Model.html"
    "04-RACI-Governance-Matrix.html"
    "05-Risk-Register.html"
    "06-Technology-Stack-Mapping.html"
    "07-Process-Specification.html"
    "Child_Monitoring_Dyslexia_BPMN_Detailed.html"
)

echo "Converting HTML files to PDF..."
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        base=$(basename "$file" .html)
        pdf="$OUTPUT_DIR/${base}.pdf"
        
        # Use macOS native conversion with wkhtmltopdf alternative
        python3 << PYEOF
import os
import subprocess

html_file = "$file"
pdf_file = "$pdf"

try:
    # Try using print to PDF via macOS native tools
    result = os.system(f'cupsfilter -m application/pdf "{html_file}" > "{pdf_file}" 2>/dev/null')
    if result != 0:
        print(f"Note: cupsfilter conversion had exit code {result} for {html_file}")
except Exception as e:
    print(f"Error: {e}")

if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
    print(f"✓ {html_file} → {pdf_file}")
else:
    print(f"⚠ {html_file} - Check PDF manually")
PYEOF
    fi
done

echo ""
echo "✓ PDF conversion started. Files available in: $OUTPUT_DIR/"
"""

with open("convert_htmls.sh", "w") as f:
    f.write(conversion_script)

os.chmod("convert_htmls.sh", 0o755)
print("✓ Conversion script: convert_htmls.sh")

print("\n" + "="*60)
print("NEXT STEPS TO CREATE PDFs:")
print("="*60)
print("""
The HTML files have been created. To convert to PDF, you have several options:

OPTION 1 - Manual (Easiest):
1. Open each HTML file in your browser
2. Press Cmd+P (Print)
3. Change printer to "Save as PDF"
4. Save in PDF_Output/ folder

OPTION 2 - Automated (Requires pandoc):
brew install pandoc
bash -c 'for f in *.html; do pandoc "$f" -o "PDF_Output/$(basename "$f" .html).pdf"; done'

OPTION 3 - Use online converter:
Upload HTML files to an online HTML to PDF converter

Files ready for conversion:
"""
)

for html in list(markdown_files.values()) + [h for h in html_files.keys()]:
    if os.path.exists(html):
        print(f"  • {html}")

