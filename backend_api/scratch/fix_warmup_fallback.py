import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update warmup questions
old_warmup = """            warmup_options = [
                "How has your day been so far?",
                "Did everything go smoothly getting set up for this session?",
                "Is there anything you need before we move into deeper questions?"
            ]"""

new_warmup = """            warmup_options = [
                "How are you doing today?",
                "How has your day been so far?",
                "Are you feeling ready and excited for our conversation today?",
                "Did everything go smoothly getting set up for this session?",
                "Is there anything you need or any questions you have before we dive in?",
                "How was your day? I hope everything is going great!"
            ]"""

content = content.replace(old_warmup, new_warmup)

# 2. Fix the "Elaborate on..." fallback to be more natural
old_fallback = """            fallback_options = [
                f"Could you elaborate on your experience with {getattr(self, 'current_topic', 'your core technologies')}?",
                f"Can you walk me through a complex problem you solved while working on {getattr(self, 'current_topic', 'your projects')}?",
                "What were the most significant technical challenges you faced in your most recent project?",
                f"How would you approach optimizing the performance of a task related to {getattr(self, 'current_topic', 'your field')}?",
                "Can you tell me more about your recent technical background?"
            ]"""

new_fallback = """            fallback_options = [
                "I'd love to hear more about that. Could you share some more details?",
                "That's interesting. Can you tell me a bit more about your experience in that area?",
                "Got it. What were some of the biggest challenges you faced with that recently?",
                "I see. How do you usually approach solving problems like that?",
                "Tell me more about your background and what you've been working on lately."
            ]"""

content = content.replace(old_fallback, new_fallback)

# 3. Add a check for "Greeting" and "Warm-up" in the fallback so it doesn't say "elaborate on Greeting"
content = content.replace(
    "f\"Could you elaborate on your experience with {getattr(self, 'current_topic', 'your core technologies')}?\"",
    "\"I'd love to hear more about your background. What have you been working on recently?\""
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Warmup questions and fallback logic improved in manager.py.")
