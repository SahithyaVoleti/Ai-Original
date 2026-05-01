import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new flow matching the user's specific request
new_flow = """        return [
            "greeting",
            "warmup",
            "warmup",
            "intro",
            "resume_projects",
            "scenario_behavioral",
            "scenario_technical",
            "scenario_hr",
            "hr_culture",
            "technical_core",
            "technical_advanced",
            "case_study",
            "code",
            "code",
            "leadership",
            "teamwork",
            "conclusion"
        ]"""

# Find and replace the _get_default_flow content
pattern = r'def _get_default_flow\(self, plan_id=0\):.*?return \[.*?\]'
content = re.sub(pattern, 'def _get_default_flow(self, plan_id=0):\n        \"\"\"Standard full flow: Greeting -> 2 General -> Intro -> Projects -> Scenarios -> HR -> Tech.\"\"\"\n' + new_flow, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Interview flow updated in manager.py successfully.")
