#!/usr/bin/env python3
"""
Advanced Markdown to HTML converter with professional styling
"""
import markdown
import os
import re
from pathlib import Path
from datetime import datetime

# Configure markdown extensions for better rendering
markdown_extensions = [
    'tables',
    'fenced_code',
    'codehilite',
    'toc',
    'extra',
    'meta',
    'nl2br'
]

markdown_configs = {
    'codehilite': {
        'css_class': 'highlight',
        'linenums': False
    }
}

files_to_convert = {
    'Child_Monitoring_Service_Card_Dyslexia_ENHANCED.md': 'Service Card - Dyslexia Monitoring',
    'AS-IS_TO-BE_Analysis.md': 'AS-IS TO-BE Analysis',
    'Target_Operating_Model.md': 'Target Operating Model',
    'RACI_Governance_Matrix.md': 'RACI Governance Matrix',
    'Risk_Register.md': 'Risk Register',
    'Technology_Stack_Mapping.md': 'Technology Stack Mapping',
    'spec-process-dyslexia-monitoring.md': 'Process Specification'
}

# Professional CSS styling
CSS_STYLE = """
<style>
    :root {
        --primary-color: #0066cc;
        --secondary-color: #0088ff;
        --accent-color: #00aa44;
        --warning-color: #ff6600;
        --danger-color: #cc0000;
        --light-bg: #f5f5f5;
        --border-color: #dddddd;
        --text-color: #333333;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html {
        scroll-behavior: smooth;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.7;
        color: var(--text-color);
        background: #ffffff;
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 20px;
    }

    header {
        border-bottom: 3px solid var(--primary-color);
        padding-bottom: 20px;
        margin-bottom: 40px;
    }

    h1 {
        color: var(--primary-color);
        font-size: 2.5em;
        margin-bottom: 10px;
        border-bottom: 3px solid var(--primary-color);
        padding-bottom: 15px;
    }

    h2 {
        color: var(--secondary-color);
        font-size: 1.8em;
        margin-top: 40px;
        margin-bottom: 15px;
        padding-left: 15px;
        border-left: 4px solid var(--secondary-color);
    }

    h3 {
        color: #0099ff;
        font-size: 1.4em;
        margin-top: 30px;
        margin-bottom: 12px;
        padding-left: 12px;
        border-left: 3px solid #0099ff;
    }

    h4, h5, h6 {
        color: var(--text-color);
        margin-top: 20px;
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
        text-align: justify;
    }

    a {
        color: var(--primary-color);
        text-decoration: none;
        border-bottom: 1px dotted var(--primary-color);
        transition: all 0.3s ease;
    }

    a:hover {
        background-color: var(--light-bg);
        border-bottom: 1px solid var(--primary-color);
    }

    ul, ol {
        margin: 15px 0 15px 30px;
        padding-left: 20px;
    }

    li {
        margin-bottom: 8px;
    }

    li > ul, li > ol {
        margin-top: 8px;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-radius: 4px;
        overflow: hidden;
    }

    th {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 15px;
        text-align: left;
        font-weight: 600;
        border: none;
    }

    td {
        padding: 12px 15px;
        border-bottom: 1px solid var(--border-color);
    }

    tr:hover {
        background-color: var(--light-bg);
    }

    tr:last-child td {
        border-bottom: none;
    }

    code {
        background-color: var(--light-bg);
        color: #c7254e;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Monaco', 'Courier New', monospace;
        font-size: 0.9em;
    }

    pre {
        background: #2d2d2d;
        color: #f8f8f2;
        padding: 15px;
        border-radius: 4px;
        overflow-x: auto;
        margin: 20px 0;
        line-height: 1.4;
        border-left: 4px solid var(--accent-color);
    }

    pre code {
        background: none;
        color: inherit;
        padding: 0;
        border-radius: 0;
    }

    blockquote {
        border-left: 4px solid var(--primary-color);
        margin: 20px 0;
        padding: 15px 20px;
        background-color: var(--light-bg);
        border-radius: 4px;
        font-style: italic;
    }

    .toc {
        background: var(--light-bg);
        border: 2px solid var(--border-color);
        border-radius: 4px;
        padding: 20px;
        margin: 30px 0;
    }

    .toc ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .toc li {
        margin: 5px 0;
    }

    .toc a {
        color: var(--primary-color);
    }

    .toc > ul > li > a {
        font-weight: 600;
        font-size: 1.1em;
    }

    .toc > ul > li > ul > li > a {
        font-size: 0.95em;
    }

    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
        margin: 40px 0;
    }

    .document-meta {
        background: var(--light-bg);
        padding: 15px 20px;
        border-radius: 4px;
        margin-bottom: 30px;
        font-size: 0.95em;
        color: #666;
    }

    .document-meta p {
        margin: 5px 0;
    }

    .highlight-box {
        background: #fff3cd;
        border-left: 4px solid var(--warning-color);
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
    }

    .success-box {
        background: #d4edda;
        border-left: 4px solid var(--accent-color);
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
    }

    .error-box {
        background: #f8d7da;
        border-left: 4px solid var(--danger-color);
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
    }

    .info-box {
        background: #d1ecf1;
        border-left: 4px solid var(--primary-color);
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
    }

    footer {
        border-top: 2px solid var(--border-color);
        padding-top: 20px;
        margin-top: 60px;
        text-align: center;
        color: #999;
        font-size: 0.9em;
    }

    @media print {
        body {
            max-width: 100%;
            padding: 20px;
        }
        
        a {
            border: none;
        }
        
        h1, h2, h3 {
            page-break-after: avoid;
        }
        
        table, pre {
            page-break-inside: avoid;
        }
        
        footer {
            display: none;
        }
    }

    @media (max-width: 768px) {
        body {
            padding: 20px 10px;
        }
        
        h1 {
            font-size: 2em;
        }
        
        h2 {
            font-size: 1.5em;
        }
        
        table {
            font-size: 0.9em;
        }
        
        th, td {
            padding: 10px;
        }
    }
</style>
"""

