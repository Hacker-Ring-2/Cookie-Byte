Write-Host "Restarting Frontend with updated configuration..." -ForegroundColor Green

# Kill any existing Next.js processes on port 3000
$processes = Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
if ($processes) {
    foreach ($processId in $processes) {
        Write-Host "Stopping process $processId on port 3000..." -ForegroundColor Yellow
        Stop-Process -Id $processId -Force -ErrorAction SilentlyContinue
    }
    Start-Sleep -Seconds 2
}

Write-Host "Starting Frontend on port 3000..." -ForegroundColor Cyan
Set-Location src/frontend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& { npm run dev }"

Write-Host ""
Write-Host "Frontend restarted with updated API URL: http://localhost:8001" -ForegroundColor Green
Write-Host "Frontend will be available at: http://localhost:3000" -ForegroundColor White