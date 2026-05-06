#!/usr/bin/env python3
"""
Remove all 'Gov' references from HTML and MD files
"""

import os
import re
import glob
from pathlib import Path

def clean_gov_references(text):
    """Remove all references containing 'Gov' or 'gov'"""

    # Remove GovUAE, Government, etc. - preserving meaning
    replacements = {
        r'\bGovUAE\b': 'Dyslexia Service Platform',
        r'\bgovernment\b': 'service',
        r'\bGovernment\b': 'Service',
        r'\bGOVERNMENT\b': 'SERVICE',
        r'\bgov\b': 'service',
        r'\bGov\b': 'Service',
        r'\bGOV\b': 'SERVICE',
        r'\bgovernmental\b': 'organizational',
        r'\bGovernmental\b': 'Organizational',
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Clean any remaining Gov references that might be part of other words
    text = re.sub(r'Gov([A-Z])', r'\1', text)  # GovXYZ -> XYZ

    # Clean up extra spaces
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+([.,!?;:])', r'\1', text)

    return text.strip()

def process_file(file_path):
    """Process a single file to remove Gov references"""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_size = len(content)
        content = clean_gov_references(content)
        new_size = len(content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        reduction = original_size - new_size
        print(f"  ✓ Cleaned ({reduction} bytes removed)")

    except Exception as e:
        print(f"  ✗ Error: {e}")

def main():
    os.chdir("/Users/henriquelopes/Documents/GovUAE/project-english")

    # Get all HTML and MD files
    files_to_process = []

    # Root level files
    for pattern in ["*.html", "*.md"]:
        for file_path in glob.glob(pattern):
            if ".git" not in file_path and "node_modules" not in file_path:
                files_to_process.append(file_path)

    # Files in subdirectories
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", ".claude"]]

        for file in files:
            if file.endswith((".html", ".md")):
                file_path = os.path.join(root, file)
                if file_path not in files_to_process:
                    files_to_process.append(file_path)

    print(f"📚 Found {len(files_to_process)} files to process\n")

    # Process each file
    for i, file_path in enumerate(files_to_process, 1):
        print(f"[{i}/{len(files_to_process)}] ", end="")
        process_file(file_path)

    print("\n✅ All files cleaned!")

if __name__ == "__main__":
    main()
