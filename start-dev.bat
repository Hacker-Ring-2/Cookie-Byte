@echo off
echo Starting TheNZT Development Environment...
echo.

REM Check if Docker containers are running
echo Checking Docker containers...
docker-compose ps

REM Start Docker containers if not running
echo Starting Docker containers...
docker-compose up -d

REM Wait a moment for containers to be ready
timeout /t 3 /nobreak > nul

echo.
echo Starting Backend (FastAPI)...
start "Backend Server" cmd /k ".venv\Scripts\activate && set PYTHONPATH=. && uvicorn src.backend.app:app --host 0.0.0.0 --port 8001 --reload"

REM Wait a moment before starting frontend
timeout /t 2 /nobreak > nul

echo.
echo Starting Frontend (Next.js)...
start "Frontend Server" cmd /k "cd src/frontend && npm run dev"

echo.
echo ========================================
echo Development servers are starting...
echo Backend: http://localhost:8001
echo Frontend: http://localhost:3000
echo ========================================
echo.
echo Press any key to exit...
pause > nul