import os

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Final Recommendation Section
# Using a simpler find/replace to avoid variable definition errors in the scratch script
target_insertion = """        # --- EXECUTIVE SUMMARY BLOCK ---
        story.append(safe_para("EXECUTIVE SUMMARY", s_head))
        summary_box_data = [[safe_para(f"<b>Conclusion:</b> {ai_summary}", s_norm, True)]]
        summary_box_tab = Table(summary_box_data, colWidths=[7.1 * inch])
        summary_box_tab.setStyle(TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
            ('BACKGROUND', (0, 0), (-1, -1), C_BG),
            ('PADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(summary_box_tab)
        story.append(gap_md)"""

replacement_logic = """        # --- FINAL RECOMMENDATION SECTION (Screenshot 3) ---
        story.append(CondPageBreak(3.0 * inch))
        story.append(safe_para("FINAL RECOMMENDATION", s_head))
        
        # Executive Summary
        story.append(safe_para("<b>Executive Summary:</b>", s_norm, True))
        story.append(safe_para(ai_summary, s_norm))
        story.append(gap_md)
        
        # Areas for Improvement
        if improvements:
            story.append(safe_para("<b>Areas for Improvement:</b>", s_norm, True))
            for imp in improvements:
                story.append(safe_para(f"• {imp}", s_norm))
            story.append(gap_md)
            
        # Remarks & Next Steps
        if next_steps:
            story.append(safe_para("<b>Remarks & Next Steps:</b>", s_norm, True))
            for ns in next_steps:
                story.append(safe_para(f"• {ns}", s_norm))
            story.append(gap_md)

        # INTERVIEW RUBRIC ASSESSMENT (Screenshot 3)
        story.append(safe_para("INTERVIEW RUBRIC ASSESSMENT", s_head))
        
        factors = [
            ("Cultural Fit", 3, "Neutral fit; acceptable but not distinctive."),
            ("Career Motivation", 4, "Clear articulation of goals and interest."),
            ("Social Skills", 5, "Excellent eye contact and engagement."),
            ("Teamwork", 3, "Adequate potential for collaboration."),
            ("Technical Skills", 1, "No technical skills demonstrated."),
            ("Leadership Capabilities", 3, "Not fully assessed in this session format."),
            ("Critical Thinking / Problem Solving", 3, "Standard problem solving approach."),
            ("Self-Awareness", 4, "Good understanding of own strengths/weaknesses.")
        ]
        
        rubric_rows = [[safe_para("<b>FACTORS</b>", s_bold, True), safe_para("<b>Candidate Score (1-5)</b>", s_bold, True), safe_para("<b>Assessment Notes</b>", s_bold, True)]]
        total_r_score = 0
        for f_name, f_base, f_note in factors:
            dynamic_score = f_base
            if f_name == "Technical Skills":
                dynamic_score = max(1, min(5, int(avg_corr / 2)))
                f_note = "High technical proficiency." if dynamic_score >= 4 else "Moderate technical knowledge." if dynamic_score >= 3 else "Technical gaps identified."
            elif f_name == "Social Skills":
                dynamic_score = max(1, min(5, int(avg_comm / 2)))
            
            rubric_rows.append([safe_para(f_name, s_norm), safe_para(str(dynamic_score), s_norm, True), safe_para(f_note, s_small)])
            total_r_score += dynamic_score
            
        avg_r_score = total_r_score / len(factors)
        rubric_rows.append([safe_para("<b>AVERAGE SCORE</b>", s_bold, True), safe_para(f"<b>{avg_r_score:.2f}</b>", s_bold, True), safe_para("", s_norm)])
        
        rubric_tab = Table(rubric_rows, colWidths=[2.2 * inch, 1.4 * inch, 3.5 * inch])
        rubric_tab.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), C_BG),
            ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(rubric_tab)
        story.append(gap_md)"""

content = content.replace(target_insertion, replacement_logic)

# 2. Update Proctoring & Integrity Report Header
content = content.replace(
    'safe_para("PROCTORING & FIDELITY LOG", s_head)',
    'safe_para("PROCTORING & INTEGRITY REPORT", s_head)'
)
# Use a string that includes variables that will be present in manager.py at runtime
content = content.replace(
    'safe_para("Session-captured frames tied to monitoring events (all subscription tiers).", s_small)',
    'safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color=\'{\\"green\\" if proctor_pct > 80 else \\"red\\"}\'>{\\"LOW\\" if proctor_pct > 80 else \\"HIGH\\"}</font>", s_norm, True)'
)

# 3. Add Session Monitoring Log Header
content = content.replace(
    'ev_lbl_style = ParagraphStyle(',
    'story.append(CondPageBreak(3.0 * inch))\n            story.append(safe_para("SESSION MONITORING LOG", s_head))\n            story.append(safe_para("The following images were captured during the session for identity verification and proctoring purposes:", s_small))\n            ev_lbl_style = ParagraphStyle('
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("PDF report finalized successfully.")
