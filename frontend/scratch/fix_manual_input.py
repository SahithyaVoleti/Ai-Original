import os

path = r'd:\AI_interviews_new\AI_Interview-main\frontend\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target location: after transcriptEndRef
insertion_point = '<div ref={transcriptEndRef} className="h-0 w-0" />'
manual_input_html = """                        <div ref={transcriptEndRef} className="h-0 w-0" />
                      </div>
                    )}
                  </div>

                  {/* MANUAL INPUT OPTION */}
                  {(stage === 'interview' && !isSpeaking) && (
                    <div className="px-6 pb-4">
                      <div className="relative group">
                        <textarea
                          value={transcript}
                          onChange={(e) => setTranscript(e.target.value)}
                          placeholder="Type your answer here if voice is not working..."
                          className="w-full h-24 p-4 bg-slate-50 border border-slate-200 rounded-3xl text-sm focus:ring-4 focus:ring-indigo-500/10 focus:border-indigo-500 outline-none transition-all resize-none font-medium text-slate-700 shadow-inner"
                        />
                        <div className="absolute bottom-3 right-3">
                          <button 
                            onClick={handleSubmitAnswer}
                            disabled={!transcript.trim() || isTranscribing}
                            className="px-6 py-2.5 bg-indigo-600 text-white rounded-2xl text-[10px] font-black uppercase tracking-widest hover:bg-indigo-700 disabled:opacity-50 transition-all flex items-center gap-2 shadow-lg shadow-indigo-200 active:scale-95"
                          >
                            <Send size={14} /> Submit Answer
                          </button>
                        </div>
                      </div>
                    </div>
                  )}
                </div>"""

# Find the specific block in the interview stage
if 'MANUAL INPUT OPTION' not in content:
    # Use a more unique pattern to avoid wrong placement
    # We want to insert it inside the transcript card container, but at the bottom.
    # Looking at the code around 3693:
    pattern = r'<div ref={transcriptEndRef} className="h-0 w-0" />\s*</div>\s*<br />\s*\)\s*\}\s*</div>'
    # Actually, simpler: replace the div and its parents with the new version
    content = content.replace('<div ref={transcriptEndRef} className="h-0 w-0" />', insertion_point + " ---TEMP--- ")
    
    # Let's try a simpler approach: finding the end of the transcript div
    content = content.replace(insertion_point, manual_input_html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Manual input UI added successfully.")
