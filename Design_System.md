---
title: GovUAE Dyslexia Service Design System
version: 1.0
date_created: 2026-05-06
owner: Design & UX Team
tags: [design-system, visual-language, components, guidelines, accessibility]
---

# Design System
## GovUAE Dyslexia Monitoring & Intervention Service

---

## 1. Executive Summary

This Design System provides a comprehensive set of guidelines, components, and patterns for the GovUAE Dyslexia Service platform. It ensures consistency across all digital touchpoints, improves user experience for diverse stakeholders (citizens, educators, specialists, government officials), and supports scalability across multiple ONGs.

**Key Principles:**
- 🟢 **Citizen-Centric**: Simple, accessible interfaces for parents and educators
- 🔵 **Professional**: Enterprise-grade governance and compliance tools
- 📊 **Data-Driven**: Clear visualization of metrics and outcomes
- ♿ **Inclusive**: WCAG 2.1 AA accessibility compliance
- 🚀 **Scalable**: Reusable components across all service areas

---

## 2. Visual Identity

### 2.1 Color Palette

#### Primary Colors
| Color | Hex | Usage | WCAG Contrast |
|-------|-----|-------|---------------|
| **Primary Blue** | `#0066cc` | Primary actions, headers, navigation | ✅ AA+ |
| **Secondary Blue** | `#0088ff` | Hover states, secondary elements | ✅ AA+ |
| **Accent Green** | `#00aa44` | Success, positive states, completion | ✅ AA+ |
| **Warning Orange** | `#ff6600` | Alerts, cautions, in-progress | ✅ AA+ |
| **Danger Red** | `#cc0000` | Critical alerts, errors, escalations | ✅ AA+ |

#### Neutral Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Dark Gray** | `#1a1a1a` | Text, dark backgrounds |
| **Medium Gray** | `#666666` | Secondary text, borders |
| **Light Gray** | `#f5f5f5` | Backgrounds, panels |
| **White** | `#ffffff` | Content areas, clean backgrounds |

#### Semantic Colors
| Context | Color | Hex | Meaning |
|---------|-------|-----|---------|
| **Success** | Green | `#00aa44` | Process completed, positive outcome |
| **Pending** | Orange | `#ff6600` | In progress, awaiting action |
| **Critical** | Red | `#cc0000` | Error, escalation required |
| **Info** | Blue | `#0066cc` | Informational, neutral |
| **Neutral** | Gray | `#666666` | Neutral state, no action |

### 2.2 Typography

#### Font Families
```
Headings: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
Body Text: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
Monospace: "Courier New", monospace
```

#### Type Scale
| Element | Size | Weight | Line Height | Usage |
|---------|------|--------|-------------|-------|
| **H1** | 2.5rem (40px) | 700 Bold | 1.2 | Page titles, major sections |
| **H2** | 1.8rem (28px) | 700 Bold | 1.3 | Section headers |
| **H3** | 1.4rem (22px) | 600 Semi-Bold | 1.4 | Subsection headers |
| **Body Large** | 1.125rem (18px) | 400 Regular | 1.6 | Key information |
| **Body Regular** | 1rem (16px) | 400 Regular | 1.6 | Standard text |
| **Body Small** | 0.875rem (14px) | 400 Regular | 1.5 | Secondary text |
| **Caption** | 0.75rem (12px) | 500 Medium | 1.4 | Metadata, labels |

#### Font Weights
- **700 (Bold)**: Headings, emphasis
- **600 (Semi-Bold)**: Subheadings, important labels
- **500 (Medium)**: Navigation, interactive elements
- **400 (Regular)**: Body text, standard content

### 2.3 Spacing System

Base unit: **8px**

| Scale | Value | Usage |
|-------|-------|-------|
| **xs** | 4px | Micro spacing |
| **sm** | 8px | Padding, margins (small) |
| **md** | 16px | Standard padding, margins |
| **lg** | 24px | Large spacing |
| **xl** | 32px | Extra large spacing |
| **2xl** | 48px | Sections |
| **3xl** | 64px | Major sections |

### 2.4 Border Radius

| Type | Radius | Usage |
|------|--------|-------|
| **Small** | 4px | Buttons, inputs |
| **Medium** | 8px | Cards, panels |
| **Large** | 16px | Large components, modals |
| **Full** | 50% | Circular elements, badges |

---

## 3. Components

### 3.1 Button Component

#### Primary Button
- **Background**: Primary Blue `#0066cc`
- **Text**: White, Medium weight
- **Padding**: 12px 24px
- **Border Radius**: 4px
- **State Variants**: Default, Hover, Active, Disabled

