import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Performance Scorecard to use BOXES (Screenshot 2)
old_scorecard_logic = """        # --- Performance scorecard table ---
        sc_rows = [
            [safe_para("OVERALL SCORE", s_small), safe_para("TECH ACCURACY", s_small), safe_para("COMM. SCORE", s_small), safe_para("TRUST ASST.", s_small)],
            [safe_para(f"<b>{ov_score:.1f}/10</b>", s_main_title, True), safe_para(f"<b>{avg_corr:.1f}/10</b>", s_main_title, True), safe_para(f"<b>{avg_comm:.1f}/10</b>", s_main_title, True), safe_para(f"<b>{proctor_pct:.0f}%</b>", s_main_title, True)]
        ]
        sc_tab = Table(sc_rows, colWidths=[1.75 * inch] * 4)
        sc_tab.setStyle(TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.75, C_BORDER),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
            ('BACKGROUND', (0, 0), (-1, -1), C_BG),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(KeepTogether([safe_para("PERFORMANCE SCORECARD", s_head), sc_tab]))"""

new_scorecard_logic = """        # --- Performance scorecard boxes ---
        sc_rows = [
            [
                Table([[safe_para(f"<b>{ov_score:.1f}</b>", s_main_title, True)], [safe_para("OVERALL PERFORMANCE", s_small)]], colWidths=[1.55*inch]),
                Table([[safe_para(f"<b>{avg_corr:.1f}</b>", s_main_title, True)], [safe_para("TECH ACCURACY", s_small)]], colWidths=[1.55*inch]),
                Table([[safe_para(f"<b>{avg_comm:.1f}</b>", s_main_title, True)], [safe_para("COMM. SCORE", s_small)]], colWidths=[1.55*inch]),
                Table([[safe_para(f"<b>{proctor_pct:.0f}%</b>", s_main_title, True)], [safe_para("TRUST ASST.", s_small)]], colWidths=[1.55*inch])
            ]
        ]
        sc_tab = Table(sc_rows, colWidths=[1.75 * inch] * 4)
        sc_tab.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        # Style individual boxes
        for i in range(4):
            sc_tab.getStyle().add('BOX', (i, 0), (i, 0), 1, C_BORDER)
            sc_tab.getStyle().add('BACKGROUND', (i, 0), (i, 0), C_BG)

        story.append(KeepTogether([safe_para("PERFORMANCE SCORECARD", s_head), sc_tab]))"""

content = content.replace(old_scorecard_logic, new_scorecard_logic)

# 2. Add Executive Summary block (Screenshot 2)
# I'll insert it before the scorecard
summary_insertion = """
        # --- EXECUTIVE SUMMARY BLOCK ---
        story.append(safe_para("EXECUTIVE SUMMARY", s_head))
        summary_box_data = [[safe_para(f"<b>Conclusion:</b> {ai_summary}", s_norm, True)]]
        summary_box_tab = Table(summary_box_data, colWidths=[7.1 * inch])
        summary_box_tab.setStyle(TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
            ('BACKGROUND', (0, 0), (-1, -1), C_BG),
            ('PADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(summary_box_tab)
        story.append(gap_md)
"""

# Find where to insert - before scorecard
content = content.replace('story.append(KeepTogether([safe_para("PERFORMANCE SCORECARD", s_head), sc_tab]))', 
                         summary_insertion + '        story.append(KeepTogether([safe_para("PERFORMANCE SCORECARD", s_head), sc_tab]))')

# 3. Update Skills Assessment Table (Screenshot 1 & 2)
# Assessment labels: "Good", "Needs Improvement", "Critical", "Average"
old_band_logic = """        def _band(avg):
            if avg is None or avg <= 0:
                return "NOT ATTEMPTED"
            if avg < 3:
                return "CRITICAL"
            if avg < 5:
                return "NEEDS IMPROVEMENT"
            if avg < 6.5:
                return "AVERAGE"
            if avg < 8:
                return "GOOD"
            return "STRONG\""""

new_band_logic = """        def _band(avg):
            if avg is None or avg <= 0:
                return "Not Attempted"
            if avg < 3.5:
                return "Critical"
            if avg < 5.5:
                return "Needs Improvement"
            if avg < 7.0:
                return "Average"
            if avg < 8.5:
                return "Good"
            return "Excellent\""""

content = content.replace(old_band_logic, new_band_logic)

# 4. Add "COMMUNICATION & GRAMMAR ANALYSIS" section (Screenshot 4)
grammar_analysis_section = """
        # --- COMMUNICATION & GRAMMAR ANALYSIS ---
        story.append(CondPageBreak(2.0 * inch))
        story.append(safe_para("COMMUNICATION & GRAMMAR ANALYSIS", s_head))
        grammar_text = f"Analysis of Grammatical Accuracy and Fluency:<br/>• The candidate's communication score is {avg_comm:.1f}/10.<br/>• Grammatical usage was evaluated at {avg_grammar:.1f}/10.<br/>• The candidate's fluency and structural delivery indicate a {_band(avg_comm)} level of communication."
        story.append(safe_para(grammar_text, s_norm, True))
        story.append(gap_md)
"""

# Insert before interaction log
content = content.replace("# --- Interaction log (reference-style) ---", grammar_analysis_section + "        # --- Interaction log (reference-style) ---")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("PDF report fields and layouts refined to match screenshots.")