def generate_table_of_contents(content):
    """Generate a table of contents from markdown headers"""
    headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
    
    if not headers:
        return ""
    
    toc = '<div class="toc">\n<h3>📑 Índice de Conteúdo</h3>\n<ul>\n'
    
    current_level = 0
    for level_marker, title in headers:
        level = len(level_marker)
        
        # Generate anchor ID from title
        anchor_id = re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')
        anchor_id = re.sub(r'-+', '-', anchor_id)
        
        # Adjust indentation
        if level > current_level:
            toc += '<ul>\n' * (level - current_level)
        elif level < current_level:
            toc += '</ul>\n' * (current_level - level)
        
        toc += f'<li><a href="#{anchor_id}">{title}</a></li>\n'
        current_level = level
    
    toc += '</ul>\n' * current_level
    toc += '</div>\n'
    
    return toc

def add_anchor_ids(content):
    """Add IDs to all headers for linking"""
    def replace_header(match):
        level_marker = match.group(1)
        title = match.group(2)
        anchor_id = re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')
        anchor_id = re.sub(r'-+', '-', anchor_id)
        return f'{level_marker} {title} {{#{anchor_id}}}'
    
    return re.sub(r'^(#{1,6})\s+(.+)$', replace_header, content, flags=re.MULTILINE)

def convert_markdown_to_html(md_file, title):
    """Convert markdown file to HTML with professional styling"""
    
    print(f"Converting: {md_file}")
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Add anchor IDs
    md_content = add_anchor_ids(md_content)
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=markdown_extensions, extension_configs=markdown_configs)
    
    # Generate table of contents
    with open(md_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    toc = generate_table_of_contents(original_content)
    
    # Create full HTML document
    output_filename = md_file.replace('.md', '.html')
    
    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="GovUAE - Dyslexia Monitoring Service">
    <meta name="created" content="{datetime.now().isoformat()}">
    <title>{title} - GovUAE</title>
    <meta name="description" content="Dyslexia Monitoring & Intervention Service Documentation">
    
    {CSS_STYLE}
</head>
<body>
    <header>
        <h1>🎯 {title}</h1>
        <p style="color: #666; margin-top: 10px;">GovUAE Dyslexia Service Transformation Initiative</p>
    </header>

    <div class="document-meta">
        <p><strong>Document:</strong> {md_file}</p>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p><strong>Purpose:</strong> Corporate Excellence & Government Modernization</p>
    </div>

    {toc}

    <main>
        {html_content}
    </main>

    <footer>
        <hr>
        <p>Document generated from Markdown | GovUAE Dyslexia Service Platform</p>
        <p>© 2026 Government Excellence Initiative</p>
    </footer>

    <script>
        // Add smooth scrolling to anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }});
        }});

        // Add copy button to code blocks
        document.querySelectorAll('pre').forEach(block => {{
            const button = document.createElement('button');
            button.textContent = 'Copy';
            button.style.cssText = 'position: absolute; top: 5px; right: 5px; padding: 5px 10px; background: #0066cc; color: white; border: none; border-radius: 3px; cursor: pointer; font-size: 0.85em;';
            block.style.position = 'relative';
            block.appendChild(button);
            
            button.addEventListener('click', function() {{
                const text = block.innerText;
                navigator.clipboard.writeText(text).then(() => {{
                    button.textContent = 'Copied!';
                    setTimeout(() => {{ button.textContent = 'Copy'; }}, 2000);
                }});
            }});
        }});
    </script>
</body>
</html>
"""

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    file_size = os.path.getsize(output_filename) / 1024
    print(f"  ✓ {output_filename} ({file_size:.1f} KB)\n")
    
    return output_filename

# Create HTML_Output directory
os.makedirs('HTML_Output', exist_ok=True)

print("="*70)
print("GENERATING PROFESSIONAL HTML DOCUMENTS")
print("="*70)
print()

generated_files = []

for md_file, title in files_to_convert.items():
    if os.path.exists(md_file):
        html_file = convert_markdown_to_html(md_file, title)
        generated_files.append((md_file, html_file))

print("="*70)
print("✓ ALL HTML FILES GENERATED SUCCESSFULLY!")
print("="*70)
print()
print("Summary:")
for md, html in generated_files:
    size = os.path.getsize(html) / 1024
    print(f"  {html} ({size:.1f} KB)")

print()
print(f"Total files: {len(generated_files)}")
print(f"Total size: {sum(os.path.getsize(html) for _, html in generated_files) / 1024:.1f} KB")
print()
print("Location: Current directory (GovUAE)")

