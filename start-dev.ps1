Write-Host "Starting TheNZT Development Environment..." -ForegroundColor Green
Write-Host ""

# Check if Docker containers are running
Write-Host "Checking Docker containers..." -ForegroundColor Yellow
docker-compose ps

# Start Docker containers if not running
Write-Host "Starting Docker containers..." -ForegroundColor Yellow
docker-compose up -d

# Wait for containers to be ready
Start-Sleep -Seconds 3

Write-Host ""
Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& { .venv\Scripts\activate; `$env:PYTHONPATH='.'; uvicorn src.backend.app:app --host 0.0.0.0 --port 8001 --reload }"

# Wait before starting frontend
Start-Sleep -Seconds 2

Write-Host ""
Write-Host "Starting Frontend (Next.js)..." -ForegroundColor Cyan
# Clear Next.js cache first
Remove-Item -Recurse -Force src/frontend/.next -ErrorAction SilentlyContinue
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& { Set-Location src/frontend; npm run dev }"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Development servers are starting..." -ForegroundColor Green
Write-Host "Backend: http://localhost:8001" -ForegroundColor White
Write-Host "Frontend: http://localhost:3000" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")