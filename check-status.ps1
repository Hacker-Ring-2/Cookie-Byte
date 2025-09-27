Write-Host "Checking TheNZT Development Environment Status..." -ForegroundColor Green
Write-Host ""

# Check Docker containers
Write-Host "Docker Containers:" -ForegroundColor Yellow
docker-compose ps
Write-Host ""

# Check if backend is running
Write-Host "Backend Status (Port 8001):" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8001" -TimeoutSec 5 -UseBasicParsing
    Write-Host "✅ Backend is running" -ForegroundColor Green
} catch {
    Write-Host "❌ Backend is not responding" -ForegroundColor Red
}

# Check if frontend is running
Write-Host "Frontend Status (Port 3000):" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:3000" -TimeoutSec 5 -UseBasicParsing
    Write-Host "✅ Frontend is running" -ForegroundColor Green
} catch {
    Write-Host "❌ Frontend is not responding" -ForegroundColor Red
}

Write-Host ""
Write-Host "URLs:" -ForegroundColor Cyan
Write-Host "Backend API: http://localhost:8001" -ForegroundColor White
Write-Host "Frontend App: http://localhost:3000" -ForegroundColor White