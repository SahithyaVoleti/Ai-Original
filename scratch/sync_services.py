import shutil
import os

api_dir = r'd:\AI_interviews_new\AI_Interview-main\backend_api'
worker_dir = r'd:\AI_interviews_new\AI_Interview-main\backend_worker'

# 1. Sync manager.py (from api to worker)
shutil.copy2(os.path.join(api_dir, 'manager.py'), os.path.join(worker_dir, 'manager.py'))

# 2. Sync proctoring_engine/service.py (from worker to api - assuming worker has the hardened logic)
# Wait, let's check which one is newer or has the logic.
# I updated worker earlier.
shutil.copy2(os.path.join(worker_dir, 'proctoring_engine', 'service.py'), os.path.join(api_dir, 'proctoring_engine', 'service.py'))

# 3. Sync other critical files
files_to_sync = ['app_config.py', 'database.py', 'text_to_speech.py']
for f in files_to_sync:
    shutil.copy2(os.path.join(api_dir, f), os.path.join(worker_dir, f))

print("Services synchronized successfully.")