#### Secondary Button
- **Background**: Light Gray `#f5f5f5`
- **Border**: 1px Medium Gray `#666666`
- **Text**: Dark Gray `#1a1a1a`, Medium weight
- **Padding**: 12px 24px
- **Border Radius**: 4px

#### Danger Button
- **Background**: Danger Red `#cc0000`
- **Text**: White, Medium weight
- **Padding**: 12px 24px
- **Border Radius**: 4px
- **Usage**: Destructive actions, escalations

### 3.2 Card Component

```
┌─────────────────────────────┐
│ Header (optional)           │
├─────────────────────────────┤
│ Content Area (16px padding) │
│                             │
├─────────────────────────────┤
│ Footer (optional)           │
└─────────────────────────────┘
```

**Properties:**
- **Background**: White `#ffffff`
- **Border**: 1px Light Gray `#f5f5f5`
- **Border Radius**: 8px
- **Shadow**: `0 2px 8px rgba(0,0,0,0.1)`
- **Padding**: 24px
- **Hover Effect**: Shadow elevation to `0 4px 12px rgba(0,0,0,0.15)`

### 3.3 Badge Component

| Style | Background | Text | Usage |
|-------|-----------|------|-------|
| **Success** | Green `#00aa44` | White | Completed, active |
| **Warning** | Orange `#ff6600` | White | In progress, pending |
| **Critical** | Red `#cc0000` | White | Error, escalation |
| **Info** | Blue `#0066cc` | White | Informational |
| **Neutral** | Gray `#f5f5f5` | Dark Gray | Neutral state |

**Properties:**
- **Padding**: 4px 12px
- **Border Radius**: 50%
- **Font Size**: 12px
- **Font Weight**: 600 (Semi-Bold)

### 3.4 Status Indicator

```
🟢 Active / Completed
🟡 Pending / In Progress
🔴 Critical / Error
⚪ Neutral / Inactive
```

**Sizes:**
- **Small**: 8px diameter
- **Medium**: 12px diameter
- **Large**: 16px diameter

### 3.5 Table Component

| Element | Style | Notes |
|---------|-------|-------|
| **Header Row** | Background: Light Gray `#f5f5f5`, Font Weight: 600 | Sticky on scroll |
| **Data Rows** | Background: White, Border: 1px `#f5f5f5` | Alternate gray on hover |
| **Hover State** | Background: Light Gray `#f5f5f5` | Improved readability |
| **Cell Padding** | 16px | Vertical & horizontal |

### 3.6 Form Components

#### Input Field
- **Border**: 1px Medium Gray `#666666`
- **Border Radius**: 4px
- **Padding**: 12px 16px
- **Focus State**: Border color → Primary Blue `#0066cc`, Shadow: `0 0 0 3px rgba(0,102,204,0.1)`
- **Error State**: Border color → Danger Red `#cc0000`, Help text in red

#### Dropdown/Select
- **Background**: White `#ffffff`
- **Border**: 1px Medium Gray `#666666`
- **Arrow Icon**: Primary Blue `#0066cc`
- **Padding**: 12px 16px
- **Border Radius**: 4px

#### Checkbox/Radio
- **Unchecked**: Border 2px Medium Gray `#666666`, Background White
- **Checked**: Background Primary Blue `#0066cc`, Checkmark White
- **Size**: 20px × 20px

### 3.7 Alert/Notification Component

```
┌─────────────────────────────────┐
│ 🟢 Success Title                │
│ Description text for the alert. │
│ [Optional Action Link]          │
└─────────────────────────────────┘
```

#### Alert Variants
| Type | Icon | Background | Border | Text |
|------|------|-----------|--------|------|
| **Success** | ✅ | Light Green | Green `#00aa44` | Dark Gray |
| **Warning** | ⚠️ | Light Orange | Orange `#ff6600` | Dark Gray |
| **Error** | ❌ | Light Red | Red `#cc0000` | Dark Gray |
| **Info** | ℹ️ | Light Blue | Blue `#0066cc` | Dark Gray |

---

## 4. Layout Patterns

### 4.1 Master-Detail Layout
```
┌──────────────────────────────────┐
│ Navigation/Sidebar               │
├──────────────────────────────────┤
│ Main Content Area                │
│                                  │
│ ┌──────────────┐ ┌────────────┐ │
│ │ List/Table   │ │ Detail View│ │
│ │              │ │            │ │
│ └──────────────┘ └────────────┘ │
└──────────────────────────────────┘
```

