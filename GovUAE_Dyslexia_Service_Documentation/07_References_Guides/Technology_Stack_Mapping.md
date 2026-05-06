---
title: Technology Stack Mapping - Oracle, ServiceNow, Microsoft Integration
version: 1.0
date_created: 2026-05-06
owner: Enterprise Architecture
tags: [technology-stack, oracle, servicenow, microsoft, integration]
---

# Technology Stack Mapping
## Enterprise Platform Integration - Dyslexia Service

---

## 🏗️ ENTERPRISE ARCHITECTURE OVERVIEW

```
                  ┌─────────────────────────────────┐
                  │   Citizen/Educator Interfaces   │
                  │  Web Portal, Mobile, WhatsApp   │
                  └──────────────┬──────────────────┘
                                 │
                  ┌──────────────▼──────────────────┐
                  │    Azure API Management         │
                  │   (Rate Limit, Auth, Monitor)   │
                  └──────────────┬──────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
    ┌───▼────┐          ┌───────▼────────┐      ┌────────▼────┐
    │ Oracle │          │   ServiceNow   │      │  Microsoft  │
    │ Cloud  │          │   Platform     │      │  Platform   │
    │ (CRM)  │          │  (Workflows)   │      │ (Analytics) │
    └───┬────┘          └────────┬───────┘      └────────┬────┘
        │                        │                       │
        └────────────────────────┼───────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  Azure Data Lake        │
                    │  (Raw Data + History)   │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │ Microsoft Power BI      │
                    │ (Dashboards, Reports)   │
                    └─────────────────────────┘
```

---

## 1️⃣ ORACLE CLOUD (CRM & Master Data)

### Primary Role: **Citizen Master Profile + Case Management**

#### Oracle Service Cloud Components

```
┌─────────────────────────────────────────────────────┐
│         ORACLE SERVICE CLOUD (Tenant)               │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  Citizen Management Module                   │  │
│  ├─ Master child profile (golden record)        │  │
│  ├─ Parent/guardian relationships               │  │
│  ├─ Contact preferences (SMS/Email/WhatsApp)    │  │
│  ├─ LGPD consent tracking (digital signatures)  │  │
│  ├─ Data deletion requests (right to be forgotten)
│  └─ Audit trail (all profile changes logged)    │  │
│                                                  │  │
│  ┌──────────────────────────────────────────────┐  │
│  │  Case Management Module                      │  │
│  ├─ Assessment records (baseline results)       │  │
│  ├─ Diagnosis record (risk classification)      │  │
│  ├─ Intervention plan (AI-generated + approved) │  │
│  ├─ Progress notes (weekly/monthly updates)     │  │
│  ├─ Communication history (all interactions)    │  │
│  ├─ Escalation records (when & why escalated)   │  │
│  ├─ Exit records (final assessment + impact)    │  │
│  └─ Document attachments (consent forms, reports)
│                                                  │  │
│  ┌──────────────────────────────────────────────┐  │
│  │  Relationship Management                     │  │
│  ├─ Educator relationships (who referred?)      │  │
│  ├─ ONG relationships (which organization?)     │  │
│  ├─ Specialist relationships (who reviewed?)    │  │
│  └─ Family relationships (siblings in program?) │  │
│                                                  │  │
│  ┌──────────────────────────────────────────────┐  │
│  │  Knowledge Base                              │  │
│  ├─ Service processes (standard operating proc) │  │
│  ├─ Intervention strategies (by deficit type)   │  │
│  ├─ FAQ for parents/educators                  │  │
│  ├─ Regulatory information (LGPD, rights)      │  │
│  └─ Training materials (for all user types)    │  │
│                                                  │  │
│  ┌──────────────────────────────────────────────┐  │
│  │  Data Governance Module                      │  │
│  ├─ Metadata management (what data exists)      │  │
│  ├─ Data lineage (where does data come from)    │  │
│  ├─ Data quality rules (enforce standards)      │  │
│  ├─ Privacy impact assessments                  │  │
│  ├─ Data classification (PII vs. non-PII)       │  │
│  └─ Access control lists (who can see what)     │  │
│                                                  │  │
└─────────────────────────────────────────────────────┘
```

