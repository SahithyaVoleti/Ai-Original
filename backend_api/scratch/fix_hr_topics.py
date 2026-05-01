import os

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add hr_culture to topic_options mapping
if "'hr_culture':" not in content:
    target = "'scenario_hr': [\"Company culture fit\", \"Long-term commitment\", \"Motivation\"],"
    replacement = target + "\n                      'hr_culture': [\"Work-life balance\", \"Team conflict resolution\", \"Ethics and Values\"],"
    content = content.replace(target, replacement)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('HR Culture category added successfully.')
