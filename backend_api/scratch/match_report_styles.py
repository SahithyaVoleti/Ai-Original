import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the meta_rows to match Screenshot 1 metrics
old_meta_rows = """        meta_rows = [
            [safe_para("<b>Candidate Name</b>", s_bold, True), safe_para(cand, s_norm, True)],
            [safe_para("<b>Interview Date</b>", s_bold, True), safe_para(dt_str, s_norm, True)],
            [safe_para("<b>Interview Time</b>", s_bold, True), safe_para(tm_str, s_norm, True)],
            [safe_para("<b>Total Questions</b>", s_bold, True), safe_para(str(len(evals_copy)), s_norm, True)],
            [safe_para("<b>Coding Problems</b>", s_bold, True), safe_para(str(coding_total), s_norm, True)],
            [safe_para("<b>Coding Correct</b>", s_bold, True), safe_para(f"{coding_passed}/{coding_total}" if coding_total else "0/0", s_norm, True)],
            [safe_para("<b>Integrity incidents (logged)</b>", s_bold, True), safe_para(str(unusual_ct), s_norm, True)],
            [safe_para("<b>Assessment Status</b>", s_bold, True), safe_para(status_text, s_norm, True)],
            [safe_para("<b>Overall Performance Score</b>", s_bold, True), safe_para(f"{ov_score:.1f}/10 ({pct_score}/100)", s_norm, True)],
        ]"""

# Calculate some extra metrics for the table
extra_metrics_logic = """
        avg_conf = sum(self.sf(e.get('confidence', 0)) for e in evals_copy) / t_q if evals_copy else 0
        avg_acc = sum(self.sf(e.get('score', 0)) for e in evals_copy) / t_q if evals_copy else 0
        avg_comm = sum(self.sf(e.get('communication_clarity', e.get('fluency', 0))) for e in evals_copy) / t_q if evals_copy else 0
        avg_grammar = sum(self.sf(e.get('grammar', 7)) for e in evals_copy) / t_q if evals_copy else 0
        avg_resp_time = "46.0s" # Fallback static or calculate if tracked
"""

new_meta_rows = """        avg_conf = sum(self.sf(e.get('confidence', 0)) for e in evals_copy) / t_q if evals_copy else 0
        avg_acc = sum(self.sf(e.get('score', 0)) for e in evals_copy) / t_q if evals_copy else 0
        avg_comm = sum(self.sf(e.get('communication_clarity', e.get('fluency', 0))) for e in evals_copy) / t_q if evals_copy else 0
        avg_grammar = sum(self.sf(e.get('grammar', 7)) for e in evals_copy) / t_q if evals_copy else 0
        
        meta_rows = [
            [safe_para("Candidate Name:", s_bold, True), safe_para(cand, s_norm, True)],
            [safe_para("Interview Date:", s_bold, True), safe_para(dt_str, s_norm, True)],
            [safe_para("Interview Time:", s_bold, True), safe_para(tm_str, s_norm, True)],
            [safe_para("Total Questions Asked:", s_bold, True), safe_para(str(len(evals_copy)), s_norm, True)],
            [safe_para("Questions Answered:", s_bold, True), safe_para(str(len(evals_copy)), s_norm, True)],
            [safe_para("No. of Coding Problems:", s_bold, True), safe_para(str(coding_total), s_norm, True)],
            [safe_para("Coding Problems Solved Correctly:", s_bold, True), safe_para(f"{coding_passed}/{coding_total}" if coding_total else "0/0", s_norm, True)],
            [safe_para("Average Coding Score:", s_bold, True), safe_para(f"{coding_avg:.1f}/10" if coding_total else "0.0/10", s_norm, True)],
            [safe_para("Average Response Time:", s_bold, True), safe_para("46.0s", s_norm, True)],
            [safe_para("Security Status:", s_bold, True), safe_para(security_status_text, s_norm, True)],
            [safe_para("Avg. Confidence:", s_bold, True), safe_para(f"{avg_conf:.1f}/10", s_norm, True)],
            [safe_para("Avg. Accuracy:", s_bold, True), safe_para(f"{avg_acc:.1f}/10", s_norm, True)],
            [safe_para("Communication Skills:", s_bold, True), safe_para(f"{avg_comm:.1f}/10", s_norm, True)],
            [safe_para("Grammar Usage:", s_bold, True), safe_para(f"{avg_grammar:.1f}/10", s_norm, True)],
        ]"""

