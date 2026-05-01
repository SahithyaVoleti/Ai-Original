import os

path = r'd:\AI_interviews_new\AI_Interview-main\frontend\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the MANUAL INPUT OPTION block
import re
pattern = r'\s*{\/\* MANUAL INPUT OPTION \*\/}.*?Submit Answer.*?<\/div>\s*<\/div>\s*<\/div>\s*}\)'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# Re-check the structure
if 'MANUAL INPUT OPTION' in content:
    # Fallback simpler removal
    start_marker = '{/* MANUAL INPUT OPTION */}'
    end_marker = '<div className="bg-indigo-50 py-3 mx-4 mb-2 rounded-xl text-center">'
    if start_marker in content and end_marker in content:
        parts = content.split(start_marker)
        rest = parts[1].split(end_marker)
        content = parts[0] + end_marker + rest[1]

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Manual typing box removed. Voice-only mode restored.")