#### Data Model: Child Master Record

```
CHILD_PROFILE Table:
├─ child_id (UUID, primary key)
├─ full_name (encrypted AES-256)
├─ date_of_birth (encrypted)
├─ gender
├─ handedness
├─ native_language
├─ current_school
├─ referral_date
├─ referral_source
├─ parent_id (foreign key to PARENT_PROFILE)
├─ current_status (Registered | Screening | Assessed | In Intervention | Exited)
├─ risk_tier (No Risk | Low | Moderate | High | Critical)
├─ last_assessment_date
├─ next_assessment_due_date
├─ intervention_start_date
├─ intervention_end_date (if exited)
├─ created_date
├─ created_by_user_id
├─ modified_date
├─ modified_by_user_id
├─ created_timestamp (audit)
├─ deleted_date (if LGPD deletion requested)
└─ archived (soft delete flag)

ASSESSMENT_RECORD Table:
├─ assessment_id (UUID)
├─ child_id (foreign key)
├─ assessment_date
├─ assessment_type (Screening | Full Battery | Follow-up)
├─ phonological_score (0-100)
├─ fluency_score (0-100)
├─ comprehension_score (0-100)
├─ visual_score (0-100)
├─ composite_score (weighted)
├─ audiovisual_discrepancy
├─ risk_classification (outcome)
├─ assessor_id (foreign key to SPECIALIST)
├─ quality_flag (if data quality issues)
├─ specialist_review_required (boolean)
├─ specialist_review_date (if >70)
├─ specialist_notes
├─ assessor_notes
└─ archived_timestamp

INTERVENTION_PLAN Table:
├─ plan_id (UUID)
├─ child_id (foreign key)
├─ assessment_id (which assessment triggered this)
├─ plan_date
├─ plan_status (Draft | Approved | Active | Paused | Completed)
├─ intervention_type (Phonological | Fluency | Comp | Multi)
├─ responsible_educator_id (foreign key)
├─ responsible_specialist_id (foreign key)
├─ start_date
├─ target_end_date
├─ phase_1_name / phase_2_name / phase_3_name
├─ phase_1_activities (JSON)
├─ phase_2_activities (JSON)
├─ phase_3_activities (JSON)
├─ acomodations (JSON array)
├─ monitoring_schedule
├─ generated_by_hermes_agent (boolean)
├─ specialist_approval_required (boolean)
├─ specialist_approved_date
├─ specialist_approved_by_id
├─ approval_signature (digital, encrypted)
└─ last_updated_date

PROGRESS_TRACKING Table:
├─ progress_id (UUID)
├─ child_id (foreign key)
├─ plan_id (foreign key)
├─ data_collection_date
├─ collection_type (Weekly | Bi-weekly | Monthly)
├─ wpm_reading_score
├─ phonological_assessment_score
├─ adherence_rate (% of sessions completed)
├─ behavioral_notes (engagement, confidence)
├─ parent_feedback
├─ educator_feedback
├─ need_reclassification (boolean, auto-flagged if ±10 points)
├─ reclassification_date (if triggered)
├─ reclassification_new_tier
├─ reclassification_reason
├─ progress_trend (Improving | Stable | Declining)
└─ next_review_date
```

#### Oracle API Contracts

```
REST API Endpoints (via Azure API Management):

1. POST /oracle/children
   Request:
   {
     "referral_date": "2026-05-06",
     "full_name": "João Silva",
     "date_of_birth": "2020-03-15",
     "parent_id": "uuid",
     "referral_source": "Educator"
   }
   Response:
   {
     "child_id": "uuid",
     "status": "Registered",
     "next_action": "Schedule Screening"
   }

2. GET /oracle/children/{child_id}
   Returns: Full child master profile + assessment history + current plan

3. POST /oracle/assessments/{child_id}
   Request: Assessment results (scores, dates, assessor_id)
   Response: Stored record + risk_classification

4. POST /oracle/plans/{child_id}
   Request: Intervention plan (phases, activities, approvals)
   Response: Plan stored + approval_status

5. POST /oracle/progress/{plan_id}
   Request: Weekly/monthly progress (WPM, adherence, notes)
   Response: Progress logged + reclassification_flag (if needed)

6. GET /oracle/cases?status=HighRisk&days_since_assessment<30
   Returns: All high-risk cases pending specialist review (for Service Board)

7. POST /oracle/consent/{child_id}/revoke
   Request: LGPD right to deletion
   Response: Data anonymized + audit trail + confirmation

8. GET /oracle/audit-trail/{child_id}
   Returns: Complete audit log (who accessed, when, what changed)
```

