# UAE Government Design System - Complete Specification Reference

> Source: https://designsystem.gov.ae/
> Version: 3.0 (Released February 17, 2026)
> Maintained by: Telecommunication and Digital Government Regulatory Authority (TDRA)
> License: MIT
> GitHub: https://github.com/TDRA-ae/aegov-dls
> Contact: design.system@tdra.gov.ae

---

## Table of Contents

1. [Overview](#1-overview)
2. [Installation & Setup](#2-installation--setup)
3. [Color System](#3-color-system)
4. [Typography](#4-typography)
5. [Layout & Spacing](#5-layout--spacing)
6. [Iconography](#6-iconography)
7. [Imagery & Illustrations](#7-imagery--illustrations)
8. [Components](#8-components)
9. [Blocks](#9-blocks)
10. [Patterns](#10-patterns)
11. [Accessibility](#11-accessibility)
12. [RTL/LTR & Bilingual Support](#12-rtlltr--bilingual-support)
13. [Motion & Animation](#13-motion--animation)
14. [Content Guidelines](#14-content-guidelines)
15. [Mobile Applications](#15-mobile-applications)
16. [Frontend Development](#16-frontend-development)
17. [Technical Coding Standards](#17-technical-coding-standards)
18. [Advanced CSS Practices](#18-advanced-css-practices)
19. [API-First Applications](#19-api-first-applications)
20. [Browser Support](#20-browser-support)
21. [Assessment & Compliance](#21-assessment--compliance)
22. [Resources & Tools](#22-resources--tools)

---

## 1. Overview

The UAE Design System is a framework and validated set of components, blocks, and patterns for Federal Government Entity (FGE) websites. It establishes unified design standards to enhance usability, accessibility, and user experience across all UAE federal digital services.

**Primary Audience:**
- Content specialists and UI designers
- Developers and user researchers
- Digital operations teams within FGEs
- Web development firms conducting compliance assessments

**Core Principles:**
- Inclusivity and Accessibility (WCAG 2.2 compliance)
- Consistency and Reusability
- Modular Design
- Continuous Improvement

**Compliance:** All Federal Government Entities must comply with the design system. Future federal websites and applications must be developed in accordance with these standards.

---

## 2. Installation & Setup

### NPM Packages

| Package | Purpose |
|---------|---------|
| `@aegov/design-system` | HTML/CSS component library (TailwindCSS plugin) |
| `@aegov/design-system-react` | React component library |

### HTML/CSS Installation

```bash
npm i @aegov/design-system
```

Create `/src/style.css`:
```css
@layer base;
@import "tailwindcss";
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";
@plugin "@aegov/design-system";
```

Build command:
```bash
npx @tailwindcss/cli -i ./src/style.css -o ./dist/style.css --watch
```

Link in HTML:
```html
<link href="/dist/style.css" rel="stylesheet">
```

### React Installation

```bash
npm install @aegov/design-system-react
```

Update `tailwind.config.js`:
```javascript
content: [
  './node_modules/@aegov/design-system-react/**/*.{js,jsx,ts,tsx}',
  './src/**/*.{js,jsx,ts,tsx}',
],
```

Import styles in `index.css`:
```css
@import '../node_modules/@aegov/design-system-react/dist/styles/tailwind.css';
```

### Technology Stack

- **CSS Framework:** TailwindCSS v4
- **JavaScript:** Forked from Flowbite's JS library (bundled)
- **Configuration:** CSS-first using `@theme` directive (not `tailwind.config.js`)
- **Build Tools:** Webpack, Babel
- **Languages in repo:** CSS (53%), TypeScript (38.4%), JavaScript (8.6%)

### Tailwind CSS v4 Key Changes

- Single `@import "tailwindcss"` replaces multiple `@tailwind` directives
- CSS-first configuration using `@theme` directive
- Automatic content detection (no manual `content` array)
- `@plugin` directives in CSS replace config-file plugins
- Full rebuilds 3.5x faster, incremental builds 8x faster than v3
- First-party Vite plugin available

---

## 3. Color System

### Core Palette (Primary)

#### AEGold (Primary Brand Color)
Represents strength and UAE identity.

| Token | Hex | Usage |
|-------|-----|-------|
| primary-50 | `#F9F7ED` | Light backgrounds |
| primary-100 | `#F2ECCF` | |
| primary-200 | `#E6D7A2` | |
| primary-300 | `#D7BC6D` | |
| primary-400 | `#CBA344` | |
| primary-500 | `#B68A35` | Hover states |
| primary-600 | `#92722A` | **Primary component color** (accessible) |
| primary-700 | `#7C5E24` | Text on gold backgrounds |
| primary-800 | `#6C4527` | |
| primary-900 | `#5D3B26` | |
| primary-950 | `#361E12` | |

> **Important:** Use `primary-600` (#92722A) for primary components, NOT `primary-500` (#B68A35), due to WCAG accessibility contrast requirements.

#### AERed (Core Accent)

| Token | Hex |
|-------|-----|
| aered-50 | `#FEF2F2` |
| aered-100 | `#FDE4E3` |
| aered-200 | `#FDCDCB` |
| aered-300 | `#FAAAA7` |
| aered-400 | `#F47A75` |
| aered-500 | `#EA4F49` |
| aered-600 | `#D83731` |
| aered-700 | `#B52520` |
| aered-800 | `#95231F` |
| aered-900 | `#7C2320` |
| aered-950 | `#430E0C` |

#### AEGreen (Core Accent)

| Token | Hex |
|-------|-----|
| aegreen-50 | `#F3FAF4` |
| aegreen-100 | `#E4F4E7` |
| aegreen-200 | `#CAE8CF` |
| aegreen-300 | `#A0D5AB` |
| aegreen-400 | `#6FB97F` |
| aegreen-500 | `#4A9D5C` |
| aegreen-600 | `#3F8E50` |
| aegreen-700 | `#2F663C` |
| aegreen-800 | `#2A5133` |
| aegreen-900 | `#24432B` |
| aegreen-950 | `#0F2415` |

#### AEBlack (Layout Element)

| Token | Hex |
|-------|-----|
| aeblack-50 | `#F7F7F7` |
| aeblack-100 | `#E1E3E5` |
| aeblack-200 | `#C3C6CB` |
| aeblack-300 | `#9EA2A9` |
| aeblack-400 | `#797E86` |
| aeblack-500 | `#5F646D` |
| aeblack-600 | `#4B4F58` |
| aeblack-700 | `#3E4046` |
| aeblack-800 | `#232528` |
| aeblack-900 | `#1B1D21` |
| aeblack-950 | `#0E0F12` |

### Supporting Palette (Secondary)

#### Tech Blue
| Token | Hex |
|-------|-----|
| techblue-50 | `#E7F5FF` |
| techblue-950 | `#071C5F` |
(Full range from 50-950)

#### Sea Blue
| Token | Hex |
|-------|-----|
| seablue-50 | `#EFFAFF` |
| seablue-950 | `#04334D` |

#### Camel Yellow
| Token | Hex |
|-------|-----|
| camel-50 | `#FFFBEB` |
| camel-950 | `#441B04` |

#### Desert Orange
| Token | Hex |
|-------|-----|
| desertorange-50 | `#FEF5EE` |
| desertorange-950 | `#3F100B` |

#### Fuchsia
| Token | Hex |
|-------|-----|
| fuchsia-50 | `#FDF4FF` |
| fuchsia-950 | `#4A044E` |

#### Slate
| Token | Hex |
|-------|-----|
| slate-50 | `#F8FAFC` |
| slate-950 | `#020617` |

### Environment / Neutral Colors

| Token | Hex | Usage |
|-------|-----|-------|
| whitely-50 | `#FFFFFF` | Primary white |
| whitely-100 | `#FCFCFC` | Light backgrounds |
| whitely-200 | `#F7F7F7` | Subtle backgrounds |
| whitely-300 | `#F2F2F2` | Borders, dividers |

### Functional / Semantic Color Mapping

| Semantic Use | Token | Palette |
|-------------|-------|---------|
| Info | `alert-info` | Tech Blue |
| Error | `alert-error` | AE Red |
| Success | `alert-success` | AE Green |
| Warning | `alert-warning` | Camel |

### Text Color Assignments

| Context | Token | Hex |
|---------|-------|-----|
| Primary text | `text-aeblack-800` | `#232528` |
| Inverse text | `text-whitely-100` | `#FCFCFC` |
| Text on gold | `text-whitely-50` or `text-primary-700` | `#FFFFFF` or `#7C5E24` |

### Background Assignments

| Context | Token | Hex |
|---------|-------|-----|
| Light background | `bg-whitely-100` | `#FCFCFC` |
| Dark background | `bg-aeblack-900` | `#1B1D21` |
| Primary background | `bg-primary-600` | `#92722A` |
| Primary light bg | `bg-primary-50` | `#F9F7ED` |

### Design Tokens (CSS Variables)

Colors integrate via the `@theme` directive with naming convention:
```css
--color-primary-600
--color-aeblack-800
--color-techblue-500
/* Pattern: --color-[palette]-[shade] */
```

### Custom Brand Color Override

Organizations may override primary/secondary colors while maintaining accessibility:

```css
@theme {
  --color-primary-50: #fef7ee;
  --color-primary-600: #e15701;
  --color-secondary-950: #1a1a1a;
}
```

**Critical rule:** Never mix color swatches or use secondary colors in place of primary colors. Components use specific swatches (e.g., `600` for primary, `500` for hover states).

### Color Guidelines

- **Contrast requirement:** WCAG 2.1 AA minimum 4.5:1 ratio for text
- **Gradients:** Use same tonality (e.g., 950 to 50) or contrasting palettes only
- Do not use color alone to convey meaning

---

## 4. Typography

### Font Families

| Language | Primary Font | Secondary Font |
|----------|-------------|----------------|
| English | **Roboto** (5 weights, 7 sizes) | **Inter** (4 weights, 7 sizes) |
| Arabic | **Noto Kufi Arabic** (5 weights, 7 sizes) | **Alexandria** (4 weights, 7 sizes) |

**Fallback Stack:**
```css
"Roboto", -apple-system, BlinkMacSystemFont, system-ui, 'Ubuntu', 'Fira Sans', sans-serif
```

### Font Weights

#### Heading Weights
| Class | Weight | Value |
|-------|--------|-------|
| `font-extralight` | Extra Light | 200 |
| `font-semibold` | Semi Bold | 600 |
| `font-bold` | Bold | 700 |
| `font-extrabold` | Extra Bold | **800 (default for all headings)** |

#### Body Content Weights
| Class | Weight | Value |
|-------|--------|-------|
| `font-light` | Light | 300 |
| `font-normal` | Normal | **400 (default)** |
| `font-medium` | Medium | 500 |
| `font-semibold` | Semi Bold | 600 |
| `font-bold` | Bold | 700 |

### Type Scale (1.333 Major Third)

#### Heading Sizes

| Level | Class | Size (rem) | Size (px) |
|-------|-------|-----------|-----------|
| H1 Display | `text-display` | 4.75rem | 76px |
| H1 | `text-h1` | 3.875rem | 62px |
| H2 | `text-h2` | 3rem | 48px |
| H3 | `text-h3` | 2.5rem | 40px |
| H4 | `text-h4` | 2rem | 32px |
| H5 | `text-h5` | 1.625rem | 26px |
| H6 | `text-h6` | 1.25rem | 20px |

#### Content/Body Sizes

| Class | Font Size (rem/px) | Line Height (rem/px) |
|-------|-------------------|---------------------|
| `text-3xl` | 1.875rem / 30px | 2.25rem / 36px |
| `text-2xl` | 1.5rem / 24px | 2rem / 32px |
| `text-xl` | 1.25rem / 20px | 1.75rem / 28px |
| `text-lg` | 1.125rem / 18px | 1.75rem / 28px |
| `text-base` | 1rem / 16px | 1.5rem / 24px |
| `text-sm` | 0.875rem / 14px | 1.25rem / 20px |
| `text-xs` | 0.75rem / 12px | 1rem / 16px |

### Text Spacing Standards (WCAG 1.4.12)

| Property | Standard |
|----------|----------|
| Body line height | Minimum 1.5x font size |
| Paragraph margin | 2x base font size |
| Letter spacing | 0.12x font size (when needed) |
| Word spacing | At least 0.16x font size |

### Responsive Typography

| Breakpoint | Heading Behavior | Body Text |
|------------|-----------------|-----------|
| < 1024px | Decrease two steps (h1 renders as h3) | `text-base` (16px) |
| < 1536px | Decrease one step (h1 renders as h2) | `text-base` (16px) |
| >= 1536px | Full size | `text-lg` (18px) |

**Responsive heading pattern example:**
```html
<h2 class="text-h4 md:text-h3 xl:text-h2">Heading Text</h2>
```

### Typography Rules

- Minimum base font: 16px (1rem)
- Recommended line length: 60-100 characters
- Ideal content width: 60% of container
- Left-align body text (English); right-align (Arabic)
- Never justify text
- Never underline non-links
- Never indent paragraphs
- Maximum 5 font weights per page
- Load only necessary weights
- Line height may adjust +/-20% for aesthetics; headings use tighter values (minimum 1rem)

---

## 5. Layout & Spacing

### Breakpoints

| Breakpoint | Min Width | CSS Media Query |
|-----------|-----------|-----------------|
| sm | 640px | `@media (min-width: 640px)` |
| md | 768px | `@media (min-width: 768px)` |
| lg | 1024px | `@media (min-width: 1024px)` |
| xl | 1280px | `@media (min-width: 1280px)` |
| 2xl | 1536px | `@media (min-width: 1536px)` |

### Container Widths & Margins

| Breakpoint | Side Margin | Inner Width |
|-----------|------------|-------------|
| >= 1536px | 28px | 1480px |
| >= 1280px | 20px | 1240px |
| >= 1024px | 22px | 980px |
| >= 768px | 14px | 740px |
| >= 640px | 10px | 100% fluid |
| < 640px | device-based | 100% fluid |

Containers are centered by default with responsive padding.

### Grid System

**Default:** 6-column grid (each column = 16.33% / 1/6th of container)

| Configuration | Column Width |
|--------------|-------------|
| 6-column (default) | 16.33% each |
| 4-column | 25% each |
| 3-column | 33.33% each |
| 12-column | Available for complex layouts |

**Recommended gutter/gap:** 24px on larger screens.

### Spacing Scale

**Tier 1** (up to 16px / 1rem): 2px increments
| Value | Pixels |
|-------|--------|
| 1 | 2px |
| 2 | 4px |
| 3 | 6px |
| 4 | 8px |
| 5 | 10px |
| 6 | 12px |
| 7 | 14px |
| 8 | 16px |

**Tier 2** (16px-48px): 4px increments
| Value | Pixels |
|-------|--------|
| 10 | 20px |
| 12 | 24px |
| 14 | 28px |
| 16 | 32px |
| 18 | 36px |
| 20 | 40px |
| 22 | 44px |
| 24 | 48px |

Proportional ratio: 16px = 2x 8px spacing relationship.

### Design Approach

**Mobile-first methodology:** Unprefixed utilities apply to all screen sizes. Prefixed utilities (e.g., `md:`, `lg:`) take effect at the specified breakpoint and above.

Baseline design at 320px, remaining fluid until 640px breakpoint activation.

---

## 6. Iconography

### Icon Library

**Library:** Phosphor Icons (open-source)
- **Total icons:** 1,512 base icons
- **Total variations:** ~9,072 (across all weight styles)
- **Website:** https://phosphoricons.com

### Icon Styles

Each icon has 5 weight options:
1. Light
2. Regular
3. Bold
4. Filled
5. Duo-tone

### Stroke Width

Default stroke: 2pt (`stroke-width="16"`). Stroke weight must correspond to the font weight of accompanying text.

### Icon Sizes

| Size | Pixels | Use Case |
|------|--------|----------|
| Mini | 20x20 px | Use sparingly |
| Minimum (WCAG) | 24x24 px | Standard minimum per WCAG 2.5.8 |
| With 18px text | 28x28 px | Paired with body text |
| Medium | 40x40 px | Prominent UI elements |
| Large | 56x56 px | Feature callouts |
| Empty states | 80x80 px | Empty state illustrations |

### Icon Colors

Minimum 1:3 contrast ratio. Recommended combinations:
- White on dark backgrounds (`bg-aeblack-900`)
- White on primary color (`bg-primary-600`)
- Primary color on white (`bg-whitely-50`)

### Implementation

**SVG (Recommended):** Direct SVG embedding for optimal performance.

**CDN:**
```html
<link href="https://unpkg.com/@phosphor-icons/web@2.0.3/src/bold/style.css" rel="stylesheet">
```

**React:**
```bash
npm install @phosphor-icons/react
```

### Usage Guidelines

- Center-align icons vertically with accompanying text
- Pair with helper text when clarity is needed
- Avoid overuse to prevent visual overwhelm
- Icons under 100px width should use icons, not illustrations

---

## 7. Imagery & Illustrations

### Photography Principles

1. **Memorable** - Reflect realism for user connection
2. **Human** - Include people for stronger resonance
3. **Future Forward** - Progressive and optimistic outlook

### Photography Rules

- Use minimal, simple backgrounds with subject in focus
- Follow the rule of thirds for single subjects
- Center-weight groups with solid backgrounds
- Natural lighting and balanced exposure (no artificial filters)
- Feature landscapes, cityscapes, UAE elements
- Reflect diversity and equality in people photography

### Supported Aspect Ratios

| Ratio | Shape |
|-------|-------|
| 1:1 | Circle or Square |
| 3:4 | Portrait |
| 3:2 | Standard landscape |
| 16:9 | Widescreen |
| 21:9 | Ultra-wide |

### Text Overlay Requirements

| Image Type | Overlay |
|-----------|---------|
| Solid background | No overlay needed |
| Semi-complicated | 30% black overlay |
| Very bright/crowded | 60% black overlay |

**Rule:** Never use colored overlays besides black.

### Image Technical Specifications

- **Preferred format:** WebP (30% more compression than JPEG without quality loss)
- **Fallback:** JPEG for unsupported browsers
- Use responsive images with `srcset` attribute
- Use `<picture>` element for art direction across breakpoints
- Implement `loading="lazy"` for below-fold images
- Use CDN for image distribution
- Never increase dimensions in code (deteriorates sharpness)

### Illustration Guidelines

- **Less is More** - Simple, easily recognizable styles
- **Geometric** - Use basic geometric shapes
- **Solid Colors** - No gradients, contouring, or soft transitions
- **Hierarchy** - Subject in foreground; supporting objects in background
- **High Contrast** - Strong contrast for emphasis

**80-20 Rule:** If illustrations are primary theme, photography is 20%; if photography dominates, illustrations are 20%.

### AI-Generated Imagery

- Recommended for hero images only
- Avoid images conflicting with values, ethics, or cultural principles
- Reject unrealistic imagery
- Ensure content relevance and accuracy

---

## 8. Components

### 8.1 Accordion

**CSS Classes:**
- `.aegov-accordion` - Container with rotation utility
- `.accordion-item` - Individual section
- `.accordion-title` - Header wrapper
- `.accordion-content` - Body wrapper (toggled with `hidden` class)
- `.accordion-content-body` - Content padding container

**Variants:**
1. Standard (Chevron Down) - `[&_.accordion-active_svg]:rotate-180`
2. Plus Icon - `[&_.accordion-active_svg]:rotate-45`
3. Nested Accordions - Unlimited nesting depth

**Behavior:** `data-accordion="collapse"` attribute. `aria-expanded` toggles state.

**React Props:** `items` (array of {value, title, children, icon?, iconRotateDeg?}), `defaultValue`, `multiple` (boolean), `className`

---

### 8.2 Alert

**Types:**

| Type | Class | Color |
|------|-------|-------|
| Info | `.alert-info` | Tech Blue |
| Error | `.alert-error` | AE Red |
| Success | `.alert-success` | AE Green |
| Warning | `.alert-warning` | Camel |

**Style Variations:**
- Soft (default): `.aegov-alert .alert-{type}`
- Solid: `.aegov-alert .alert-solid .alert-{type}`

**Features:** Icon support, action links, title + list, dismissible (via `data-dismiss-target`).

**React Props:** `variant`, `style` (soft/solid), `showIcon`, `action`, `title`, `onDismiss`

---

### 8.3 Avatar

**Sizes:**

| Class | Dimensions |
|-------|-----------|
| `.avatar-xs` | 24px |
| `.avatar-sm` | 32px |
| `.avatar-base` | 40px (default) |
| `.avatar-lg` | 48px |
| `.avatar-xl` | 56px |
| `.avatar-2xl` | 64px |
| `.avatar-3xl` | 80px |

**Variants:** Square (default), Rounded (`.avatar-rounded`)
**Status:** Online (`bg-aegreen-500`), Offline (`bg-aered-500`)
**Placeholder:** `.no-user` class when no image available.

---

### 8.4 Badge

**Color Variants:**

| Class | Color |
|-------|-------|
| `.badge-info` | Tech Blue |
| `.badge-error` | AE Red |
| `.badge-success` | AE Green |
| `.badge-warning` | Camel |

**Sizes:** `.badge-base` (default), `.badge-lg`
**Styles:** `.badge-soft` (default), `.badge-solid`
**Icons:** `<svg class="badge-icon">` with `aria-hidden="true"`

---

### 8.5 Banner

**Positions:** `.banner-top` (default), `.banner-bottom`

**Variants:**

| Class | Background | Use Case |
|-------|-----------|----------|
| default | Light/white | Standard notifications |
| camel | `bg-camel-600` | Attention-grabbing |
| red | `bg-aered-50` | Government services |
| notice | Slate/primary | Cookie/consent notices |
| dark | `bg-slate-700` | Temporary announcements |

**Key Classes:** `.aegov-banner`, `.banner-content`, `.banner-link`, `.banner-dismiss`, `.banner-notice`

**ARIA Roles:** `role="region"`, `role="status"`, `role="alert"`, or `role="banner"` depending on content type.

---

### 8.6 Blockquote

**Variants:**
- Standard (Soft): `.aegov-quote` with SVG quote icon
- Colored (Solid): `.aegov-quote .quote-colored` with background color (no SVG icon)

**Structure:** `.quote-footer` > `.quote-author` + `.quote-cite`
**Required:** `cite` attribute on `<blockquote>` element.

---

### 8.7 Breadcrumbs

**CSS:** `.aegov-breadcrumb.with-seperator`
**Structure:** `<nav aria-label="Breadcrumb">` > `<ol>` > `<li>`
**Current page:** `<span aria-current="page">` (not a link)
**Separators:** Slash (default) or caret
**Supports:** Schema.org microdata with `itemscope` and `itemprop`

---

### 8.8 Button

**Types:**

| Type | Class | Priority |
|------|-------|----------|
| Solid | `.aegov-btn` | Primary (highest) |
| Outline | `.aegov-btn .btn-outline` | Medium |
| Soft | `.aegov-btn .btn-soft` | Medium |
| Link | `.aegov-btn .btn-link` | Low |

**Sizes:**

| Class | Height | Padding (L/R) |
|-------|--------|---------------|
| `btn-xs` | 32px (2rem) | 1rem |
| `btn-sm` | 40px (2.5rem) | 1.25rem |
| `btn-base` | 48px (3rem) | 1.5rem (default) |
| `btn-lg` | 52px (3.25rem) | 1.75rem |

**Color:** Primary (default), Secondary (`.btn-secondary` - uses aeblack)

**Icon Support:**
- Left icon: SVG before label
- Right icon: SVG after label with `.rtl:-scale-x-100` for RTL
- Icon-only: `.btn-icon` class + `<span class="sr-only">` label

**States:** Hover (CSS), Focus (CSS), Active (CSS), Disabled (`disabled` attribute + `aria-disabled="true"`)

**Responsive:**
```html
<button class="aegov-btn btn-sm lg:btn-base 2xl:btn-lg">
```

**React Props:** `variant` (solid/soft/link/outline), `style` (primary/secondary), `size` (xs/sm/base/lg), `block`, `isIcon`, `disabled`

---

### 8.9 Card

**Base class:** `.aegov-card`

**Variants:**

| Class | Purpose |
|-------|---------|
| `card-bordered` | Adds border |
| `card-glow` | Shadow/glow hover effect |
| `card-sm` | Small size |
| `card-base` | Base size (default) |
| `card-lg` | Large size |
| `card-news` | News/media card |
| `card-service` | Service CTA card |
| `card-creative` | Image-focused card |

**Card Types:**
1. **Media Card** - Image, title (h5), description, action link
2. **News Card (borderless)** - Image, date/category, title, description, link
3. **News Card (bordered)** - With `card-bordered` and `card-glow`
4. **Service Card** - No image, two CTAs, bookmark icon
5. **Creative Card** - Image-dominant with overlay title
6. **Image on Left** - Horizontal layout (responsive stacking)

**Layout Patterns:** Stacked (shared borders), Matrix (grid), With Gaps (individual spacing)

**Border radius:** 1rem (16px) default, 0.75rem on tablets, 0.5rem on mobile
**Inner padding:** 1.5rem (24px) minimum
**Element spacing:** 1.5rem to 2rem

---

### 8.10 Checkbox

**Base class:** `.aegov-check-item`

**Sizes:**

| Class | Box Size | Font |
|-------|----------|------|
| `.check-sm` | 16x16px | 14px |
| `.check-base` | 20x20px | 16px (default) |
| `.check-lg` | 24x24px | 18px |

**Variants:** Basic, With link, With description (`.aegov-check-group`), List element (`.group-list`), Secondary (`.check-secondary`)

**React Props:** `label`, `checked`, `disabled`, `size`, `variant`, `onCheckedChange`, `description`

---

### 8.11 Dropdown

**Trigger:** `data-dropdown-toggle="{id}"`
**Trigger method:** `data-dropdown-trigger="click"` (default) or `"hover"`
**Placement:** `data-dropdown-placement="top|right|bottom|left"`

**Classes:** `.aegov-dropdown`, `.dropdown-body`, `.dropdown-item`, `.dropdown-header`

**Variants:** Basic list, With header & dividers, With icons, Color variants, With form components, Custom UI, Hover trigger

**React Props:** `groups` (array), `side`, `align`, `trigger`

---

### 8.12 File Input

**Classes:** `.aegov-form-control.aegov-file-input-control`, `.file-input-label`

**Variants:**
1. Basic upload button
2. With file summary (uploaded files list)
3. Single image feedback (avatar-style)
4. Drag & drop interface (`.form-control-dropbox`)
5. Default browser UI (with size variants)

**Sizes:** `.control-sm` (40px), `.control-base` (48px), `.control-lg` (56px)

---

### 8.13 Hyperlink

**States:**

| State | Style |
|-------|-------|
| Default | `text-primary-600`, underlined |
| Hover | `text-primary-500`, underlined, 2px thickness |
| Active | `text-primary-700`, underlined |
| Visited | `text-primary-600`, underlined |
| Focus | Ring with lighter primary shade |

**Variants:** Default inline link, Block CTA (`.aegov-link`), Soft button link (`.link-soft`), Button-styled link
**RTL:** Icons use `-scale-x-100` transform
**Required attributes:** `title`, `rel="noopener noreferrer"` (external), `target="_blank"` (new tab)

---

### 8.14 Input

**Base class:** `.aegov-form-control` > `.form-control-input`

**Sizes:**

| Class | Height | Font |
|-------|--------|------|
| `.control-sm` | 40px | 14px |
| `.control-base` | 48px | 16px (default) |
| `.control-lg` | 56px | 18px |

**Types:** text, email, password, search, url, date, datetime-local, month, number, tel, range

**Features:** Prefix (`.control-prefix`), Suffix (`.control-suffix`), Error state (`.control-error`), Helper text, Secondary variant (`.control-secondary`)

**React Props:** `label`, `placeholder`, `id`, `type`, `size`, `variant`, `disabled`, `required`, `error`, `helperText`, `prefix`, `suffix`

---

### 8.15 Modal

**Base class:** `.aegov-modal`

**Sizes:**
- Small: `sm:max-w-sm`
- Medium: `sm:max-w-xl` (default)
- Large: `sm:max-w-2xl`
- Extra Large: `sm:max-w-4xl`

**Variants:**
1. Simple Modal
2. Language Selection
3. Gold Star Rating
4. Customer Pulse (feedback)
5. Single/Multiple Action Modals
6. Alert Modals (scrollable, checkbox)
7. Serious Modal (`.modal-serious` - red, destructive actions)

**Behavior:**
- Open: `data-modal-target="{id}"` + `data-modal-toggle="{id}"`
- Close: Backdrop click, ESC key, `data-modal-hide="{id}"`
- Static backdrop: `data-modal-backdrop="static"`
- Placement: `data-modal-placement="{top|center|bottom}-{left|center|right}"`

**Accessibility:** `role="dialog"`, `aria-labelledby`, `aria-hidden="true"` (closed), `tabindex="-1"`, focus trap, ESC key close.

---

### 8.16 Navigation

**Base class:** `.main-navigation`

**Variants:**
1. Basic Navigation (horizontal links)
2. Navigation with Dropdown (hover on desktop, accordion on mobile)
3. Multi-Column Dropdown (category headings)
4. Mega Menu (`.grid-cols-4`, customizable columns)

**Responsive:**
- Desktop (lg+): Horizontal, hover dropdowns
- Mobile: Hamburger menu, full-screen modal, accordion submenus

**Key classes:** `.menu.nav-menu`, `.menu-item`, `.menu-item-has-children`, `.active-page`, `.submenu-btn`

**Keyboard:** Arrow keys navigate menu items. Space/Enter opens/closes mega menus. Focus moves to first focusable element on open.

---

### 8.17 Pagination

**Classes:**
- `.aegov-pagination` - Wrapper
- `.aegov-pagination-previous` / `.aegov-pagination-next`
- `.aegov-pagination-page` - Page number
- `.aegov-pagination-current` - Active page (`aria-current="page"`)
- `.aegov-pagination-extend` - Ellipsis
- `.aegov-pagination-first` / `.aegov-pagination-last`

**Responsive:** Mobile shows simplified "Page X of Y" view.
**RTL:** `rtl:rotate-180` on arrow icons.

---

### 8.18 Popover

**Trigger:** `data-popover-target="{id}"`
**Class:** `.aegov-popover`
**Structure:** `.popover-header` + `.popover-body` + `data-popper-arrow`
**Behavior:** Click to open, click outside or ESC to close, focus management.

---

### 8.19 Radio

**Base class:** `.aegov-check-item` (same wrapper as checkbox)
**Sizes:** `.check-sm` (16px), `.check-base` (20px default), `.check-lg` (24px)
**Variants:** Basic, With description (`.aegov-check-group`), List element (`.group-list`), Secondary (`.check-secondary`)

**React:** `<Radio>` with `<RadioItem>` children. Props: `defaultValue`, `disabled`, `required`, `size`, `variant`, `orientation`

---

### 8.20 Range Slider

**Structure:** `.aegov-form-control` > `<input type="range">` + `<output>`
**Attributes:** `min`, `max`, `value`, `oninput`
**Variants:** Primary (default), Secondary (`.control-secondary`)

---

### 8.21 Select

**Structure:** `.aegov-form-control` > `.form-control-input` > `<select>`
**Sizes:** `.control-sm` (40px), `.control-base` (48px), `.control-lg` (56px)
**Variants:** Primary (default, gold accent), Secondary (`.control-secondary`)
**Multi-select:** Add `multiple` attribute
**Error state:** `.control-error` + `aria-invalid="true"` + `aria-describedby`

---

### 8.22 Slider (Carousel)

**Dependency:** Requires slider library (Slick Slider with jQuery or Embla Carousel)
**Base class:** `.aegovs-slider-style`

**Variants:**
1. Logo Slider - 4 slides, autoplay, dots
2. Initiatives Slider - 4/3/2/1 responsive slides
3. News Slider - 3/3/2/1 responsive slides

**Rules:**
- Minimum 7-second auto-scroll timer
- Always support touch gestures
- Provide manual pagination
- Maximum one auto-scrolling slider per page

---

### 8.23 Steps (Stepper)

**State Classes:**
- `.step-completed` - Finished
- `.step-current` - Active (`aria-current="step"`)
- `.step-upcoming` - Future
- `.step-disabled` - Unavailable

**Sizes:** `.step-sm` (32px), `.step-base` (40px default), `.step-lg` (48px)
**Layout:** `.step-connector` (horizontal), `.step-connector-vertical`, `.step-text-below`

**React Props:** `steps`, `currentStep`, `size`, `orientation` (horizontal/vertical), `showLabels`

---

### 8.24 Tabs

**Base class:** `.aegov-tab`
**Structure:** `<ul class="tab-items" data-tabs-toggle="{id}" role="tablist">` > `<li role="presentation">` > `<a role="tab">`

**Variants:**
1. Default tabs
2. Compact (`.tab-sm`)
3. With icons (SVG before label)
4. Pills (`.tab-pills` + `.tab-link`)

**Responsive:** `max-xl:overflow-auto` for horizontal scrolling on small screens.
**Spacing:** `gap-4 md:gap-6 lg:gap-7 xl:gap-8`

---

### 8.25 Textarea

**Structure:** `.aegov-form-control` > `.form-control-input` > `<textarea>`
**Sizes:** `.control-sm` (96px/14px), `.control-base` (120px/16px), `.control-lg` (128px/18px)
**Variants:** Primary (default), Secondary (`.control-secondary`)
**Error:** `.control-error` with `<p class="error-message">`
**Default rows:** 4

---

### 8.26 Toast

**Base class:** `.aegov-toast`
**Structure:** `.toast-icon` + `.toast-body` + `.toast-dismiss`
**Dismiss:** `data-dismiss-target="#{id}"`
**ARIA:** `role="alert"` on container
**Features:** Optional icon, title, description, action button, close button.

---

### 8.27 Toggle (Switch)

**Base class:** `.aegov-toggle`
**Structure:** `<label class="aegov-toggle">` > `<input type="checkbox" class="sr-only peer" role="switch">` > `.toggle-item`

**Variants:**
- Default
- Success (`.toggle-success` - green)
- Mode (`.toggle-mode` - dark/light)
- Secondary (`.toggle-secondary` - black)
- With icons (`.toggle-icon`)

---

### 8.28 Tooltip

**Trigger:** `data-tooltip-target="{id}"`
**Class:** `.aegov-tooltip`
**Trigger types:** `data-tooltip-trigger="hover"` (default) or `"click"`
**Placement:** `data-tooltip-placement="top|right|bottom|left"` (default: top, auto-fallback to bottom)
**Animation:** `transition-opacity` + `duration-{x}`

---

## 9. Blocks

### 9.1 Header

**Structure:**
- Logo (SVG only, max height 110px)
- Primary navigation (max 7 items)
- Secondary navigation (Login, Accessibility, Language icons with tooltips)

**Required Navigation Order:**
1. Homepage link
2. Service catalogue with dropdown
3. (Entity-specific items)
4. Digital participation
5. Open data
6. About
7. Optional "More" menu

**Variants:**
- **Ministry Header** - Search always visible in top section
- **Authority Header** - UAE emblem positioned right, search in secondary nav icon

**Responsive:** Horizontal on lg+, hamburger menu below lg.

---

### 9.2 Footer

**Required Sections:**

**Top Section (`footer-top`):**
- 4 navigation categories (accordion on mobile, 4-column grid on desktop)
  - The Ministry
  - Using the Website
  - Information and Support
  - References
- Contact information (Tawasul logo, "171" hotline)

**Bottom Section (`footer-bottom`):**
- Copyright: (c) [year] [entity name]. All rights reserved.
- Social media: Facebook, Instagram, LinkedIn, Twitter, YouTube
- Last updated timestamp

**Customization:** Limited to link selection, entity details, and custom color swatches.

---

### 9.3 Hero

**Constraints:**
- Maximum height: 500px on desktop
- Maximum slides: 4
- Landscape images on desktop, portrait on mobile (<640px)
- Minimum auto-scroll timer: 7 seconds

**Variants:**
1. **Full Width** - Image spans viewport
2. **Hero Split** - 50/50 text-to-image
3. **Hero Static** - Non-animated with card grid

**Content Types:**
- Type 1: Solid background + right-side creative
- Type 2: Full-creative slide (text within image)

**Slider Libraries:** Slick Slider (jQuery) or Embla Carousel (dependency-free)

---

### 9.4 Content Block

**Types:**
- Text-based with sidebar navigation (60% content width)
- Full-screen two-column auto-divided (`columns-1 lg:columns-2 gap-10`)
- Image-left layout (`grid-cols-1 lg:grid-cols-2`)
- Image-right with mobile stack (`lg:order-last`)
- Left-aligned CTA
- Center-aligned CTA (`text-center`, `max-w-2xl`)

---

### 9.5 Filter Block

**Layout:** Sidebar filter panel (280px) + content area (desktop), stacked (mobile)
**Components:** Search input, checkboxes (multi-select), radio buttons (single-select), select dropdown, range slider
**Features:** Expandable "See more" links, bordered/borderless variants

---

### 9.6 Newsletter Block

**Variants:**
1. Full width with input form (dark background `bg-aeblack-800`)
2. Sidebar variation (compact)
3. Button-only variants (subscribe link instead of form)

**Elements:** Email input + send icon button, decorative paper plane SVGs.

---

### 9.7 Page Rating

**Required on:** Service card pages, news articles, press releases, events, blog articles.

**Structure:** "Did you find this content useful?" with Yes (thumbs-up) and No (thumbs-down) buttons.

**Variants:** Without background, With background (`primary-50`).

---

### 9.8 Team Block

**Layouts:** 4-column grid, 3-column grid
**Card structure:** Image (rounded-xl, aspect-square, object-cover) + name + title (centered)
**Requirements:** Consistent backgrounds, front-facing photos, full name + mandatory designation.

---

### 9.9 Login Block

**Primary:** UAE Pass (mandatory for all government entities)
**Secondary:** Username/password (requires approval, must include deprecation warning)
**Layout:** Centered container (max 26rem), entity logo, UAE Pass button, account creation link
**Minimum height:** 32rem (xl: 35rem)

---

## 10. Patterns

### 10.1 Address Pattern

**Domestic (UAE):**
1. Emirate (dropdown, 7 emirates)
2. City (auto-loads on emirate selection)
3. Area (auto-loads on city selection)
4. Apartment/Villa Number
5. Building/Community Name
6. Street Address
7. P.O. Box (optional)
8. Additional Landmarks (optional)
9. Makani (optional, for supported emirates)

**International:**
1. Address Details
2. P.O. Box / ZIP Code
3. City
4. State
5. Country (dropdown)
6. Additional Landmarks (optional)

**Rule:** Fields causing form changes flow downward. Use select boxes for standardized locations.

---

### 10.2 Name Pattern

**Primary (recommended):** First name (mandatory) + Middle name (optional) + Last name (mandatory)
**Secondary:** First name + middle name combined + Last name

**Display conventions:**
- Formal: "Dear Mr. Abdullah Al Shamsi"
- Third-person: First and last name
- Informal/Dashboard: First name only ("Hello, Abdulla")

---

### 10.3 Contact Number Pattern

**Format:** `+971 551234567` (country code + space + number)
**Advanced:** `+971 55 1234567` (with area code separation)

**Rules:**
- Default country code based on user location/profile
- Never allow empty country dropdown
- Verify numbers when added
- Allow multiple contact types with labels

---

### 10.4 Date Pattern

**Official format:** DMY (Day-Month-Year)
- Numeric: `28/09/2023`
- Human-readable: `28th Sep, 2023`
- ISO 8601 (technical): `YYYY-MM-DD hh:mm:ss TZ`

---

### 10.5 Emirates ID Pattern

**Format:** `784-1945-1234567-0` (14 characters with dashes)
**Input:** System applies formatting automatically (user enters numbers only)
**Display:** Masked by default: `784-1945-XXXXXXX-X`
**Security:** Encrypt and secure the data entry method

---

### 10.6 Currency Symbol Pattern

**AED Symbol (introduced March 27, 2025):**
- Primary colors: Black or white only
- Brand colors permitted only in marketing contexts
- Position directly before numerical values
- Match symbol font, size, and weight to price digits
- Always display left of numerical value
- No stylization, superscript, or subscript
- Cannot replace the written word "Dirhams"
- Cannot be used as a logo or branding element

---

## 11. Accessibility

### Compliance Level

**Standard:** WCAG 2.1 AA (with future alignment to WCAG 2.2)
**All components:** Tested for WCAG 2.2 guidelines

### Contrast Requirements

- Minimum 4.5:1 ratio for text
- Primary component color uses `#92722A` (primary-600) specifically for contrast compliance

### Keyboard Navigation

- Entire website must be navigable with keyboard only
- All clickable/actionable elements require visible focus states
- Tab key for navigation
- Enter/Space for activation
- Arrow keys for menu navigation
- ESC for closing modals/dropdowns

### Screen Reader Support

- Apple: VoiceOver (pre-installed)
- Windows: Narrator (pre-installed)
- Android: TalkBack (pre-installed)
- Tested with: JAWS, NVDA, Narrator

### ARIA Requirements

- `aria-labelledby` - Reference clickable action elements
- `aria-label` - Descriptive labels for interactive elements
- `aria-expanded` - Accordion/dropdown states
- `aria-current` - Navigation and pagination
- `aria-live` - Status updates
- `aria-selected`, `aria-pressed` - Interactive elements
- `aria-describedby` - Form controls and descriptions

### Focus Management

- Browser default zoom at 175% during development
- No overlapping sections
- Focus ring visible on all interactive elements
- Focus trap in modals
- Focus returns to trigger on modal close

### Media Accessibility

- **Video:** Subtitles/captions in WebVTT format (not burned in)
- **Images:** Descriptive alt text
- **Audio:** Transcripts with contextual sounds

### Minimum Sizes

- Icons: 24px minimum (WCAG 2.5.8)
- Touch targets: 44x44px minimum

### Required Pages

- Accessibility policy page explaining native OS features

### Performance Targets (Lighthouse)

| Metric | Target |
|--------|--------|
| Accessibility score | >= 90 |
| SEO score | >= 90 |
| Performance score | >= 90 |
| Best Practices | >= 80 (prefer >= 90) |
| LCP | <= 2.5 seconds |
| FCP | <= 1.8 seconds |
| TTI | <= 5 seconds |

---

## 12. RTL/LTR & Bilingual Support

### HTML Configuration

```html
<!-- English -->
<html lang="en" dir="ltr">

<!-- Arabic -->
<html lang="ar" dir="rtl">
```

### CSS Logical Properties

Use logical properties that adapt automatically based on text direction:
```css
/* Instead of padding-left/right */
padding-inline-start: 1rem;
margin-inline-end: 1rem;
```

### Tailwind RTL Utilities

- `rtl:-scale-x-100` - Flip icons/arrows for RTL
- `rtl:` prefix for RTL-specific styles
- `ltr:` prefix for LTR-specific styles

### Font Families

| Direction | Primary | Secondary |
|-----------|---------|-----------|
| LTR (English) | Roboto | Inter |
| RTL (Arabic) | Noto Kufi Arabic | Alexandria |

In Tailwind classes:
- English: `font-roboto` or `font-inter`
- Arabic: `font-noto` (Noto Kufi Arabic) or `font-alexandria`

### Navigation RTL Pattern

- English: `[Back] [Title] [Notifications] [Avatar]`
- Arabic: `[Avatar] [Notifications] [Title] [Back]`

### Text Alignment

- English: Left-align body text
- Arabic: Right-align body text
- Never justify text in either direction

### Implementation

All components in the UAE Design System support RTL and have been designed to work for languages that require RTL layout. The framework requires coding frontend to comply with browser and OS features rather than relying on plugins.

### Requirements

- Mirrored layouts for RTL users
- Fonts supporting both Latin and Arabic glyphs
- Proper alignment in both directions
- All components tested for RTL compatibility

---

## 13. Motion & Animation

### General Principles

- Use subtle animations for visual feedback without distraction (micro-interactions)
- Slide transitions in hero sections should be gradual to preserve search engine performance metrics
- Maintain minimum 7-second timer before auto-shifting sliders

### Tooltip Animation

```html
class="transition-opacity duration-{x}"
```

### Accordion Animation

- SVG icon rotation on expand: `rotate-180` (chevron) or `rotate-45` (plus)
- Content reveal via toggling `hidden` class

### Card Hover Effects

- `.card-glow` class adds shadow/glow on hover
- Only apply glow to media cards with clickable content

### Button States

- Hover, focus, and active states are CSS-managed
- No explicit duration specifications beyond Tailwind defaults

### Modal Transitions

- JavaScript-driven visibility toggle
- Backdrop darkens/blurs background

### Newsletter Block

- Optional decorative paper plane animations

> Note: The design system does not publish a comprehensive motion/animation specification with specific easing curves, duration values, or transition timing functions. Animations are primarily handled through Tailwind CSS utilities and component-level JavaScript.

---

## 14. Content Guidelines

### Voice & Tone

**Core voice:** Corporate yet approachable

| Characteristic | Meaning |
|---------------|---------|
| Professional | Facts-focused |
| Accessible | All cultures/ages |
| User-centric | Speaks user language |
| Clear | Simple, logical |
| Confident | Trustworthy |

### Writing Rules

- Use sentence case exclusively (not Title Case or ALL CAPS)
- Use first-person pronouns ("we", "you")
- Eliminate jargon; employ plain language
- No witty, sarcastic, or overly playful content
- Spell out acronyms at first mention
- Minimize contractions (cannot vs. can't)
- Spell out numbers at start of sentences; numerals mid-sentence
- Apply commas to numbers > 999

### English Variant

**British English (Oxford Dictionary):**
- "Defence" not "Defense"
- "Licence" not "License"
- "Mobile phone" not "Cell phone"

### Punctuation

| Mark | Rule |
|------|------|
| Oxford comma | Yes, use in lists |
| Commas | Outside quotation marks (unless part of original) |
| Hyphens | Unspaced for compounds (all-round) |
| Em dashes | For elaboration or parenthetical |
| Ampersands | Use "and" unless brand name |
| Exclamation points | Minimal use |
| Single quotes | Direct speech; double within |

### Navigation Terminology

| Formal | Semi-formal | Informal |
|--------|-------------|----------|
| Services | Our services | What we do |
| Contact | Contact us | Get in touch |
| Frequently asked questions | FAQs | Need more info? |

**Rule:** Ministry websites must avoid informal navigation terms.

### Formatting

- **Bold:** Headlines, menu items, buttons only (sparingly in paragraphs)
- **Italics:** Emphasis, citations, UI elements (avoid combining with hyperlinks)

### Accessibility in Content

- Screen readers require sentence case
- Avoid Unicode characters (misread by assistive technology)
- Use descriptive alt text
- Provide transcripts for audio, captions for video
- Avoid visually-dependent language ("watch video" instead of "play video")

---

## 15. Mobile Applications

### Core Principles

1. User-Centric design
2. Simplicity (clear language, intuitive icons)
3. Accessibility (WCAG compliance)
4. Consistency across all government apps
5. Security (UAE Pass, data privacy)
6. Performance optimization

### Authentication

- **Primary:** UAE Pass (mandatory)
- **Secondary (with approval):** Biometric, PIN/Passcode
- **Onboarding:** Minimum 3-step registration guidance

### Navigation Patterns

**Bottom Fixed Navigation:**
- 3-5 key sections with icons and text labels
- "More" menu as final element

**Title/Header Bar:**
- English: `[Back] [Title] [Notifications] [Avatar]`
- Arabic: `[Avatar] [Notifications] [Title] [Back]`

### Design Trends

- Flat UI / Soft UI
- Dark mode support (system-level detection + user override)
- Micro-interactions for feedback
- Minimalism with effective whitespace

### Offline Functionality

- Cache non-authenticated content
- Clear connection notifications
- Auto-resume on reconnection
- No blank screens or generic errors

### Splash Screens & Onboarding

- Minimize splash screen duration
- Maximum 4 onboarding screens
- Show onboarding only to first-time users

### Customer Feedback

- Customer Pulse surveys mandatory after service completion

---

## 16. Frontend Development

### Core Pillars

1. Performance-first development
2. Progressive enhancement
3. Component-based architecture
4. Accessibility-first thinking

### Recommended Technologies

| Category | Tools |
|----------|-------|
| Frameworks | React, Vue.js |
| Type system | TypeScript (suggested) |
| Build tools | Webpack or Vite |
| Monitoring | Lighthouse, Chrome DevTools |

### Performance Targets

| Metric | Target |
|--------|--------|
| LCP | <= 2.5 seconds |
| FCP | <= 1.8 seconds |
| TTI | <= 5 seconds |

### Best Practices

- Route-based code-splitting (e.g., React.lazy)
- Lazy load images below fold (`loading="lazy"`)
- Modern formats (WebP, AVIF)
- Responsive images with `srcset`
- Audit bundle sizes regularly
- Remove unused dependencies
- Gzip/Brotli compression
- CDN for asset distribution

### Component Architecture

- Separate smart (logic) from presentational (display) components
- Atomic design principles
- Component isolation with well-defined props
- Document usage and patterns

### Prohibitions

- Do not block users on older browsers/devices
- Do not merge data fetching, state, and DOM markup in single files
- Do not load uncompressed large assets above the fold
- Do not rely on visual cues alone for critical information

---

## 17. Technical Coding Standards

### Code Quality

- Meaningful naming for variables, functions, components
- DRY (Don't Repeat Yourself) principle
- Single-responsibility functions
- Intentional commenting for context
- Automated formatting (Prettier, ESLint)
- Separation of concerns in file organization

### Component Rules

- Reference base design system components
- Extend rather than override styles
- Apply native accessibility attributes (ARIA)
- Avoid hardcoding layout values or colors
- Do not introduce conflicting third-party components

### Browser Support

- Chrome (current + previous)
- Safari iOS/macOS (latest two)
- Chromium-based Edge
- Firefox (current + previous)
- Graceful degradation for older browsers (IE11 basic support)

### Keyboard & Touch

- All interactive elements reachable via Tab
- Visible, distinguishable focus states
- 44x44px minimum touch targets
- Avoid hover-only interactions

### Multilingual HTML

```html
<html lang="en">         <!-- English -->
<html lang="ar" dir="rtl"> <!-- Arabic -->
```

---

## 18. Advanced CSS Practices

### Feature Detection

```css
@supports (display: grid) {
  /* Grid layout */
}
```

### Screen Reader Accessibility

`.sr-only` technique hides content visually while exposing to assistive technology.

### Logical Properties for RTL

```css
padding-inline-start: 1rem;
margin-inline-end: 1rem;
/* These adapt automatically based on text direction */
```

### Input Modality Detection

```css
@media (hover: hover) and (pointer: fine) {
  /* Mouse/trackpad users */
}
```

### Orientation-Aware Styling

```css
@media (orientation: portrait) { /* Portrait layouts */ }
@media (orientation: landscape) { /* Landscape layouts */ }
```

### Conditional Display

Media queries for print vs. screen, high-contrast preferences, and resolution.

### Framework

Pairs TailwindCSS utility-first approach with vanilla CSS where needed.

---

## 19. API-First Applications

### Core Principles

1. **Separation of concerns** - Decouple frontends from APIs (React, Vue, Svelte)
2. **Design system compliance** - Use approved component libraries
3. **Secure APIs** - OAuth2, tokens, strict CORS; never expose credentials in frontend
4. **Schema-driven** - OpenAPI, JSON Schema, or GraphQL SDL
5. **Future extensibility** - Reusable, framework-agnostic components

### State Management

- Centralize API interaction in dedicated service modules
- Use Redux (React) or Pinia (Vue) for state management

### Resources

- [UAE Government API Guidelines (PDF)](https://u.ae/-/media/APIFirst/UAE-Government-API-Guidelines-First-Version.pdf)
- [API First Policy](https://uaelegislation.gov.ae/en/policy/details/api-first-policy)
- [TDRA Academy: API First Course](https://academy.tdra.gov.ae/course?course_id=270)

---

## 20. Browser Support

### Browserslist Configuration

```json
{
  "browserslist": [
    "defaults and supports es6-module",
    "iOS >= 12",
    "Android >= 8",
    "last 2 years",
    "> 0.5%",
    "not dead"
  ]
}
```

**Coverage:** ~95.3% in the UAE

### Supported Browsers

- Chrome (current + previous)
- Firefox (current + previous)
- Edge (Chromium-based)
- Safari iOS/macOS (latest two versions)

### Excluded

- Internet Explorer (all versions)
- Dead/unmaintained browsers
- Unsupported forks

### Modern CSS Features Used

- Cascade layers
- Custom properties (CSS variables)
- `color-mix()`
- `:focus-visible`
- `backdrop-filter`

### Vendor Prefixes

Use Autoprefixer (PostCSS plugin) in build processes.

### Fallback Strategy

Graceful degradation: full functionality in modern browsers, basic usability in older ones. Show outdated browser notice only when content cannot function (include detected version + upgrade options).

---

## 21. Assessment & Compliance

### Excellence Program

**Two tracks:**
1. **Private Sector** - "Approved UAE Design System Expert"
2. **Government Adoption** - "Design System Pioneer"

**Threshold:** 90%+ adherence to design system standards

### Assessment Process

1. Download checklist (Version 2.0, Sept 2023)
2. Validate criteria at each implementation stage
3. Self-evaluate with reasoning
4. Submit completed checklist + website for review

### Testing Methodology

- Separate Lighthouse reports for Desktop and Mobile
- Chrome DevTools in Incognito Mode
- Connection from within the UAE (no VPN)
- Test pages: homepage, about, contact, services, + 3 random service pages

### Performance Benchmarks

| Metric | Target |
|--------|--------|
| Accessibility score | >= 90 |
| SEO score | >= 90 |
| Performance score | >= 90 |
| Best Practices | >= 80 (prefer >= 90) |
| LCP | <= 2.5 seconds |
| FCP | <= 1.8 seconds |

---

## 22. Resources & Tools

### Official Resources

| Resource | URL |
|----------|-----|
| Design System Website | https://designsystem.gov.ae/ |
| GitHub Repository | https://github.com/TDRA-ae/aegov-dls |
| Figma Community File | https://www.figma.com/community/file/1604770692420171644 |
| AI Assistant (UAsk) | https://beta-ask.u.ae/dls |
| NPM Package (HTML) | `@aegov/design-system` |
| NPM Package (React) | `@aegov/design-system-react` |

### Design Tools

- Figma (primary design tool with community file)
- InVision
- Axure RP
- Balsamiq

### Testing Tools

| Category | Tools |
|----------|-------|
| Visual Regression | Percy, Wraith, BackstopJS |
| Cross-browser | BrowserStack, LambdaTest, Sizzy |
| Accessibility | aXe, Wave, Google Lighthouse, Monsido, ColorZilla, a11y |
| Code Validation | W3C Validator, SonarSource |
| Usability | UserTesting.com, Lookback.io |
| Performance | Google PageSpeed Insights, WebPageTest, GTmetrix, Pingdom |

### Icon Library

- **Phosphor Icons:** https://phosphoricons.com
- **React:** `@phosphor-icons/react`
- **CDN:** `https://unpkg.com/@phosphor-icons/web@2.0.3/src/bold/style.css`

### Contact & Community

- Email: design.system@tdra.gov.ae
- GitHub Issues: https://github.com/TDRA-ae/aegov-dls/issues
- Community Discussions: https://github.com/orgs/TDRA-ae/discussions

---

## Appendix: Complete Component CSS Class Reference

| Component | Base Class | Key Modifier Classes |
|-----------|-----------|---------------------|
| Accordion | `.aegov-accordion` | `.accordion-item`, `.accordion-title`, `.accordion-content` |
| Alert | `.aegov-alert` | `.alert-info`, `.alert-error`, `.alert-success`, `.alert-warning`, `.alert-solid` |
| Avatar | `.aegov-avatar` | `.avatar-xs` thru `.avatar-3xl`, `.avatar-rounded`, `.no-user` |
| Badge | `.aegov-badge` | `.badge-info`, `.badge-error`, `.badge-success`, `.badge-warning`, `.badge-soft`, `.badge-solid`, `.badge-lg` |
| Banner | `.aegov-banner` | `.banner-top`, `.banner-bottom`, `.banner-content`, `.banner-notice` |
| Blockquote | `.aegov-quote` | `.quote-colored`, `.quote-footer`, `.quote-author`, `.quote-cite` |
| Breadcrumbs | `.aegov-breadcrumb` | `.with-seperator` |
| Button | `.aegov-btn` | `.btn-outline`, `.btn-soft`, `.btn-link`, `.btn-secondary`, `.btn-icon`, `.btn-xs`, `.btn-sm`, `.btn-base`, `.btn-lg` |
| Card | `.aegov-card` | `.card-bordered`, `.card-glow`, `.card-sm`, `.card-base`, `.card-lg`, `.card-news`, `.card-service`, `.card-creative` |
| Checkbox | `.aegov-check-item` | `.check-sm`, `.check-base`, `.check-lg`, `.check-secondary`, `.aegov-check-group`, `.group-list` |
| Dropdown | `.aegov-dropdown` | `.dropdown-body`, `.dropdown-item`, `.dropdown-header` |
| File Input | `.aegov-file-input-control` | `.file-input-label`, `.file-input-summary`, `.form-control-dropbox` |
| Form Control | `.aegov-form-control` | `.form-control-input`, `.control-prefix`, `.control-suffix`, `.control-error`, `.control-sm`, `.control-base`, `.control-lg`, `.control-secondary` |
| Hyperlink | `.aegov-link` | `.link-soft`, `.link-icon` |
| Modal | `.aegov-modal` | `.aegov-modal-wrapper`, `.aegov-modal-close`, `.modal-serious` |
| Navigation | `.main-navigation` | `.menu`, `.nav-menu`, `.menu-item`, `.menu-item-has-children`, `.active-page`, `.submenu-btn` |
| Pagination | `.aegov-pagination` | `.aegov-pagination-previous`, `.aegov-pagination-next`, `.aegov-pagination-current`, `.aegov-pagination-extend` |
| Popover | `.aegov-popover` | `.popover-header`, `.popover-body` |
| Radio | `.aegov-check-item` | Same as Checkbox |
| Select | `.aegov-form-control` | Same as Form Control |
| Slider | `.aegovs-slider-style` | `.logos-slider`, `.initiative-slider`, `.news-card-slider` |
| Steps | (semantic HTML) | `.step-completed`, `.step-current`, `.step-upcoming`, `.step-disabled`, `.step-sm`, `.step-base`, `.step-lg`, `.step-connector` |
| Tabs | `.aegov-tab` | `.tab-items`, `.tab-link`, `.tab-sm`, `.tab-pills`, `.tab-active` |
| Textarea | `.aegov-form-control` | Same as Form Control |
| Toast | `.aegov-toast` | `.toast-icon`, `.toast-body`, `.toast-dismiss` |
| Toggle | `.aegov-toggle` | `.toggle-item`, `.toggle-success`, `.toggle-mode`, `.toggle-secondary`, `.toggle-icon` |
| Tooltip | `.aegov-tooltip` | `.tooltip-arrow` |

---

*Document compiled from https://designsystem.gov.ae/ and all linked documentation pages.*
*Last updated: May 2026*
