# GovUAE Dyslexia Service Platform - Project Specifications

## Project Overview
This is a **static HTML documentation portal** for the Dyslexia Service Platform, deployed on Vercel and GitHub Pages. The project contains governance, operational, and technical documentation for a child dyslexia monitoring and intervention system (DIMS).

## Key Specifications

### Language & Localization
- **Primary Language:** English (all new content and updates must be in English)
- **Status:** Portuguese content has been migrated to English
- **Enforcement:** All HTML files must have `lang="en"` attribute

### Technology Stack
- **Type:** Static HTML (no Node.js/build tools required)
- **Hosting:** Vercel (primary), GitHub Pages (secondary)
- **Deployment:** Direct git push to main branch
- **File Format:** HTML5 with embedded CSS and JavaScript

### Project Structure
```
GovUAE/
├── index.html                          (Portal homepage)
├── pages/
│   ├── service-card-dyslexia.html      (Service design canvas)
│   ├── child-monitoring-dyslexia-bpmn-detailed.html (BPMN process diagram)
│   ├── spec-process-dyslexia-monitoring.html (Process spec)
│   ├── as-is-to-be-analysis.html       (Strategic analysis)
│   ├── target-operating-model.html     (Operating model)
│   ├── raci-governance-matrix.html     (Governance matrix)
│   ├── risk-register.html              (Risk assessment)
│   └── technology-stack-mapping.html   (Tech architecture)
├── assets/
│   └── uae-emblem.png                  (UAE government emblem)
├── dist/
│   ├── style.css                       (Built UAE Design System CSS)
│   └── custom.css                      (Portal bridge styles)
├── src/
│   └── style.css                       (Tailwind source CSS)
├── docs/
│   └── uae-design-system-research.md   (UAE DS v3.0 reference)
├── vercel.json                         (Redirects for old URLs)
├── package.json
└── .gitignore
```

### Critical Files & Updates
1. **01-Service-Card-Dyslexia.html**
   - Status: ✅ Translated to English (commit: 56bcc07)
   - Content: Service design with 9-stage monitoring process
   - Last update: 2026-05-06

2. **Child_Monitoring_Dyslexia_BPMN_Detailed.html**
   - Status: Uses draw.io iframe (no Mermaid errors)
   - Contains: Complete 9-stage BPMN 2.0 process
   - Diagram source: DIMS_BPMN_DrawIO.drawio

3. **Portal Index (index.html)**
   - Status: ⚠️ Still shows Portuguese (cached on GitHub Pages)
   - Vercel: Shows updated English version
   - Issue: GitHub Pages serves stale cache despite .nojekyll file

### Known Issues & Solutions
1. **GitHub Pages Cache Problem**
   - Symptom: Old Portuguese version served instead of English
   - Cause: Aggressive CDN caching (600s max-age)
   - Workaround: Use Vercel for primary access (no cache issues)
   - Solution: .nojekyll file added to disable Jekyll processing

2. **Translation Completeness**
   - All Portuguese terms must be replaced with English equivalents
   - Use case-insensitive Perl regex for thorough coverage
   - Verify `lang="en"` attribute in HTML head

### Development Workflow
1. **Before Making Changes:**
   - Ensure all content updates are in English
   - Run git status to check for untracked submodules
   - Clean up worktree/submodule changes before committing

2. **When Updating Files:**
   - Edit HTML directly (no build required)
   - Test on Vercel: https://govuae-dyslexia-service.vercel.app/
   - Use `curl` or browser to verify content
   - Commit with clear message (fix, feat, chore prefix)

3. **After Pushing:**
   - Vercel updates automatically (no caching issues)
   - GitHub Pages may lag (cache) - check Vercel instead
   - Use `curl https://raw.githubusercontent.com/...` to verify remote content

### Content Standards
- **Language:** English only (all headings, descriptions, metadata)
- **HTML Structure:** Semantic HTML5 with lang="en"
- **Styling:** Embedded CSS (no external dependencies)
- **Accessibility:** WCAG 2.1 AA compliance recommended
- **Special Characters:** Escape ampersands as `&amp;` in content

### Git Workflow
```bash
# Check status
git status

# Commit changes
git add <files>
git commit -m "type: description"
git push origin main

# Verify on Vercel (primary check)
curl https://govuae-dyslexia-service.vercel.app/<filename>

# Verify on GitHub raw (secondary check)
curl https://raw.githubusercontent.com/hbuosi/govuae-dyslexia-service/main/<filename>
```

### Useful Commands
```bash
# Check for Portuguese content
grep -r "[áéíóúãõç]" *.html | head -20

# Verify language attribute
grep -o 'lang="[^"]*"' *.html

# Count occurrences of specific word
grep -o "word" file.html | wc -l
```

### Contacts & Resources
- **Repository:** https://github.com/hbuosi/govuae-dyslexia-service
- **Production URL (Vercel only):** https://govuae-dyslexia-service.vercel.app/
- **GitHub Pages:** ❌ DISABLED - Do not use. Use Vercel only.

### BPMN Diagram Standard
- **Tool:** Mermaid.js v10.6.1 (NOT draw.io - draw.io is blocked in some environments)
- **Standard:** BPMN 2.0 (ISO 19510:2013)
- **Colors:**
  - Start Event: `#90EE90` (Light Green) with `#2E7D32` border
  - End Event: `#FFB6B6` (Light Red) with `#C62828` border
  - Tasks/Activities: `#B3D9FF` (Light Blue) with `#1565C0` border
  - Gateways/Decisions: `#FFE082` (Light Yellow/Amber) with `#F57C00` border