---

## 2️⃣ SERVICENOW (WORKFLOW ORCHESTRATION)

### Primary Role: **Process Automation + SLA Management + Ticketing**

#### ServiceNow Module Structure

```
┌──────────────────────────────────────────────────────┐
│         SERVICENOW PLATFORM (Single Instance)        │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  ITSM (IT Service Management)                  │ │
│  ├─ Incident Management (escalations, SLA track) │ │
│  ├─ Problem Management (root cause analysis)    │ │
│  ├─ Change Management (approvals for updates)   │ │
│  └─ Known Error Database (common issues)        │ │
│                                                  │ │
│  ┌────────────────────────────────────────────────┐ │
│  │  ITBM (IT Business Management)                 │ │
│  ├─ Portfolio Management (service offerings)     │ │
│  ├─ Project Portfolio Management (programs)      │ │
│  ├─ Resource Management (staffing, allocation)   │ │
│  └─ Financial Management (cost tracking)         │ │
│                                                  │ │
│  ┌────────────────────────────────────────────────┐ │
│  │  Workflow Engine (Custom Flows)                │ │
│  │                                                │ │
│  │  Flow 1: Intake → Screening → Assessment      │ │
│  │  ├─ Create ticket for new referral            │ │
│  │  ├─ Auto-assign to screening specialist       │ │
│  │  ├─ Track SLA (24h intake, 48h screening)    │ │
│  │  ├─ Auto-escalate if >48h                     │ │
│  │  └─ Route to assessment specialist when ready │ │
│  │                                                │ │
│  │  Flow 2: High-Risk Cases → Specialist Review  │ │
│  │  ├─ Detect score >70 (from Oracle)           │ │
│  │  ├─ Create specialist review ticket           │ │
│  │  ├─ Auto-assign to available specialist       │ │
│  │  ├─ Track 48h SLA                            │ │
│  │  ├─ Auto-escalate to ONG coordinator if >48h │ │
│  │  └─ Notify system when review complete       │ │
│  │                                                │ │
│  │  Flow 3: Plan Approval Workflow                │ │
│  │  ├─ AI generates plan                         │ │
│  │  ├─ Route for psychopedagogue review          │ │
│  │  ├─ Collect approval (e-signature)            │ │
│  │  ├─ 2h SLA for approval                      │ │
│  │  ├─ If rejected: route back to AI for revisions
│  │  └─ Once approved: send to communication flow │ │
│  │                                                │ │
│  │  Flow 4: Multi-Channel Communication          │ │
│  │  ├─ Generate SMS for parent (via Twilio)     │ │
│  │  ├─ Generate Email for educator              │ │
│  │  ├─ Generate Email for specialist (if ref)   │ │
│  │  ├─ Update dashboard for ONG coordinator     │ │
│  │  ├─ Log all communications (audit trail)     │ │
│  │  └─ Track delivery confirmation              │ │
│  │                                                │ │
│  │  Flow 5: Reclassification Check                │ │
│  │  ├─ Weekly: check score change (±10 points)  │ │
│  │  ├─ If change detected: create re-assessment │ │
│  │  ├─ Route to assessment specialist            │ │
│  │  ├─ Update intervention plan (if tier changed)
│  │  └─ Notify stakeholders of new classification │ │
│  │                                                │ │
│  │  Flow 6: SLA Escalation Management            │ │
│  │  ├─ Detect any SLA approaching threshold (75%) 
│  │  ├─ Escalate to supervisor                    │ │
│  │  ├─ Auto-assign escalation team               │ │
│  │  ├─ Generate executive report                 │ │
│  │  └─ Track escalation resolution               │ │
│  │                                                │ │
│  │  Flow 7: Incident/Issue Reporting             │ │
│  │  ├─ Create ticket from user feedback          │ │
│  │  ├─ Classify severity (Low/Med/High/Critical) │ │
│  │  ├─ Auto-route to appropriate team            │ │
│  │  ├─ SLA based on severity                    │ │
│  │  ├─ Track resolution                          │ │
│  │  └─ Notify user of status updates             │ │
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Reports & Dashboards                          │ │
│  ├─ Intake SLA Dashboard (% <24h)                 │ │
│  ├─ Specialist Review SLA (% <48h)               │ │
│  ├─ Plan Approval SLA (% <2h + 2h specialist)   │ │
│  ├─ Reclassification Tracking (# per month)      │ │
│  ├─ Escalation Report (reasons, resolution time) │ │
│  └─ Trend Analysis (improving/declining)         │ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

#### ServiceNow Ticket Schema

```
INTAKE_TICKET Table:
├─ ticket_id (auto-generated)
├─ child_id (from Oracle)
├─ created_date
├─ referral_source (Educator | Parent | ONG | Specialist)
├─ priority (Low | Medium | High)
├─ status (New | In Progress | Waiting | Resolved)
├─ assigned_to (Intake Coordinator user ID)
├─ sla_target_date (24h from creation)
├─ sla_status (On Track | At Risk | Overdue)
├─ completion_date
├─ time_to_resolution
├─ notes (validation results, missing data items)
└─ activity_log (who did what, when)

