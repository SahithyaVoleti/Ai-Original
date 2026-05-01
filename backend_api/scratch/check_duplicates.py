import re
import collections

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\api.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all routes (handling single/double quotes)
routes = re.findall(r"@app\.route\(['\"]([^'\"]+)['\"]", content)
# Find all function definitions (handling arguments)
functions = re.findall(r"def (\w+)\(.*\):", content)

route_counts = collections.Counter(routes)
func_counts = collections.Counter(functions)

print("Duplicate Routes:")
for route, count in route_counts.items():
    if count > 1:
        print(f"  {route}: {count}")

print("\nDuplicate Functions (Global):")
for func, count in func_counts.items():
    if count > 1:
        print(f"  {func}: {count}")
