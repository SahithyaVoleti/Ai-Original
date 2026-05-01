@echo off
echo Starting AI Interviewer Platform...

:: Start Backend API
start cmd /k "cd backend/api && ..\..\.venv\Scripts\activate && python api.py"

:: Start Backend Worker
start cmd /k "cd backend/worker && ..\..\.venv\Scripts\activate && python run_proctor_server.py"

:: Start Frontend
start cmd /k "cd frontend && npm run dev"

echo All services are starting in separate windows.
pause
