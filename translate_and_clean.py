#!/usr/bin/env python3
"""
Translate all HTML and MD files to English and remove all 'Gov' references
"""

import os
import re
import glob
from pathlib import Path
import anthropic

# Initialize Anthropic client
client = anthropic.Anthropic()

def clean_gov_references(text):
    """Remove all references containing 'Gov' or 'gov'"""
    # Remove 'Gov' or 'gov' from words (like GovUAE -> UAE, Government -> ment which we'll clean)
    text = re.sub(r'\bGov[A-Za-z]*\b', '', text)  # GovUAE, Government, etc.
    text = re.sub(r'\bgov[a-z]*\b', '', text)    # lowercase variants
    text = re.sub(r'\bGOV[A-Z]*\b', '', text)    # GOV acronyms

    # Clean up extra spaces created by removals
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+([.,!?;:])', r'\1', text)

    return text.strip()

def translate_to_english(text, file_type="html"):
    """Translate text to English using Claude API"""

    prompt = f"""Translate this {file_type} content to English. Maintain all HTML structure and formatting.
If already in English, return as is. Keep all links, code blocks, and formatting intact.

Content to translate:
{text}"""

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def process_file(file_path):
    """Process a single file: translate and clean"""
    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine file type
    file_ext = Path(file_path).suffix
    file_type = "html" if file_ext == ".html" else "markdown"

    # Check if file is already mostly in English (skip if it is)
    # Just remove Gov references from all files
    content = clean_gov_references(content)

    # Translate if it's not English
    # For now, we'll assume files in Portuguese need translation
    if any(pt_word in content.lower() for pt_word in ['dyslexia', 'service', 'platform', 'analysis']):
        print(f"  Translating {file_path}...")
        content = translate_to_english(content, file_type)

    # Clean again after translation
    content = clean_gov_references(content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Completed: {file_path}")

def main():
    os.chdir("/Users/henriquelopes/Documents/GovUAE/project-english")

    # Get all HTML and MD files (excluding node_modules and .git)
    files_to_process = []

    for pattern in ["*.html", "*.md"]:
        for file_path in glob.glob(pattern):
            if ".git" not in file_path and "node_modules" not in file_path:
                files_to_process.append(file_path)

    # Also get files in subdirectories (like GovUAE_Dyslexia_Service_Documentation/)
    for root, dirs, files in os.walk("."):
        # Skip node_modules and .git
        dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", ".claude"]]

        for file in files:
            if file.endswith((".html", ".md")):
                file_path = os.path.join(root, file)
                if file_path not in files_to_process:
                    files_to_process.append(file_path)

    print(f"\n📚 Found {len(files_to_process)} files to process\n")

    # Process each file
    for i, file_path in enumerate(files_to_process, 1):
        print(f"[{i}/{len(files_to_process)}] ", end="")
        try:
            process_file(file_path)
        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("\n✅ All files processed!")

if __name__ == "__main__":
    main()
