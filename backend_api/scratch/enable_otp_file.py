import os

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\.env'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

updated = False
with open(path, 'w', encoding='utf-8') as f:
    for line in lines:
        if line.startswith('ENABLE_OTP_FILE='):
            f.write('ENABLE_OTP_FILE=true\n')
            updated = True
        else:
            f.write(line)
    if not updated:
        f.write('\nENABLE_OTP_FILE=true\n')

print("ENABLE_OTP_FILE set to true in .env")
