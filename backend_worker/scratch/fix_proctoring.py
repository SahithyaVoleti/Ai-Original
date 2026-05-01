import os

path = r'd:\AI_interviews_new\AI_Interview-main\backend_worker\proctoring_engine\service.py'
if not os.path.exists(path):
    print(f"Error: Path {path} not found")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update termination logic in process_frame
# Gadget termination
content = content.replace(
    'if self.gadget_strike_count >= 3:',
    'if self.gadget_strike_count >= 3:\n                            self.should_terminate = True'
)
# Identity mismatch termination (3 strikes instead of 15)
content = content.replace(
    'if self.identity_mismatch_counts >= 15:',
    'if self.identity_mismatch_counts >= 3:\n                                    self.should_terminate = True'
)
# Face missing termination (3 strikes)
content = content.replace(
    'self.record_event("FACE_MISSING", f"Strike ({self.no_face_strike_count}/3): Candidate not visible for 30s.", "HIGH", frame)',
    'self.record_event("FACE_MISSING", f"Strike ({self.no_face_strike_count}/3): Candidate not visible for 30s.", "HIGH", frame)\n                    if self.no_face_strike_count >= 3:\n                        self.should_terminate = True\n                        self.termination_reason = "Repeated absence from camera frame."'
)

# Fix formatting/quotes if needed
content = content.replace('dY"', '🚨')
content = content.replace('s,?', '⚠️')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Proctoring service hardened successfully.")
