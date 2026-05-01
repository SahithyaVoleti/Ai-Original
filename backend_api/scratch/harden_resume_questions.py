import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Stop overwriting resume topics in technical_advanced
old_advanced_logic = """            if 'advanced' in category:
                all_topics = ["System Architecture", "Performance Optimization", "Scalability Patterns", "Security Best Practices", "Distributed Systems"]"""

new_advanced_logic = """            if 'advanced' in category:
                # Append advanced topics instead of overwriting, so resume topics remain
                all_topics.extend(["System Architecture", "Performance Optimization", "Scalability Patterns", "Security Best Practices", "Distributed Systems"])"""

content = content.replace(old_advanced_logic, new_advanced_logic)

# Fix 2: Increase the weight of resume-specific items in the prompt
old_tech_instruction = 'context_instruction = f"Generate a unique technical question about: {topic_to_ask}. DO NOT ask for a general \'tell me about your background\'. Ask a specific \'How would you...\' or \'Explain a time...\' question."'
new_tech_instruction = 'context_instruction = f"Generate a deep technical question about {topic_to_ask} strictly based on the candidate\'s background as listed in their RESUME. If the topic is a project or skill from their CV, ask about specific implementation details, challenges, or architectural choices they made. Ensure the question feels personalized to THEIR experience, not generic."'

content = content.replace(old_tech_instruction, new_tech_instruction)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Resume-grounded question generation hardened in manager.py.")
