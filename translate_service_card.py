#!/usr/bin/env python3
"""
Translate Service Card from Portuguese to English
"""

import anthropic
import re

def translate_html_content(html_content):
    """Translate HTML content from Portuguese to English"""

    client = anthropic.Anthropic()

    # Extract text portions for translation (excluding HTML tags)
    prompt = """Translate this HTML content from Portuguese to English.
Keep ALL HTML structure, tags, attributes, and CSS intact.
ONLY translate the text content between tags.
Do NOT change any URLs, links, IDs, classes, or styling.

HTML to translate:
""" + html_content

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=8096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def main():
    print("📝 Translating Service Card from Portuguese to English...")

    # Read the HTML file
    with open("01-Service-Card-Dyslexia.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    print("  Translating content (this may take a moment)...")
    translated_html = translate_html_content(html_content)

    # Write back
    with open("01-Service-Card-Dyslexia.html", "w", encoding="utf-8") as f:
        f.write(translated_html)

    print("✅ Service Card translated successfully!")
    print("   File: 01-Service-Card-Dyslexia.html")

if __name__ == "__main__":
    main()
