import os

# Root path for shared static files
ROOT_DIR = r'd:\AI_interviews_new\AI_Interview-main'
SHARED_STATIC = os.path.join(ROOT_DIR, 'static', 'proctor_evidence')

# 1. Update manager.py
manager_path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(manager_path, 'r', encoding='utf-8') as f:
    m_content = f.read()

target_m = 'scan_dir = os.path.join(os.getcwd(), "evidence")'
replacement_m = f'scan_dir = r"{SHARED_STATIC}"'
m_content = m_content.replace(target_m, replacement_m)

with open(manager_path, 'w', encoding='utf-8') as f:
    f.write(m_content)

# 2. Update service.py
service_path = r'd:\AI_interviews_new\AI_Interview-main\backend_worker\proctoring_engine\service.py'
with open(service_path, 'r', encoding='utf-8') as f:
    s_content = f.read()

target_s = 'self.evidence_path = os.path.join(os.getcwd(), "static", "proctor_evidence")'
replacement_s = f'self.evidence_path = r"{SHARED_STATIC}"'
s_content = s_content.replace(target_s, replacement_s)

with open(service_path, 'w', encoding='utf-8') as f:
    f.write(s_content)

# 3. Create directory
if not os.path.exists(SHARED_STATIC):
    os.makedirs(SHARED_STATIC, exist_ok=True)

print(f"Evidence path synchronized to shared location: {SHARED_STATIC}")
