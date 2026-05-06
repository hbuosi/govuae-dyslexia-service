#!/usr/bin/env python3
import markdown
import re
from pathlib import Path

# Read the current Service Card HTML file
html_file = Path('01-Service-Card-Dyslexia.html')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract markdown content from the body (between <body> and </body>)
body_match = re.search(r'<body>\n(.*?)\n</body>', content, re.DOTALL)
if body_match:
    markdown_content = body_match.group(1)
else:
    print("Could not extract body content")
    exit(1)

# Convert markdown to HTML
md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'toc', 'extra', 'meta', 'nl2br'])
html_content = md.convert(markdown_content)

# Create complete HTML document with design system
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Card - Dyslexia Monitoring & Intervention System</title>
    <style>
        :root {{
            --color-primary: #0066cc;
            --color-secondary: #0088ff;
            --color-success: #00aa44;
            --color-warning: #ff6600;
            --color-danger: #cc0000;
            --color-dark: #1a1a1a;
            --color-medium: #666666;
            --color-light: #f5f5f5;
            --color-white: #ffffff;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 1rem;
            line-height: 1.7;
            color: var(--color-dark);
            background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
            padding: 20px;
        }}

        /* Navigation */
        .navbar {{
            background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-secondary) 100%);
            color: var(--color-white);
            padding: 16px 24px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            margin: -20px -20px 30px -20px;
            border-radius: 0 0 8px 8px;
        }}

        .navbar-brand {{
            font-weight: 700;
            font-size: 1.3rem;
        }}

        .navbar-links {{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .navbar a {{
            color: var(--color-white);
            text-decoration: none;
            transition: opacity 200ms;
        }}

        .navbar a:hover {{
            opacity: 0.8;
        }}

        /* Breadcrumb */
        .breadcrumb {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 12px 0;
            font-size: 0.9rem;
            color: var(--color-medium);
            margin-bottom: 24px;
        }}

        .breadcrumb a {{
            color: var(--color-primary);
            text-decoration: none;
        }}

        /* Container */
        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        /* Headers */
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 700;
            margin: 28px 0 16px 0;
            color: var(--color-dark);
        }}

        h1 {{
            font-size: 2.5rem;
            border-bottom: 3px solid var(--color-primary);
            padding-bottom: 12px;
            margin-bottom: 20px;
        }}

        h2 {{
            font-size: 1.8rem;
            color: var(--color-primary);
            border-left: 4px solid var(--color-primary);
            padding-left: 12px;
        }}

        h3 {{
            font-size: 1.4rem;
            color: var(--color-secondary);
        }}

        h4 {{
            font-size: 1.2rem;
        }}

        /* Paragraphs */
        p {{
            margin-bottom: 16px;
            line-height: 1.8;
        }}

        /* Links */
        a {{
            color: var(--color-primary);
            text-decoration: none;
            transition: color 200ms;
        }}

        a:hover {{
            color: var(--color-secondary);
            text-decoration: underline;
        }}

        /* Lists */
        ul, ol {{
            margin: 16px 0;
            padding-left: 40px;
        }}

        li {{
            margin-bottom: 8px;
            line-height: 1.8;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}

        thead {{
            background-color: var(--color-primary);
            color: var(--color-white);
        }}

        th {{
            padding: 16px;
            text-align: left;
            font-weight: 600;
        }}

        td {{
            padding: 14px 16px;
            border-bottom: 1px solid var(--color-light);
        }}

        tbody tr:hover {{
            background-color: var(--color-light);
        }}

        /* Code blocks */
        pre {{
            background-color: var(--color-dark);
            color: var(--color-white);
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 20px 0;
            font-size: 0.9rem;
            line-height: 1.5;
        }}

        code {{
            font-family: "Courier New", monospace;
            background-color: var(--color-light);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9rem;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
            color: inherit;
        }}

        /* Blockquotes */
        blockquote {{
            border-left: 4px solid var(--color-primary);
            padding-left: 16px;
            margin: 20px 0;
            color: var(--color-medium);
            font-style: italic;
        }}

        /* Badges */
        .badge {{
            display: inline-block;
            background-color: var(--color-primary);
            color: var(--color-white);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-right: 8px;
        }}

        /* Footer */
        footer {{
            background-color: var(--color-dark);
            color: var(--color-white);
            padding: 24px;
            margin: 40px -20px -20px -20px;
            text-align: center;
            font-size: 0.9rem;
        }}

        footer a {{
            color: var(--color-secondary);
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            body {{
                padding: 12px;
            }}

            h1 {{
                font-size: 2rem;
            }}

            h2 {{
                font-size: 1.5rem;
            }}

            h3 {{
                font-size: 1.2rem;
            }}

            .navbar {{
                margin: -12px -12px 20px -12px;
            }}

            .navbar-links {{
                gap: 12px;
            }}

            table {{
                font-size: 0.9rem;
            }}

            th, td {{
                padding: 12px;
            }}
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="navbar-brand">Dyslexia Service Platform</div>
        <div class="navbar-links">
            <a href="index.html">Home</a>
            <a href="AS-IS_TO-BE_Analysis.html">Strategy</a>
            <a href="RACI_Governance_Matrix.html">Governance</a>
            <a href="Technology_Stack_Mapping.html">Technology</a>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="container">
        <div class="breadcrumb">
            <a href="index.html">Home</a>
            <span>/</span>
            <a href="index.html#operations">Operations</a>
            <span>/</span>
            <span>Service Card</span>
        </div>

        <!-- Main Content -->
        {html_content}
    </div>

    <!-- Footer -->
    <footer>
        <p>Dyslexia Service Platform Documentation</p>
        <p style="font-size: 0.85rem; margin-top: 12px; color: #999;">Generated on 2026-05-06 | Classification: Confidential</p>
    </footer>
</body>
</html>
"""

# Write the properly formatted HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("✅ Service Card properly formatted with HTML conversion!")
