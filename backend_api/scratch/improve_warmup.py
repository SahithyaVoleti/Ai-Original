import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update warmup questions to be more conversational
old_warmup_options = """            warmup_options = [
                "How has your day been so far?",
                "Did everything go smoothly getting set up for this session?",
                "Is there anything you need before we move into deeper questions?"
            ]"""

new_warmup_options = """            warmup_options = [
                "How are you doing today?",
                "How has your day been so far?",
                "How was your day? Hope it's going well!",
                "Are you feeling ready for our conversation today?",
                "Did everything go smoothly getting set up for this session?",
                "Is there anything you need before we move into deeper questions?"
            ]"""

content = content.replace(old_warmup_options, new_warmup_options)

# 2. Fix the "Elaborate on [Topic]" issue by hardening the prompt
# This usually happens in the main prompt construction at the end of generate_question

old_prompt_tail = """            prompt = f\"\"\"
            You are a professional AI Interviewer. 
            Context: {context}
            Instruction: {context_instruction}
            Candidate Resume Context: {resume_for_prompt}
            Recent History: {json.dumps(history_copy[-3:], indent=2)}
            \"\"\""""

# I need to find the actual prompt construction in manager.py
# I'll search for it first.