SPECIALIST_REVIEW_TICKET Table:
├─ ticket_id
├─ child_id (from Oracle)
├─ assessment_id (which assessment being reviewed)
├─ created_date
├─ score (composite score, reason for review)
├─ assigned_to (Specialist user ID)
├─ sla_target_date (48h from creation)
├─ sla_status (On Track | At Risk | Overdue)
├─ review_completed_date
├─ specialist_decision (Confirmed | Denied | Referred)
├─ specialist_notes
├─ differential_diagnosis (if considered)
├─ follow-up_actions
└─ approval_signature (digital)

ESCALATION_TICKET Table:
├─ ticket_id
├─ parent_ticket_id (what triggered escalation)
├─ escalation_reason (SLA breach | Quality issue | Safety concern)
├─ escalated_date
├─ escalation_level (ONG Coordinator | Service Board | Executive)
├─ assigned_to (escalation owner)
├─ priority (High | Critical)
├─ resolution_target_date
├─ mitigation_actions
├─ resolved_date
└─ root_cause_analysis
```

#### ServiceNow API Integrations

```
Inbound APIs (from Oracle/Azure):
1. POST /servicenow/tickets/intake
   When: New referral in Oracle
   Data: child_id, referral_date, referral_source
   Action: Create intake ticket, assign, set SLA

2. POST /servicenow/tickets/specialist-review
   When: Assessment score >70 detected
   Data: child_id, assessment_id, composite_score
   Action: Create review ticket, assign specialist

3. POST /servicenow/tickets/reclassification
   When: Reclassification needed (score ±10)
   Data: child_id, old_score, new_score, reason
   Action: Create re-assessment ticket

Outbound APIs (to Oracle/Azure):
1. GET /servicenow/tickets?status=overdue&sla_target<now
   Fetch: All overdue tickets for escalation
   
2. POST /servicenow/tickets/{ticket_id}/resolution
   Update: completion_date, resolution_time, outcomes
   
3. GET /servicenow/reports/sla-compliance?period=weekly
   Generate: SLA metrics by team/process