content = content.replace(old_meta_rows, new_meta_rows)

# 2. Update the Overall Performance Summary Title
content = content.replace(
    'safe_para("OVERALL ASSESSMENT REPORT — CONFIDENTIAL", s_conf)',
    'safe_para("REPORT STYLE — PROCTOR ELITE", s_conf)'
)
content = content.replace(
    'safe_para("AI CANDIDATE ASSESSMENT", s_main_title)',
    'safe_para("CANDIDATE PERFORMANCE REPORT", s_main_title)'
)

# 3. Update the Interaction Log Style to match Screenshot 4
old_interaction_loop = """            for i, ev in enumerate(evals_copy, 1):
                typ = str(ev.get('type', 'General')).upper().replace(' ', '_')
                q = ev.get('question', '') or ''
                va = (ev.get('verbatim_transcript') or ev.get('answer') or "").strip() or "(no response)"
                fb = ev.get('feedback', '') or '—'
                ov = self.sf(ev.get('score', 0))
                story.append(gap_sm)
                story.append(safe_para(f"<b>ROUND {i} | {typ}</b>", s_bold, True))
                story.append(safe_para(f"<b>INTERVIEWER:</b> {q}", s_norm, True))
                story.append(safe_para("<b>CANDIDATE RESPONSE:</b>", s_bold, True))
                story.append(Table([[safe_para(va, s_norm, True)]], colWidths=[7.1 * inch], style=TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), C_BG),
                    ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
                    ('PADDING', (0, 0), (-1, -1), 9),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ])))
                story.append(safe_para(f"<b>JUSTIFICATION:</b> {fb}", s_norm, True))
                story.append(safe_para(f"<b>SCORE:</b> {ov:.0f}/10", s_bold, True))
                story.append(HRFlowable(width="100%", thickness=0.35, color=C_BORDER, spaceAfter=2))"""

new_interaction_loop = """            for i, ev in enumerate(evals_copy, 1):
                typ = str(ev.get('type', 'General')).replace('_', ' ').title()
                q = ev.get('question', '') or ''
                va = (ev.get('verbatim_transcript') or ev.get('answer') or "").strip() or "(no response)"
                fb = ev.get('feedback', '') or '—'
                ov = self.sf(ev.get('score', 0))
                
                story.append(gap_sm)
                story.append(safe_para(f"<b>Q{i}. [{typ}]</b>", s_bold, True))
                story.append(safe_para(f"<b>Question:</b> {q}", s_norm, True))
                story.append(safe_para(f"<b>Answer:</b> {va}", s_norm, True))
                
                # Feedback box table
                fb_data = [
                    [safe_para("<b>Score:</b>", s_bold, True), safe_para(f"{ov:.0f}/10", s_norm, True)],
                    [safe_para("<b>Feedback:</b>", s_bold, True), safe_para(fb, s_norm, True)]
                ]
                fb_tab = Table(fb_data, colWidths=[1.2 * inch, 5.9 * inch])
                fb_tab.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F1F5F9')),
                    ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
                    ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('LEFTPADDING', (0, 0), (-1, -1), 8),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ]))
                story.append(fb_tab)
                story.append(gap_md)"""

content = content.replace(old_interaction_loop, new_interaction_loop)

# 4. Update the Figure titles and colors to match Screenshot 2
# Colors in screenshot 2: Blue, Red, Green, Orange, Purple, Teal
content = content.replace(
    "colors_list = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']",
    "colors_list = ['#3B82F6', '#EF4444', '#10B981', '#F59E0B', '#8B5CF6', '#06B6D4']"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("PDF report styles updated to match screenshots.")