### 4.2 Dashboard Grid
- **Grid System**: 12-column responsive grid
- **Breakpoints**:
  - **Mobile**: < 768px (1 column)
  - **Tablet**: 768px - 1024px (2 columns)
  - **Desktop**: > 1024px (3-4 columns)

### 4.3 Navigation Patterns

#### Top Navigation Bar
- **Height**: 64px
- **Background**: Primary Blue `#0066cc`
- **Text**: White
- **Items**: Logo, Navigation Links, User Profile, Logout
- **Sticky**: Yes, on scroll

#### Sidebar Navigation
- **Width**: 250px (collapsible to 60px)
- **Background**: Light Gray `#f5f5f5`
- **Border**: 1px Right Gray
- **Items**: Main sections, collapsible groups
- **Active State**: Left border Primary Blue, text bold

#### Breadcrumb Navigation
```
Home > Governance > RACI Matrix > Activity 1.1
```
- **Separator**: `/`
- **Active Item**: Bold, Primary Blue
- **Clickable Items**: Underlined on hover

---

## 5. Data Visualization

### 5.1 Charts & Graphs

#### Bar Charts
- **Colors**: Primary Blue `#0066cc` (primary), Secondary Blue `#0088ff` (secondary)
- **Spacing**: 8px between bars
- **Labels**: 12px, Dark Gray `#1a1a1a`

#### Line Charts
- **Line Color**: Primary Blue `#0066cc`
- **Fill Color**: rgba(0, 102, 204, 0.1)
- **Point Color**: Primary Blue `#0066cc`
- **Grid**: Light Gray `#f5f5f5`

#### Pie/Donut Charts
- **Color Sequence**: Primary Blue → Secondary Blue → Green → Orange → Red
- **Labels**: 12px, Dark Gray
- **Legend**: Below chart, clickable for filtering

### 5.2 Metrics Widgets

```
┌──────────────────────┐
│ Metric Title         │
│ 95%                  │
│ ↑ 5% vs last month   │
└──────────────────────┘
```

- **Title**: Small, Gray `#666666`
- **Value**: Large (2rem), Bold, Primary Blue `#0066cc`
- **Trend**: Small, Green `#00aa44` (up), Red `#cc0000` (down)

---

## 6. Accessibility Standards

### 6.1 Color Contrast
- **Text**: Minimum 4.5:1 ratio (WCAG AA)
- **Large Text**: Minimum 3:1 ratio (WCAG AA)
- **UI Components**: Minimum 3:1 ratio (WCAG AA)

### 6.2 Focus Management
- **Focus Indicator**: 3px solid Primary Blue `#0066cc`
- **Focus Order**: Logical, left-to-right, top-to-bottom
- **Keyboard Navigation**: Tab, Shift+Tab, Enter, Arrow keys

### 6.3 Semantic HTML
- **Headings**: Use H1-H6 in proper hierarchy
- **Lists**: Use `<ul>`, `<ol>`, `<li>` appropriately
- **Forms**: Use proper `<label>` associations
- **Buttons**: Use `<button>` element, not links styled as buttons

### 6.4 ARIA Labels
- **aria-label**: For icon-only buttons
- **aria-describedby**: For form validation messages
- **aria-live**: For dynamic content updates
- **role**: Only when semantic HTML insufficient

### 6.5 Text Alternatives
- **Images**: Descriptive alt text
- **Icons**: Aria-label or title attribute
- **Charts**: Data table alternative

---

## 7. Responsive Design

### 7.1 Breakpoints
```css
/* Mobile First */
Mobile: 320px - 767px
Tablet: 768px - 1023px
Desktop: 1024px+
```

### 7.2 Responsive Behavior
| Component | Mobile | Tablet | Desktop |
|-----------|--------|--------|---------|
| **Sidebar** | Hidden, toggle menu | Visible, collapsible | Visible fixed |
| **Table** | Stacked rows | Scroll horizontal | Full table |
| **Columns** | 1 column | 2 columns | 3+ columns |
| **Typography** | Scaled down 10% | Normal | Normal |

### 7.3 Touch Targets
- **Minimum Size**: 44px × 44px (mobile)
- **Spacing**: 8px minimum between targets
- **Mobile Buttons**: Padding increased to 16px

---

## 8. Interaction Patterns

### 8.1 Loading States
```
🔄 Loading...
⏳ Processing...
```

- **Spinner**: Primary Blue `#0066cc`
- **Duration**: Animated 1.5s rotation
- **Message**: Below or beside spinner

### 8.2 Empty States
```
📭 No data available
Create your first item to get started.
[+ Create Item Button]
```

- **Icon**: Large, Light Gray `#f5f5f5`
- **Message**: Helpful, actionable text
- **Action**: Primary button for next step

