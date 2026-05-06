import os
import re
from pathlib import Path

# Get all HTML files
html_files = list(Path('.').glob('*.html'))
print(f"🔍 Verificando {len(html_files)} arquivos HTML...\n")

# Extract all href links
broken_links = {}
valid_files = set(f.name for f in html_files)

for html_file in sorted(html_files):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all href links
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    
    for href in hrefs:
        # Skip external links, anchors, and javascript
        if href.startswith(('http', 'mailto:', 'javascript:', '#')):
            continue
        
        # Check if file exists
        if not Path(href).exists():
            if html_file.name not in broken_links:
                broken_links[html_file.name] = []
            broken_links[html_file.name].append(href)

# Report results
if broken_links:
    print("❌ LINKS QUEBRADOS ENCONTRADOS:\n")
    for file, links in sorted(broken_links.items()):
        print(f"  📄 {file}")
        for link in sorted(set(links)):
            print(f"      → {link}")
        print()
else:
    print("✅ NENHUM LINK QUEBRADO ENCONTRADO!\n")

# Show all valid files for reference
print(f"📚 Arquivos HTML válidos ({len(valid_files)}):")
for f in sorted(valid_files):
    print(f"  ✓ {f}")
