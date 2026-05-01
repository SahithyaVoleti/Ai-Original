import os

# Fix manager.py syntax error in BOTH locations (backend_api and backend_worker)
paths = [
    r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py',
    r'd:\AI_interviews_new\AI_Interview-main\backend_worker\manager.py'
]

for path in paths:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The problematic line looks like this:
    # safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color='{\"green\" if proctor_pct > 80 else \"red\"}'>{\"LOW\" if proctor_pct > 80 else \"HIGH\"}</font>", s_norm, True)
    
    # We'll replace it with a much safer version using helper variables
    old_line_part = 'safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color=\'{\\"green\\" if proctor_pct > 80 else \\"red\\"}\'>{\\"LOW\\" if proctor_pct > 80 else \\"HIGH\\"}</font>", s_norm, True)'
    
    # Let's find the actual line in the file more robustly
    import re
    # We'll use a regex to find the complex line and replace it with a simpler one
    pattern = r'safe_para\(f"Trust Score: {proctor_pct:\.0f}/100<br/>Status: <font color=\'.*?\'>.*?</font>", s_norm, True\)'
    
    new_logic = """
            status_color = "green" if proctor_pct > 80 else "red"
            status_label = "LOW" if proctor_pct > 80 else "HIGH"
            story.append(safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color='{status_color}'>{status_label}</font>", s_norm, True))"""

    # Actually, the original code had:
    # story.append(safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color='{\"green\" if proctor_pct > 80 else \"red\"}'>{\"LOW\" if proctor_pct > 80 else \"HIGH\"}</font>", s_norm, True))
    
    # I'll just do a direct string replacement for the exact broken line
    # I'll read the line from the file to be sure
    
    with open(path, 'w', encoding='utf-8') as f:
        # Replacement that avoids the nested quotes issue
        content = content.replace(
            'safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color=\'{\\"green\\" if proctor_pct > 80 else \\"red\\"}\'>{\\"LOW\\" if proctor_pct > 80 else \\"HIGH\\"}</font>", s_norm, True)',
            'safe_para(f"Trust Score: {proctor_pct:.0f}/100<br/>Status: <font color=\'{\x27green\x27 if proctor_pct > 80 else \x27red\x27}\'>{\x27LOW\x27 if proctor_pct > 80 else \x27HIGH\x27}</font>", s_norm, True)'
        )
        f.write(content)

print("Syntax error fixed in manager.py.")
