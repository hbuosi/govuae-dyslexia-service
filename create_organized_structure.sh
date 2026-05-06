#!/bin/bash

# Create main documentation folder
MAIN_DIR="GovUAE_Dyslexia_Service_Documentation"
mkdir -p "$MAIN_DIR"

# Create subdirectories
mkdir -p "$MAIN_DIR/01_Portal"
mkdir -p "$MAIN_DIR/02_Governance_Strategy"
mkdir -p "$MAIN_DIR/03_Operations_Process"
mkdir -p "$MAIN_DIR/04_Technology_Architecture"
mkdir -p "$MAIN_DIR/05_Visual_Diagrams"
mkdir -p "$MAIN_DIR/06_PDF_Output"
mkdir -p "$MAIN_DIR/07_References_Guides"
mkdir -p "$MAIN_DIR/_System_Design"

# Copy Portal files
cp index.html "$MAIN_DIR/01_Portal/" 2>/dev/null
cp README_HTML_DOCUMENTATION.md "$MAIN_DIR/01_Portal/" 2>/dev/null

# Copy Governance & Strategy files
cp AS-IS_TO-BE_Analysis.html "$MAIN_DIR/02_Governance_Strategy/" 2>/dev/null
cp Target_Operating_Model.html "$MAIN_DIR/02_Governance_Strategy/" 2>/dev/null
cp RACI_Governance_Matrix.html "$MAIN_DIR/02_Governance_Strategy/" 2>/dev/null
cp Risk_Register.html "$MAIN_DIR/02_Governance_Strategy/" 2>/dev/null

# Copy Operations & Process files
cp Child_Monitoring_Service_Card_Dyslexia_ENHANCED.html "$MAIN_DIR/03_Operations_Process/" 2>/dev/null
cp spec-process-dyslexia-monitoring.html "$MAIN_DIR/03_Operations_Process/" 2>/dev/null

# Copy Technology files
cp Technology_Stack_Mapping.html "$MAIN_DIR/04_Technology_Architecture/" 2>/dev/null

# Copy Visual Diagrams
cp Child_Monitoring_Dyslexia_BPMN_Detailed.html "$MAIN_DIR/05_Visual_Diagrams/" 2>/dev/null

# Copy PDFs
cp PDF_Output/*.pdf "$MAIN_DIR/06_PDF_Output/" 2>/dev/null

# Copy numbered versions and other files
cp 0*.html "$MAIN_DIR/07_References_Guides/" 2>/dev/null
cp *.md "$MAIN_DIR/07_References_Guides/" 2>/dev/null

echo "✓ Folder structure created: $MAIN_DIR"
echo ""
echo "Folder Structure:"
tree -L 2 "$MAIN_DIR" 2>/dev/null || find "$MAIN_DIR" -maxdepth 2 -type d | sort

