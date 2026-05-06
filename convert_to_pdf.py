#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

# Files to convert
markdown_files = [
    "Child_Monitoring_Service_Card_Dyslexia_ENHANCED.md",
    "AS-IS_TO-BE_Analysis.md",
    "Target_Operating_Model.md",
    "RACI_Governance_Matrix.md",
    "Risk_Register.md",
    "Technology_Stack_Mapping.md",
    "spec-process-dyslexia-monitoring.md"
]

html_files = [
    "Child_Monitoring_Dyslexia_BPMN_Detailed.html"
]

output_dir = "PDF_Output"
os.makedirs(output_dir, exist_ok=True)

# Convert Markdown files to PDF using pandoc
for md_file in markdown_files:
    if os.path.exists(md_file):
        pdf_file = os.path.join(output_dir, md_file.replace('.md', '.pdf'))
        cmd = [
            'pandoc',
            md_file,
            '-f', 'markdown',
            '-t', 'pdf',
            '--pdf-engine=xlatex',
            '-o', pdf_file,
            '-V', 'geometry:margin=1in',
            '-V', 'fontsize=11pt'
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✓ {md_file} → {pdf_file}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to convert {md_file}: {e.stderr.decode()}")
        except Exception as e:
            print(f"✗ Error converting {md_file}: {e}")

# Convert HTML files to PDF using weasyprint
try:
    from weasyprint import HTML
    for html_file in html_files:
        if os.path.exists(html_file):
            pdf_file = os.path.join(output_dir, html_file.replace('.html', '.pdf'))
            try:
                HTML(html_file).write_pdf(pdf_file)
                print(f"✓ {html_file} → {pdf_file}")
            except Exception as e:
                print(f"✗ Error converting {html_file}: {e}")
except ImportError:
    print("WeasyPrint not available, skipping HTML conversion")

print(f"\nPDFs saved to: {output_dir}/")
