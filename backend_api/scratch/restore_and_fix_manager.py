import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Define security_status_text properly in generate_pdf_report
target_def = 'ov_score = (self.calculate_score() / 10.0) if hasattr(self, \'calculate_score\') else 0'
replacement_def = """ov_score = (self.calculate_score() / 10.0) if hasattr(self, 'calculate_score') else 0
        security_status_text = "Clean"
        if any(v.get('severity') == 'CRITICAL' for v in self.violations) or (hasattr(self, 'proctor_score') and self.proctor_score == 0):
            security_status_text = "TERMINATED due to multiple security violations"
        elif self.violations:
            security_status_text = "Warnings Issued\""""

content = content.replace(target_def, replacement_def)

# 2. Update meta_rows to include Security Status
target_meta = '[safe_para("<b>Assessment Status</b>", s_bold, True), safe_para(status_text, s_norm, True)],'
replacement_meta = """[safe_para("<b>Security Status</b>", s_bold, True), safe_para(security_status_text, s_norm, True)],
            [safe_para("<b>Assessment Status</b>", s_bold, True), safe_para(status_text, s_norm, True)],"""

content = content.replace(target_meta, replacement_meta)

# 3. Add the Rubric Assessment and Final Recommendation sections correctly
# Find the place before interaction log
target_insertion = "        # --- Interaction log (reference-style) ---"

new_sections = """        # --- FINAL RECOMMENDATION SECTION (Screenshot 3) ---
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
        story.append(gap_md)

        # --- Performance scorecard (neat 2x2) ---
        sc_val = ParagraphStyle('ScVal', fontSize=16, textColor=C_MAIN, fontName='Helvetica-Bold', alignment=TA_CENTER)
        sc_sub = ParagraphStyle('ScSub', fontSize=7, textColor=C_MUTED, fontName='Helvetica', alignment=TA_CENTER)
        card = [
            [safe_para(f"{ov_score:.1f}", sc_val), safe_para(f"{avg_corr:.1f}", sc_val), safe_para(f"{avg_fluency:.1f}", sc_val), safe_para(f"{proctor_pct:.0f}%", sc_val)],
            [safe_para("OVERALL PERFORMANCE", sc_sub), safe_para("TECH ACCURACY", sc_sub), safe_para("COMM. SCORE", sc_sub), safe_para("TRUST / INTEGRITY", sc_sub)]
        ]
        sc_tab = Table(card, colWidths=[1.77 * inch] * 4)
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
        story.append(KeepTogether([safe_para("PERFORMANCE SCORECARD", s_head), sc_tab]))
        story.append(gap_md)
        
        # --- COMMUNICATION & GRAMMAR ANALYSIS ---
        story.append(CondPageBreak(2.0 * inch))
        story.append(safe_para("COMMUNICATION & GRAMMAR ANALYSIS", s_head))
        grammar_text = f"Analysis of Grammatical Accuracy and Fluency:<br/>• The candidate's communication score is {avg_comm:.1f}/10.<br/>• Grammatical usage was evaluated at {avg_grammar:.1f}/10.<br/>• The candidate's fluency and structural delivery indicate a {_band(avg_comm)} level of communication."
        story.append(safe_para(grammar_text, s_norm, True))
        story.append(gap_md)

        # --- Proctoring & Integrity Report Header (Screenshot 4) ---
        story.append(CondPageBreak(3.0 * inch))
        story.append(safe_para("PROCTORING & INTEGRITY REPORT", s_head))
        status_color_lbl = 'green' if proctor_pct > 80 else 'red'
        status_label_lbl = 'LOW' if proctor_pct > 80 else 'HIGH'
        story.append(safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color='{status_color_lbl}'>{status_label_lbl}</font>", s_norm, True))
        story.append(gap_md)

        # --- Session Monitoring Log Header (Screenshot 5) ---
        story.append(safe_para("SESSION MONITORING LOG", s_head))
        story.append(safe_para("The following images were captured during the session for identity verification and proctoring purposes:", s_small))
        
"""

content = content.replace(target_insertion, new_sections + target_insertion)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Manager.py restored and updated with correct report logic.")
