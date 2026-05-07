# Dyslexia Service Platform - Documentation Portal

Documentation portal for the Child Dyslexia Monitoring and Intervention Service (DIMS). Built with the [Design System v3.0](https://designsystem.gov.ae/).

**Live:** [govuae-dyslexia-service.vercel.app](https://govuae-dyslexia-service.vercel.app/)

---

## Documents

| Document | Description |
|----------|-------------|
| [Service Card](pages/service-card-dyslexia.html) | Service design canvas with value proposition, stakeholders, KPIs, and 9-stage monitoring process |
| [BPMN Process Diagram](pages/child-monitoring-dyslexia-bpmn-detailed.html) | End-to-end BPMN 2.0 process flow with decision gateways and risk classification |
| [Process Specification](pages/spec-process-dyslexia-monitoring.html) | Detailed process spec with requirements, constraints, and acceptance criteria |
| [AS-IS / TO-BE Analysis](pages/as-is-to-be-analysis.html) | Current-state pain points and future-state transformation vision |
| [Target Operating Model](pages/target-operating-model.html) | Organizational design, governance composition, and capability maturity model |
| [RACI Governance Matrix](pages/raci-governance-matrix.html) | Role-responsibility mapping across 13 process areas and 15 roles |
| [Risk Register](pages/risk-register.html) | 31 identified risks with mitigation strategies and ownership |
| [Technology Stack](pages/technology-stack-mapping.html) | Enterprise architecture with integration patterns and security design |

## Tech Stack

- **Frontend:** Static HTML5 with [Design System v3.0](https://designsystem.gov.ae/) (`@aegov/design-system`)
- **CSS:** TailwindCSS v4 + custom portal styles
- **Icons:** [Phosphor Icons](https://phosphoricons.com/)
- **BPMN Rendering:** Mermaid.js v10.6.1
- **Hosting:** Vercel
- **Standard:** WCAG 2.1 AA accessibility compliance

## Project Structure

```
├── index.html                 Portal homepage
├── pages/                     Documentation pages (kebab-case)
├── assets/                    Images and static assets
├── dist/                      Built CSS (Design System + custom)
├── src/                       Tailwind source CSS
├── docs/                      Reference documentation
├── vercel.json                URL redirects
└── package.json               Build dependencies
```

## Development

### Prerequisites

- Node.js 18+

### Setup

```bash
npm install
```

### Build CSS

```bash
npm run build:css
```

### Watch mode (auto-rebuild on changes)

```bash
npm run watch:css
```

### Local preview

```bash
npx serve .
```

## Design System

This portal follows the [Design System v3.0](https://designsystem.gov.ae/) maintained by TDRA. Key design decisions:

- **Primary color:** AEGold `#92722A` (primary-600)
- **Typography:** Roboto (English), Noto Kufi Arabic (Arabic)
- **Components:** `aegov-card`, `aegov-btn`, `aegov-badge`, `aegov-breadcrumb`
- **Spacing:** 4px base scale with 24px default gaps
- **Layout:** Max 1280px container, 6-column grid system

Full design system reference: [docs/uae-design-system-research.md](docs/uae-design-system-research.md)

## License

Internal documentation - Department X.
