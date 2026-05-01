import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new flow
new_flow = """        return [
            "greeting",
            "warmup",
            "intro",
            "scenario_behavioral",
            "scenario_technical",
            "resume_skills",
            "resume_projects",
            "resume_overview",
            "technical_core",
            "technical_advanced",
            "case_study",
            "scenario_hr",
            "behavioral",
            "code",
            "code",
            "hr_culture",
            "leadership",
            "teamwork",
            "adaptability",
            "future_goals",
            "conclusion"
        ]"""

# Find and replace the _get_default_flow content
pattern = r'def _get_default_flow\(self, plan_id=0\):.*?return \[.*?\]'
content = re.sub(pattern, 'def _get_default_flow(self, plan_id=0):\n        \"\"\"Standard full flow: Optimized with more Scenario and HR rounds.\"\"\"\n' + new_flow, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Interview flow updated successfully.")