### 8.3 Transitions & Animations
| Action | Animation | Duration | Easing |
|--------|-----------|----------|--------|
| **Hover** | Color/Shadow | 200ms | ease-in-out |
| **Open/Close** | Fade + Scale | 300ms | ease-in-out |
| **Slide** | Slide + Fade | 400ms | ease-out |
| **Loading** | Spin | 1500ms | linear |

### 8.4 Confirmation Dialogs
```
┌─────────────────────────────┐
│ ⚠️ Confirm Action           │
├─────────────────────────────┤
│ Are you sure? This cannot   │
│ be undone.                  │
├─────────────────────────────┤
│ [Cancel]      [Confirm]     │
└─────────────────────────────┘
```

- **Width**: 400px max
- **Button Order**: Cancel (secondary), Confirm (danger)

---

## 9. Page Templates

### 9.1 Content Page Template
```
┌──────────────────────────────────┐
│ Navigation Bar                   │
├──────────────────────────────────┤
│ ┌────────────┬────────────────┐ │
│ │  Sidebar   │  Content       │ │
│ │            │  ┌──────────┐  │ │
│ │ Navigation │  │ H1 Title │  │ │
│ │ Links      │  ├──────────┤  │ │
│ │            │  │          │  │ │
│ │            │  │ Content  │  │ │
│ │            │  │          │  │ │
│ │            │  │          │  │ │
│ └────────────┴────────────────┘ │
├──────────────────────────────────┤
│ Footer                           │
└──────────────────────────────────┘
```

### 9.2 Dashboard Template
```
┌──────────────────────────────────┐
│ Navigation Bar                   │
├──────────────────────────────────┤
│ Breadcrumb / Title               │
├──────────────────────────────────┤
│ ┌────────┐ ┌────────┐ ┌────────┐│
│ │ Widget │ │ Widget │ │ Widget ││
│ └────────┘ └────────┘ └────────┘│
│ ┌────────────────────────────────┤│
│ │ Large Chart / Table            ││
│ │                                ││
│ └────────────────────────────────┘│
└──────────────────────────────────┘
```

### 9.3 Form Template
```
┌──────────────────────────────────┐
│ Form Title                       │
├──────────────────────────────────┤
│ Field Label*                     │
│ [Input Field                   ] │
│ Help text or error message       │
│                                  │
│ Field Label*                     │
│ [Dropdown                      ] │
│                                  │
│ [Cancel Button] [Submit Button] │
└──────────────────────────────────┘
```

---

## 10. Usage Guidelines

### 10.1 Best Practices

✅ **DO:**
- Use semantic HTML elements
- Maintain consistent spacing and typography
- Test with keyboard navigation
- Provide alt text for images
- Use color purposefully (not just for decoration)
- Ensure sufficient contrast ratios
- Test on multiple devices and browsers

❌ **DON'T:**
- Use color alone to convey information
- Rely on hover states for critical information
- Create nested interactive elements
- Use tables for layout
- Auto-play audio or video
- Flash or blink content (accessibility risk)

### 10.2 Component Selection Guide

| Need | Component | Alternative |
|------|-----------|------------|
| Primary action | Primary Button | Icon + Text |
| Secondary action | Secondary Button | Link |
| Confirmation | Alert Dialog | Toast Notification |
| Error feedback | Form Error | Tooltip |
| Status indication | Badge | Status Indicator |
| Large datasets | Table | Cards Grid |

---

## 11. Implementation

### 11.1 CSS Variables
```css
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
  --font-size-body: 1rem;
  --font-size-small: 0.875rem;
}
```

### 11.2 Responsive Utilities
```css
@media (max-width: 767px) {
  /* Mobile styles */
}

@media (min-width: 768px) and (max-width: 1023px) {
  /* Tablet styles */
}

@media (min-width: 1024px) {
  /* Desktop styles */
}
```

---

## 12. Design Tokens Summary

| Token | Value | Category |
|-------|-------|----------|
| Primary Color | `#0066cc` | Color |
| Success Color | `#00aa44` | Color |
| Warning Color | `#ff6600` | Color |
| Danger Color | `#cc0000` | Color |
| Base Spacing | 8px | Spacing |
| Small Radius | 4px | Radius |
| Typography Scale | 8 levels | Typography |
| Breakpoint 1 | 768px | Responsive |
| Breakpoint 2 | 1024px | Responsive |

---

**Document prepared for consistent UX/UI across GovUAE Dyslexia Service Platform**
*Ensures: Visual consistency, accessibility compliance, professional quality, scalability*
