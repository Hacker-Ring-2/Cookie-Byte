Write-Host "Restarting Frontend Server..." -ForegroundColor Yellow

# Kill any existing Next.js processes
Write-Host "Stopping existing Next.js processes..." -ForegroundColor Red
Get-Process -Name "node" -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*next*" } | Stop-Process -Force -ErrorAction SilentlyContinue

# Clear Next.js cache
Write-Host "Clearing Next.js cache..." -ForegroundColor Yellow
Remove-Item -Recurse -Force src/frontend/.next -ErrorAction SilentlyContinue

# Wait a moment
Start-Sleep -Seconds 2

# Start frontend server
Write-Host "Starting fresh Next.js server..." -ForegroundColor Green
Set-Location src/frontend
npm run dev