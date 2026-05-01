import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Summary Table in manager.py to match Screenshot 1
# We need to find where the summary table (sc_tab or similar) is built.
# Looking at the code from previous view (lines 800-1000)

# I'll search for the summary table part
old_summary_tab_logic = """        # --- Candidate Summary Header Table ---
        sum_rows = [
            [safe_para("<b>Candidate Name:</b>", s_bold, True), safe_para(self.candidate_name or "N/A", s_norm, True)],
            [safe_para("<b>Interview Date:</b>", s_bold, True), safe_para(self.start_time.strftime("%B %d, %Y"), s_norm, True)],
            [safe_para("<b>Interview Time:</b>", s_bold, True), safe_para(self.start_time.strftime("%I:%M %p"), s_norm, True)],
            [safe_para("<b>Total Questions Asked:</b>", s_bold, True), safe_para(str(len(evals_copy)), s_norm, True)],
            [safe_para("<b>Security Status:</b>", s_bold, True), safe_para(security_status_text, s_norm, True)]
        ]"""

# I'll check what's actually in the file first to be sure