```

---

## 3️⃣ MICROSOFT PLATFORM (ANALYTICS & AUTOMATION)

### Primary Role: **Dashboards, Power Automations, Data Analytics**

#### Microsoft Stack Components

```
┌──────────────────────────────────────────────────────┐
│         MICROSOFT POWER PLATFORM                     │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Power Apps (Portals & Forms)                  │ │
│  │                                                │ │
│  │  1. Educator Referral Portal                  │ │
│  │     ├─ Intake form (pre-populated from school)│ │
│  │     ├─ LGPD consent collection (digital sig)  │ │
│  │     ├─ Submit → Creates Oracle record + Service NOW ticket
│  │     └─ Real-time status (pending/submitted)   │ │
│  │                                                │ │
│  │  2. Parent Self-Service Portal                │ │
│  │     ├─ Register child                         │ │
│  │     ├─ View assessment results                │ │
│  │     ├─ See intervention plan                  │ │
│  │     ├─ Track progress (WPM trends)            │ │
│  │     ├─ Message educators/specialists          │ │
│  │     └─ Request data deletion (LGPD)           │ │
│  │                                                │ │
│  │  3. Screening Questionnaire Form              │ │
│  │     ├─ Multiple choice (behavioral indicators)│ │
│  │     ├─ Auto-scoring (client-side)             │ │
│  │     ├─ Risk level output (immediate feedback) │ │
│  │     └─ Submit → Trigger triage in ServiceNow  │ │
│  │                                                │ │
│  │  4. Assessment Specialist Dashboard           │ │
│  │     ├─ View scheduled assessments             │ │
│  │     ├─ Enter test results (forms)             │ │
│  │     ├─ See quality checks (data validation)   │ │
│  │     ├─ View WPM scoring guide (reference)     │ │
│  │     └─ Bulk operations (export results)       │ │
│  │                                                │ │
│  │  5. Intervention Plan Approval Form           │ │
│  │     ├─ Display AI-generated plan             │ │
│  │     ├─ Reviewer (psychopedagogue) can edit   │ │
│  │     ├─ Digital signature / approval           │ │
│  │     └─ Submit → Trigger communication workflow│ │
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Power Automate (Workflow Automation)          │ │
│  │                                                │ │
│  │  Automation 1: Assessment Completion Flow      │ │
│  │  ├─ When: Assessment data submitted (from App)│ │
│  │  ├─ Then: Call scoring API (Azure Function)   │ │
│  │  ├─ Then: Update Oracle case                  │ │
│  │  ├─ If score >70: Create specialist ticket   │ │
│  │  ├─ Send confirmation SMS (Twilio)           │ │
│  │  └─ Log activity (audit trail)               │ │
│  │                                                │ │
│  │  Automation 2: Plan Approval Notification      │ │
│  │  ├─ When: Plan approved in ServiceNow         │ │
│  │  ├─ Then: Generate multi-channel notifications│ │
│  │  ├─ SMS to parent (via Twilio)               │ │
│  │  ├─ Email to educator                         │ │
│  │  ├─ Email to specialist (if referred)         │ │
│  │  ├─ Update Oracle case status                 │ │
│  │  └─ Log communications (audit)                │ │
│  │                                                │ │
│  │  Automation 3: Weekly Progress Collection      │ │
│  │  ├─ When: Monday at 8am (scheduled)           │ │
│  │  ├─ Then: Query Oracle for active plans       │ │
│  │  ├─ Then: Send SMS reminder to educator       │ │
│  │  ├─ Then: Create form link (Power App)        │ │
│  │  ├─ When: Form submitted → Update Oracle      │ │
│  │  ├─ Then: Check for reclassification (±10)   │ │
│  │  ├─ If triggered: Create new assessment ticket│ │
│  │  └─ Log progress metrics                      │ │
│  │                                                │ │
│  │  Automation 4: SLA Escalation Alert           │ │
│  │  ├─ When: Hourly check (scheduled)            │ │
│  │  ├─ Then: Query ServiceNow for SLA breaches   │ │
│  │  ├─ Then: Send email to coordinator           │ │
│  │  ├─ Then: Update escalation ticket (severity) │ │
│  │  └─ Then: Notify executive (if critical)     │ │
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Power BI (Analytics & Reporting)              │ │
│  │                                                │ │
│  │  Dashboard 1: ONG Coordinator Dashboard        │ │
│  │  ├─ Current caseload (total children, by tier)│ │
│  │  ├─ SLA compliance (% <target time)           │ │
│  │  ├─ Intake queue (pending assignments)        │ │
│  │  ├─ Assessment schedule (completed vs. pending)
│  │  ├─ High-risk cases (pending specialist review)
│  │  ├─ Intervention plans (active, pending approval)
│  │  ├─ Escalations (current, unresolved)         │ │
│  │  └─ KPI metrics (targets vs. actual)          │ │
│  │                                                │ │
│  │  Dashboard 2: Educator Dashboard               │ │
│  │  ├─ My referred children (status tracking)    │ │
│  │  ├─ Assessment results (when available)       │ │
│  │  ├─ Intervention plans & strategies           │ │
│  │  ├─ Child progress (WPM trends, improvement %) 
│  │  ├─ Recommended acomodations                 │ │
│  │  └─ Resource materials (strategies, tools)    │ │
│  │                                                │ │
│  │  Dashboard 3: Government Oversight Dashboard  │ │
│  │  ├─ Program metrics (children served per state)
│  │  ├─ Service maturity (% following standard process)
│  │  ├─ Quality metrics (accuracy, equity, outcomes)
│  │  ├─ Compliance status (LGPD, SLA, audit)      │ │
│  │  ├─ Specialist capacity (supply vs. demand)   │ │
│  │  ├─ Budget tracking (cost per child)          │ │
│  │  └─ Impact metrics (improvement rate, ROI)    │ │
│  │                                                │ │
│  │  Dashboard 4: Operational Health               │ │
│  │  ├─ System uptime (99.5% target)              │ │
│  │  ├─ API response times (latency)              │ │
│  │  ├─ Data quality scores (completeness, accuracy)
│  │  ├─ Error rates (failures, retries)           │ │
│  │  ├─ User activity (logins, actions)           │ │
│  │  └─ Help desk tickets (volume, resolution time)
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 4️⃣ AZURE DATA PLATFORM

