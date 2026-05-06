#!/usr/bin/env python3
"""
Manually translate Service Card from Portuguese to English using pattern replacement
"""

import re

def translate_portuguese_to_english(text):
    """Translate Portuguese text to English"""

    # Portuguese to English dictionary for Service Card content
    translations = {
        # Headers and titles
        r'\bSistema Inteligente de Monitoramento e Interven[çc]ão em Dislexia\b': 'Intelligent Dyslexia Monitoring and Intervention System',
        r'\bSistema Inteligente de Monitoramento\b': 'Intelligent Monitoring System',
        r'\bSistema de Monitoramento\b': 'Monitoring System',
        r'\bInteligência em Monitoramento de Dislexia\b': 'Dyslexia Intelligence Monitoring',

        # Common words
        r'\bMonitoramento Cont[íi]nuo\b': 'Continuous Monitoring',
        r'\bMonitoramento\b': 'Monitoring',
        r'\bmonitoramento\b': 'monitoring',
        r'\bInterven[çc][ãa]o\b': 'Intervention',
        r'\binterven[çc][ãa]o\b': 'intervention',
        r'\bInteligência\b': 'Intelligence',
        r'\binteligência\b': 'intelligence',
        r'\bAvaliation\b': 'Assessment',
        r'\bavaliation\b': 'assessment',
        r'\bProgresso\b': 'Progress',
        r'\bprogresso\b': 'progress',
        r'\bPrograma\b': 'Program',
        r'\bprograma\b': 'program',
        r'\bEstágio\b': 'Stage',
        r'\bestágio\b': 'stage',
        r'\bAtividades\b': 'Activities',
        r'\batividades\b': 'activities',
        r'\bPapél\b': 'Role',
        r'\bpapel\b': 'role',
        r'\bResponsabilidade\b': 'Responsibility',
        r'\bresponsabilidade\b': 'responsibility',
        r'\bObjectivos\b': 'Objectives',
        r'\bobjetivos\b': 'objectives',
        r'\bPeríodo\b': 'Period',
        r'\bperíodo\b': 'period',
        r'\bTempo\b': 'Time',
        r'\btempo\b': 'time',
        r'\bDuração\b': 'Duration',
        r'\bduração\b': 'duration',
        r'\bDescri[çc][ãa]o\b': 'Description',
        r'\bdescri[çc][ãa]o\b': 'description',
        r'\bRelat[óo]rio\b': 'Report',
        r'\brelatório\b': 'report',
        r'\bRecursos\b': 'Resources',
        r'\brecursos\b': 'resources',
        r'\bEducacional\b': 'Educational',
        r'\beducacional\b': 'educational',
        r'\bPedagógica\b': 'Pedagogical',
        r'\bpedagógica\b': 'pedagogical',
        r'\bDocente\b': 'Teacher',
        r'\bdocente\b': 'teacher',
        r'\bEducador\b': 'Educator',
        r'\beducador\b': 'educator',
        r'\bProfessor\b': 'Teacher',
        r'\bprofessor\b': 'teacher',
        r'\bCrian[çc]as\b': 'Children',
        r'\bcrian[çc]as\b': 'children',
        r'\bEstudante\b': 'Student',
        r'\bestudante\b': 'student',
        r'\bCoordena[dç][ao]r\b': 'Coordinator',
        r'\bcoordena[dç][ao]r\b': 'coordinator',
        r'\bGestor\b': 'Manager',
        r'\bgestor\b': 'manager',
        r'\bStakeholder\b': 'Stakeholder',
        r'\bAcess[óo]\b': 'Access',
        r'\bacesso\b': 'access',
        r'\bComunica[çc][ãa]o\b': 'Communication',
        r'\bcomunica[çc][ãa]o\b': 'communication',
        r'\bAvalia[çc][ãa]o\b': 'Evaluation',
        r'\bavalia[çc][ãa]o\b': 'evaluation',
        r'\bTeste\b': 'Test',
        r'\bteste\b': 'test',
        r'\bTestes\b': 'Tests',
        r'\btestes\b': 'tests',
        r'\bAn[áa]lise\b': 'Analysis',
        r'\ban[áa]lise\b': 'analysis',
        r'\bRegistro\b': 'Record',
        r'\bregistro\b': 'record',
        r'\bDocumenta[çc][ãa]o\b': 'Documentation',
        r'\bdocumenta[çc][ãa]o\b': 'documentation',
        r'\bAlternativa\b': 'Alternative',
        r'\balternativa\b': 'alternative',
        r'\bRecommenda[çc][ãa]o\b': 'Recommendation',
        r'\brecommenda[çc][ãa]o\b': 'recommendation',
        r'\bDefinance\b': 'Deficit',
        r'\bD[ée]ficit\b': 'Deficit',
        r'\bd[ée]ficit\b': 'deficit',
        r'\bDificuldade\b': 'Difficulty',
        r'\bdificuldade\b': 'difficulty',
        r'\bAprendizado\b': 'Learning',
        r'\baprendizado\b': 'learning',
        r'\bLeitura\b': 'Reading',
        r'\bleitura\b': 'reading',
        r'\bEscrita\b': 'Writing',
        r'\bescrita\b': 'writing',
        r'\bCompara[çc][ãa]o\b': 'Comparison',
        r'\bcompara[çc][ãa]o\b': 'comparison',
        r'\bConcl[uú]s[ãa]o\b': 'Conclusion',
        r'\bconcl[uú]s[ãa]o\b': 'conclusion',
        r'\bEspecialista\b': 'Specialist',
        r'\bespecialista\b': 'specialist',
        r'\bPsicólogo\b': 'Psychologist',
        r'\bpsicólogo\b': 'psychologist',
        r'\bConsult[óo]rio\b': 'Consultation',
        r'\bconsult[óo]rio\b': 'consultation',
        r'\bReuni[ãa]o\b': 'Meeting',
        r'\breuni[ãa]o\b': 'meeting',
        r'\bFerramentas\b': 'Tools',
        r'\bferramentas\b': 'tools',
        r'\bMetodologia\b': 'Methodology',
        r'\bmetodologia\b': 'methodology',
        r'\bProcesso\b': 'Process',
        r'\bprocesso\b': 'process',
        r'\bEtapa\b': 'Stage',
        r'\betapa\b': 'stage',
        r'\bFase\b': 'Phase',
        r'\bfase\b': 'phase',
    }

    # Apply all replacements
    for portuguese, english in translations.items():
        text = re.sub(portuguese, english, text, flags=re.IGNORECASE)

    return text

def main():
    print("📝 Translating Service Card Portuguese content to English...")

    # Read the HTML file
    with open("01-Service-Card-Dyslexia.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    print("  Processing content...")
    translated_html = translate_portuguese_to_english(html_content)

    # Write back
    with open("01-Service-Card-Dyslexia.html", "w", encoding="utf-8") as f:
        f.write(translated_html)

    print("✅ Service Card translated successfully!")
    print("   File: 01-Service-Card-Dyslexia.html")

if __name__ == "__main__":
    main()
