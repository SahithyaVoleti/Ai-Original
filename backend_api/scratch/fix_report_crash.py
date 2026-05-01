import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up duplicate sections and simplify card table
# Remove the old Executive Summary block (lines 967-983 roughly)
old_sum_block = """        # --- Executive summary ---
        story.append(safe_para("EXECUTIVE SUMMARY", s_head))
        sum_tab = Table([[safe_para(ai_summary, s_norm)]], colWidths=[7.1 * inch])
        sum_tab.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), C_WHITE),
            ('BOX', (0, 0), (-1, -1), 0.75, C_BORDER),
            ('PADDING', (0, 0), (-1, -1), 11),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(
            KeepTogether(
                [
                    safe_para(hire_line, s_bold, True),
                    gap_sm,
                    sum_tab,
                ]
            )
        )"""

content = content.replace(old_sum_block, "")

# 2. Fix the scorecard table (Simplified layout)
old_card_logic = """        card = [
            [
                Table([[safe_para(f"{ov_score:.1f}", sc_val), safe_para("OVERALL PERFORMANCE", sc_sub)]], colWidths=[2.9 * inch]),
                Table([[safe_para(f"{avg_corr:.1f}", sc_val), safe_para("TECH ACCURACY", sc_sub)]], colWidths=[2.9 * inch]),
            ],
            [
                Table([[safe_para(f"{avg_fluency:.1f}", sc_val), safe_para("COMM. SCORE", sc_sub)]], colWidths=[2.9 * inch]),
                Table([[safe_para(f"{proctor_pct:.0f}%", sc_val), safe_para("TRUST / INTEGRITY", sc_sub)]], colWidths=[2.9 * inch]),
            ],
        ]"""

new_card_logic = """        card = [
            [safe_para(f"{ov_score:.1f}", sc_val), safe_para(f"{avg_corr:.1f}", sc_val), safe_para(f"{avg_fluency:.1f}", sc_val), safe_para(f"{proctor_pct:.0f}%", sc_val)],
            [safe_para("OVERALL PERFORMANCE", sc_sub), safe_para("TECH ACCURACY", sc_sub), safe_para("COMM. SCORE", sc_sub), safe_para("TRUST / INTEGRITY", sc_sub)]
        ]"""

content = content.replace(old_card_logic, new_card_logic)
content = content.replace('sc_tab = Table(card, colWidths=[3.55 * inch, 3.55 * inch])', 'sc_tab = Table(card, colWidths=[1.77 * inch] * 4)')

# 3. Add error logging to doc.build
old_build = """        try:
            doc.build(story)
        finally:"""

new_build = """        try:
            doc.build(story)
        except Exception as build_err:
            print(f"[PDF ERROR] doc.build failed: {build_err}")
            import traceback
            traceback.print_exc()
            return False
        finally:"""

content = content.replace(old_build, new_build)

# 4. Clean up non-ASCII characters in formatting
content = content.replace("—", "-")
content = content.replace("?", "-")
content = content.replace("o", "")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("PDF report logic simplified and error logging added.")