### Primary Role: **Centralized Data Lake + Analytics + AI/ML**

```
┌──────────────────────────────────────────────────────┐
│         AZURE DATA PLATFORM                          │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Azure Data Lake Storage (Gen 2)               │ │
│  │  ├─ Raw data zone (all assessments, progress)  │ │
│  │  ├─ Processed zone (cleaned, validated data)   │ │
│  │  ├─ Analytics zone (aggregated metrics)        │ │
│  │  ├─ Audit zone (compliance, access logs)       │ │
│  │  └─ Archive zone (historical data >2 years)    │ │
│  │                                                │ │
│  │  Storage by Entity:                            │ │
│  │  ├─ /child_assessments/ (1M+ records)         │ │
│  │  ├─ /progress_tracking/ (weekly updates)       │ │
│  │  ├─ /intervention_plans/ (structured)          │ │
│  │  ├─ /communications/ (SMS/email logs)          │ │
│  │  ├─ /audit_logs/ (every action logged)         │ │
│  │  ├─ /reference_data/ (norms, thresholds)       │ │
│  │  └─ /ml_features/ (extracted for models)       │ │
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Azure Synapse Analytics (SQL + Spark)         │ │
│  │  ├─ Data warehouse (DW schema)                 │ │
│  │  ├─ Fact table: FACT_ASSESSMENT                │ │
│  │  │  └─ child_id, assessment_date, scores      │ │
│  │  ├─ Dimension tables: DIM_CHILD, DIM_DATE...   │ │
│  │  ├─ Fact table: FACT_PROGRESS                  │ │
│  │  │  └─ child_id, week, wpm, adherence         │ │
│  │  ├─ Spark notebooks: ML feature engineering    │ │
│  │  └─ SQL queries: Generate Power BI datasets    │ │
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Azure Machine Learning (Predictive Models)    │ │
│  │                                                │ │
│  │  Model 1: Reclassification Predictor           │ │
│  │  ├─ Input: Assessment profile, intervention    │ │
│  │  ├─ Output: Predicted score at 3/6 months      │ │
│  │  ├─ Training: Historical assessment data       │ │
│  │  ├─ Use: Proactive plan adjustment             │ │
│  │  └─ Monitoring: Monthly retraining              │ │
│  │                                                │ │
│  │  Model 2: Dropout Prediction                   │ │
│  │  ├─ Input: Engagement metrics, adherence       │ │
│  │  ├─ Output: Probability of program dropout     │ │
│  │  ├─ Use: Early intervention (if risk high)     │ │
│  │  └─ Monitoring: Weekly model performance       │ │
│  │                                                │ │
│  │  Model 3: Assessment Accuracy Validator        │ │
│  │  ├─ Input: Assessment scores, follow-up outcome
│  │  ├─ Output: Confidence in classification       │ │
│  │  ├─ Use: Flag potentially false positives      │ │
│  │  └─ Monitoring: Quarterly validation           │ │
│  │                                                │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🔗 INTEGRATION FLOWS (Key Workflows)

### Flow 1: Complete Child Journey

```
Parent Referral (Web Portal)
  ↓
