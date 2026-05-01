import os
import re

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\manager.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure warmup options are in the EXACT order the user wants
old_warmup = """            warmup_options = [
                "How are you doing today?",
                "How has your day been so far?",
                "Are you feeling ready and excited for our conversation today?",
                "Did everything go smoothly getting set up for this session?",
                "Is there anything you need or any questions you have before we dive in?",
                "How was your day? I hope everything is going great!"
            ]"""

new_warmup = """            warmup_options = [
                "How are you doing today?",
                "How has your day been so far? Hope everything is going great!",
                "Are you feeling ready to start our session?",
                "Did everything go smoothly getting set up today?",
                "Is there anything you need before we dive into the technical questions?"
            ]"""

content = content.replace(old_warmup, new_warmup)

# 2. Make the 'intro' question more varied and styled
old_intro = """        elif category == 'intro':
            context = "Step 3: Self Introduction (MANDATORY)"
            context_instruction = "Ask the candidate: 'Please introduce yourself.' (MANDATORY)"
            self.current_topic = "Self Introduction\""""

new_intro = """        elif category == 'intro':
            context = "Step 4: Self Introduction"
            intro_styles = [
                "Could you please introduce yourself and walk me through your background?",
                "To get us started, I'd love to hear a bit about your journey and what brings you here today.",
                "Why don't we start with a brief introduction? Tell me about yourself and your key experiences.",
                "I've seen your resume, but I'd love to hear your story in your own words. Could you introduce yourself?"
            ]
            style = random.choice(intro_styles)
            context_instruction = f"Ask the candidate to introduce themselves. Use this style: {style}. Keep it professional and welcoming."
            self.current_topic = "Self Introduction\""""

content = content.replace(old_intro, new_intro)

# 3. Simplify Greeting
old_greeting = """            context_instruction = (
                f"Greet {nm} professionally using a time-appropriate opener (good morning, good afternoon, or good evening). "
                f"Then ask exactly ONE short welcoming question—such as how they are doing today or if they feel ready to begin. "
                f"Keep the whole utterance brief and natural."
            )"""

new_greeting = """            context_instruction = (
                f"Say a warm 'Hi' or 'Hello' to {nm}. Include 'Good morning', 'Good afternoon', or 'Good evening' based on the time. "
                f"Keep it very brief, just a greeting. Example: 'Hello {nm}, good morning!'"
            )"""

content = content.replace(old_greeting, new_greeting)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Interview flow sequence and styles updated in manager.py.")
