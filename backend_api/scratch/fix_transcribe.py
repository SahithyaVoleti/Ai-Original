import os

path = r'd:\AI_interviews_new\AI_Interview-main\backend_api\api.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add transcribe route before generate_video
transcribe_route = """
@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    \"\"\"High-accuracy audio transcription using OpenAI Whisper.\"\"\"
    try:
        if 'audio' not in request.files:
            return jsonify({"status": "error", "message": "No audio file provided"}), 400
        
        audio_file = request.files['audio']
        temp_path = os.path.join(current_dir, "temp_answer.webm")
        audio_file.save(temp_path)
        
        # Use manager's client (OpenAI) for transcription
        if hasattr(manager, 'client') and manager.client:
            with open(temp_path, "rb") as audio:
                transcript = manager.client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio,
                    language="en"
                )
                text = transcript.text
                print(f"✨ Whisper Transcription: {text[:50]}...")
                
                try: os.remove(temp_path)
                except: pass
                
                return jsonify({"status": "success", "transcript": text})
        else:
            return jsonify({"status": "error", "message": "Transcription service unavailable"}), 500
            
    except Exception as e:
        print(f"❌ Transcription Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
"""

if '/api/transcribe' not in content:
    content = content.replace("@app.route('/api/generate_video'", transcribe_route + "\n@app.route('/api/generate_video'")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Transcription route added to api.py successfully.")
