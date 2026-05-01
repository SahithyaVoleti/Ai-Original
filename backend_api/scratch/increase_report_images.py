import os

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Increase screenshot capacity for all plans
old_cap = 'tier_ev_cap = {0: 4, 1: 6, 2: 10, 3: 12, 4: 15}'
new_cap = 'tier_ev_cap = {0: 10, 1: 12, 2: 15, 3: 18, 4: 20}'

content = content.replace(old_cap, new_cap)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Screenshot capacity increased in PDF report.")
