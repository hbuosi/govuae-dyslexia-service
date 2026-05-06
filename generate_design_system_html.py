#!/usr/bin/env python3
import markdown
import os
from datetime import datetime

def generate_html_with_design_system(markdown_file, output_file, title):
    """Generate HTML from markdown with Design System styling"""

    with open(markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    md = markdown.Markdown(
        extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'toc',
            'extra',
            'meta',
            'nl2br'
        ]
    )
    html_content = md.convert(md_content)

    # Design System CSS
    css = """
    :root {
        --color-primary: #0066cc;
        --color-secondary: #0088ff;
        --color-success: #00aa44;
        --color-warning: #ff6600;
        --color-danger: #cc0000;
        --color-dark: #1a1a1a;
        --color-medium: #666666;
        --color-light: #f5f5f5;
        --color-white: #ffffff;

        --spacing-xs: 4px;
        --spacing-sm: 8px;
        --spacing-md: 16px;
        --spacing-lg: 24px;
        --spacing-xl: 32px;

        --radius-sm: 4px;
        --radius-md: 8px;
        --radius-lg: 16px;

        --font-size-h1: 2.5rem;
        --font-size-h2: 1.8rem;
        --font-size-h3: 1.4rem;
        --font-size-body: 1rem;
        --font-size-small: 0.875rem;

        --shadow-sm: 0 2px 8px rgba(0,0,0,0.1);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.15);
        --shadow-lg: 0 8px 24px rgba(0,0,0,0.2);
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
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: var(--font-size-body);
        line-height: 1.6;
        color: var(--color-dark);
        background-color: var(--color-white);
    }

    /* Navigation Bar */
    .navbar {
        background-color: var(--color-primary);
        color: var(--color-white);
        padding: var(--spacing-md) var(--spacing-lg);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: var(--shadow-md);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .navbar a {
        color: var(--color-white);
        text-decoration: none;
        margin: 0 var(--spacing-md);
        transition: opacity 200ms ease-in-out;
    }

    .navbar a:hover {
        opacity: 0.8;
    }

    .navbar-brand {
        font-weight: 700;
        font-size: 1.2rem;
    }

    .navbar-links {
        display: flex;
        align-items: center;
        gap: var(--spacing-lg);
    }

    /* Container */
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: var(--spacing-lg);
    }

    /* Breadcrumb */
    .breadcrumb {
        display: flex;
        align-items: center;
        gap: var(--spacing-sm);
        padding: var(--spacing-md) 0;
        font-size: var(--font-size-small);
        color: var(--color-medium);
        margin-bottom: var(--spacing-lg);
    }

    .breadcrumb a {
        color: var(--color-primary);
        text-decoration: none;
        transition: color 200ms ease-in-out;
    }

    .breadcrumb a:hover {
        color: var(--color-secondary);
        text-decoration: underline;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
        margin-top: var(--spacing-lg);
        margin-bottom: var(--spacing-md);
        color: var(--color-dark);
    }

    h1 {
        font-size: var(--font-size-h1);
        border-bottom: 3px solid var(--color-primary);
        padding-bottom: var(--spacing-md);
        margin-bottom: var(--spacing-lg);
    }

    h2 {
        font-size: var(--font-size-h2);
        margin-top: var(--spacing-xl);
    }

    h3 {
        font-size: var(--font-size-h3);
    }

    /* Paragraphs & Text */
    p {
        margin-bottom: var(--spacing-md);
        line-height: 1.8;
    }

    /* Links */
    a {
        color: var(--color-primary);
        text-decoration: none;
        transition: color 200ms ease-in-out;
        border-bottom: 1px solid transparent;
    }

    a:hover {
        color: var(--color-secondary);
        border-bottom: 1px solid var(--color-primary);
    }

    /* Lists */
    ul, ol {
        margin-left: var(--spacing-lg);
        margin-bottom: var(--spacing-md);
    }

    li {
        margin-bottom: var(--spacing-sm);
        line-height: 1.8;
    }

    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: var(--spacing-lg) 0;
        box-shadow: var(--shadow-sm);
        border-radius: var(--radius-md);
        overflow: hidden;
    }

    thead {
        background-color: var(--color-light);
        font-weight: 600;
    }

    th, td {
        padding: var(--spacing-md);
        text-align: left;
        border-bottom: 1px solid var(--color-light);
    }

    tbody tr:hover {
        background-color: var(--color-light);
    }

    /* Code blocks */
    pre {
        background-color: var(--color-dark);
        color: var(--color-white);
        padding: var(--spacing-lg);
        border-radius: var(--radius-md);
        overflow-x: auto;
        margin: var(--spacing-lg) 0;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    code {
        font-family: "Courier New", monospace;
        background-color: var(--color-light);
        padding: 2px 6px;
        border-radius: var(--radius-sm);
        font-size: 0.9rem;
    }

    pre code {
        background-color: transparent;
        padding: 0;
    }

    /* Blockquotes */
    blockquote {
        border-left: 4px solid var(--color-primary);
        padding-left: var(--spacing-lg);
        margin: var(--spacing-lg) 0;
        color: var(--color-medium);
        font-style: italic;
    }

    /* Cards / Panels */
    .panel {
        background-color: var(--color-white);
        border: 1px solid var(--color-light);
        border-radius: var(--radius-md);
        padding: var(--spacing-lg);
        margin: var(--spacing-lg) 0;
        box-shadow: var(--shadow-sm);
        transition: box-shadow 200ms ease-in-out;
    }

    .panel:hover {
        box-shadow: var(--shadow-md);
    }

    .panel-header {
        font-weight: 600;
        color: var(--color-primary);
        margin-bottom: var(--spacing-md);
        font-size: 1.1rem;
    }

    /* Alerts / Notifications */
    .alert {
        padding: var(--spacing-lg);
        border-radius: var(--radius-md);
        margin: var(--spacing-lg) 0;
        border-left: 4px solid;
        display: flex;
        gap: var(--spacing-md);
    }

    .alert-success {
        background-color: rgba(0, 170, 68, 0.1);
        border-color: var(--color-success);
        color: var(--color-dark);
    }

    .alert-warning {
        background-color: rgba(255, 102, 0, 0.1);
        border-color: var(--color-warning);
        color: var(--color-dark);
    }

    .alert-danger {
        background-color: rgba(204, 0, 0, 0.1);
        border-color: var(--color-danger);
        color: var(--color-dark);
    }

    .alert-info {
        background-color: rgba(0, 102, 204, 0.1);
        border-color: var(--color-primary);
        color: var(--color-dark);
    }

    /* Color Swatches */
    .color-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: var(--spacing-lg);
        margin: var(--spacing-lg) 0;
    }

    .color-swatch {
        border-radius: var(--radius-md);
        padding: var(--spacing-lg);
        text-align: center;
        color: var(--color-white);
        font-weight: 600;
        box-shadow: var(--shadow-sm);
    }

    .color-swatch.primary {
        background-color: var(--color-primary);
    }

    .color-swatch.secondary {
        background-color: var(--color-secondary);
    }

    .color-swatch.success {
        background-color: var(--color-success);
    }

    .color-swatch.warning {
        background-color: var(--color-warning);
    }

    .color-swatch.danger {
        background-color: var(--color-danger);
    }

    /* Badge / Tag */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: var(--font-size-small);
        font-weight: 600;
        margin-right: var(--spacing-sm);
    }

    .badge-primary {
        background-color: var(--color-primary);
        color: var(--color-white);
    }

    .badge-success {
        background-color: var(--color-success);
        color: var(--color-white);
    }

    .badge-warning {
        background-color: var(--color-warning);
        color: var(--color-white);
    }

    .badge-danger {
        background-color: var(--color-danger);
        color: var(--color-white);
    }

    /* Buttons */
    .btn {
        display: inline-block;
        padding: 12px 24px;
        border-radius: var(--radius-sm);
        font-weight: 500;
        border: none;
        cursor: pointer;
        transition: all 200ms ease-in-out;
        text-decoration: none;
        font-size: 1rem;
    }

    .btn-primary {
        background-color: var(--color-primary);
        color: var(--color-white);
    }

    .btn-primary:hover {
        background-color: var(--color-secondary);
    }

    .btn-secondary {
        background-color: var(--color-light);
        color: var(--color-dark);
        border: 1px solid var(--color-medium);
    }

    .btn-secondary:hover {
        background-color: var(--color-medium);
        color: var(--color-white);
    }

    .btn-danger {
        background-color: var(--color-danger);
        color: var(--color-white);
    }

    .btn-danger:hover {
        background-color: #aa0000;
    }

    /* Footer */
    footer {
        background-color: var(--color-dark);
        color: var(--color-white);
        padding: var(--spacing-xl) var(--spacing-lg);
        margin-top: var(--spacing-3xl);
        border-top: 1px solid var(--color-medium);
    }

    footer a {
        color: var(--color-secondary);
    }

    footer p {
        margin-bottom: var(--spacing-sm);
        font-size: var(--font-size-small);
    }

    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: var(--spacing-lg);
    }

    .footer-section h4 {
        color: var(--color-secondary);
        font-size: 1rem;
        margin-bottom: var(--spacing-md);
    }

    /* Sidebar / TOC */
    .sidebar {
        position: sticky;
        top: 80px;
        width: 250px;
        padding: var(--spacing-lg);
        background-color: var(--color-light);
        border-radius: var(--radius-md);
        max-height: calc(100vh - 100px);
        overflow-y: auto;
    }

    .sidebar-title {
        font-weight: 600;
        margin-bottom: var(--spacing-md);
        color: var(--color-primary);
    }

    .sidebar ul {
        list-style: none;
        margin-left: 0;
    }

    .sidebar li {
        margin-bottom: var(--spacing-sm);
    }

    .sidebar a {
        display: block;
        padding: var(--spacing-sm) var(--spacing-md);
        border-radius: var(--radius-sm);
        transition: all 200ms ease-in-out;
    }

    .sidebar a:hover {
        background-color: var(--color-primary);
        color: var(--color-white);
        border-bottom: none;
    }

    /* Layout */
    .main-layout {
        display: grid;
        grid-template-columns: 1fr 250px;
        gap: var(--spacing-xl);
        max-width: 1400px;
        margin: 0 auto;
        padding: var(--spacing-lg);
    }

    .main-content {
        flex: 1;
    }

    /* Responsive */
    @media (max-width: 1024px) {
        .main-layout {
            grid-template-columns: 1fr;
        }

        .sidebar {
            position: static;
            width: 100%;
            max-height: none;
        }
    }

    @media (max-width: 768px) {
        h1 {
            font-size: 2rem;
        }

        h2 {
            font-size: 1.5rem;
        }

        h3 {
            font-size: 1.2rem;
        }

        .container {
            padding: var(--spacing-md);
        }

        .navbar {
            flex-direction: column;
            gap: var(--spacing-md);
            padding: var(--spacing-md);
        }

        .navbar-links {
            width: 100%;
            flex-wrap: wrap;
            justify-content: center;
        }

        table {
            font-size: 0.9rem;
        }

        th, td {
            padding: var(--spacing-sm);
        }

        .color-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 480px) {
        .navbar-links {
            gap: var(--spacing-sm);
        }

        .navbar a {
            margin: 0 var(--spacing-sm);
            font-size: 0.9rem;
        }

        .color-grid {
            grid-template-columns: 1fr;
        }

        .color-swatch {
            padding: var(--spacing-md);
        }
    }
    """

    # HTML template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} - GovUAE Design System</title>
        <style>
            {css}
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar">
            <div class="navbar-brand">🏛️ GovUAE</div>
            <div class="navbar-links">
                <a href="index.html">📑 Index</a>
                <a href="Design_System.html">🎨 Design System</a>
                <a href="AS-IS_TO-BE_Analysis.html">📊 Strategy</a>
                <a href="RACI_Governance_Matrix.html">⚙️ Governance</a>
                <a href="Target_Operating_Model.html">🏗️ Operations</a>
                <a href="Technology_Stack_Mapping.html">💻 Technology</a>
            </div>
        </nav>

        <!-- Breadcrumb -->
        <div class="container">
            <div class="breadcrumb">
                <a href="index.html">Home</a>
                <span>/</span>
                <span>{title}</span>
            </div>
        </div>

        <!-- Main Content -->
        <div class="container">
            {html_content}
        </div>

        <!-- Footer -->
        <footer>
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Documentation</h4>
                    <p><a href="Design_System.html">Design System</a></p>
                    <p><a href="AS-IS_TO-BE_Analysis.html">AS-IS TO-BE Analysis</a></p>
                    <p><a href="RACI_Governance_Matrix.html">RACI Matrix</a></p>
                </div>
                <div class="footer-section">
                    <h4>Governance</h4>
                    <p><a href="Target_Operating_Model.html">Operating Model</a></p>
                    <p><a href="Risk_Register.html">Risk Register</a></p>
                    <p><a href="Technology_Stack_Mapping.html">Technology Stack</a></p>
                </div>
                <div class="footer-section">
                    <h4>About</h4>
                    <p><a href="#">GovUAE Portal</a></p>
                    <p><a href="#">Dyslexia Service</a></p>
                    <p><a href="#">Contact</a></p>
                </div>
            </div>
            <hr style="border: none; border-top: 1px solid var(--color-medium); margin: var(--spacing-lg) 0;">
            <div style="text-align: center; padding: var(--spacing-lg) 0;">
                <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S GMT+4')} | GovUAE Dyslexia Service Documentation</p>
                <p style="font-size: var(--font-size-small); color: var(--color-medium);">Classification: Internal Use | © 2026 Government of UAE</p>
            </div>
        </footer>
    </body>
    </html>
    """

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"✅ Generated: {output_file}")

# Generate Design System HTML
generate_html_with_design_system(
    '/Users/henriquelopes/Documents/GovUAE/Design_System.md',
    '/Users/henriquelopes/Documents/GovUAE/Design_System.html',
    'Design System'
)

print("\n✅ Design System HTML created successfully!")
