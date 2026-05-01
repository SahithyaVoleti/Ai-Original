import os

path = r'd:\AI_interviews_new\AI_Interview-main\frontend\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '---TEMP---' in line:
        # We found the junk part. We need to stop the double closing.
        # Looking at the context, we should stop here and skip the next few redundant lines.
        skip = True
        # Keep the '</div>' part of the line if it was meant to be there, but remove junk
        new_lines.append('                </div>\n')
        continue
    
    if skip:
        # These are the redundant lines:
        #       </div>
        #     )}
        #   </div>
        if 'bg-indigo-50' in line:
            skip = False # Resume here
            new_lines.append(line)
        else:
            continue
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Syntax error in page.tsx fixed.")