Create Oracle CHILD_PROFILE record
  ↓
ServiceNow creates INTAKE_TICKET (24h SLA)
  ↓
Intake Coordinator validates data
  ↓
Route to Screening Specialist
  ↓
Screening questionnaire (Power App)
  ↓
Triage decision (automated)
  ↓
If High Risk:
  ├─ Create ServiceNow SPECIALIST_REVIEW_TICKET
  ├─ Route to specialist
  └─ 48h SLA tracking
  ↓
Assessment scheduled
  ↓
3 sessions (Power App for data entry)
  ↓
Auto-scoring (Azure Function API)
  ↓
Update Oracle ASSESSMENT_RECORD
  ↓
If score >70:
  ├─ Power Automate triggers specialist review
  ├─ Specialist reviews in Power App
  ├─ Approval creates ServiceNow approval ticket
  └─ E-signature captured
  ↓
AI generates plan (Hermes Agent)
  ↓
Psychopedagogue reviews in Power App
  ↓
Approval → Power Automate triggers communications
  ├─ SMS to parent (Twilio)
  ├─ Email to educator
  ├─ Email to specialist (if referred)
  └─ Update ONG dashboard
  ↓
Intervention begins
  ↓
Weekly progress collection (Power App)
  ↓
Data synced to Oracle PROGRESS_TRACKING
  ↓
Power BI dashboards updated (real-time)
  ↓
Monthly reclassification check (Azure Logic)
  ├─ If ±10 points: Create new assessment
  └─ Power Automate notifies stakeholders
  ↓
6-month exit assessment
  ↓
Impact report generation (Power BI + Synapse)
  ↓
Program closeout (Oracle case archived)
```

---

## 📊 Technology Stack: License & Cost Model

```
Component              Annual License Cost (10k children/year)
─────────────────────────────────────────────────────────
Oracle Service Cloud   R$ 500,000 (enterprise tier)
ServiceNow Platform    R$ 450,000 (enterprise tier + workflows)
Microsoft Power Platform  R$ 200,000 (500 users, Power Apps/Automate)
Azure Cloud (Data Lake + Synapse)  R$ 300,000 (compute + storage)
Azure AI/ML Services   R$ 100,000 (model training + inference)
Twilio Communications  R$ 50,000 (SMS/WhatsApp at scale)
SendGrid Email Service R$ 20,000 (email at scale)
─────────────────────────────────────────────────────────
TOTAL ANNUAL           R$ 1,620,000 (~$324k USD)

Cost per Child/Year:   R$ 162 (or ~$32 USD)
  Note: Technology costs are 14% of total cost of service (R$1,156/child)
  Rest goes to people (assessors, specialists, coordinators)
```

---

## ✅ Implementation Roadmap

```
Phase 1: Foundation (Month 1-2)
├─ Provision Oracle Cloud tenant
├─ Deploy ServiceNow instance
├─ Set up Azure subscriptions
├─ Establish data governance policies
└─ Initial infrastructure testing

Phase 2: Integration (Month 3-4)
├─ Build Oracle ↔ ServiceNow APIs
├─ Build Oracle ↔ Azure Data Lake connectors
├─ Develop Power Apps (intake, screening, assessment)
├─ Build Power Automate workflows
├─ Test end-to-end data flows

Phase 3: Pilot (Month 5-6)
├─ Deploy to 2 pilot ONGs
├─ Real-world testing with 500 children
├─ Collect feedback + refine
├─ Validate data quality
├─ Stress-test performance

Phase 4: Scale (Month 7-12)
├─ Deploy to all 20 partner ONGs
├─ Full training program
├─ 24/7 support setup
├─ Performance monitoring
├─ Continuous optimization
```

---

**Document prepared for enterprise architecture & technology governance**
*Demonstrates: Enterprise system integration, data architecture, automation strategy, technology governance readiness*
