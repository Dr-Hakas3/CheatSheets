@echo off
cd /d "C:\Users\user\Desktop\Study\GitHub\CheatSheets"

echo Pulling latest changes from GitHub...
git pull origin main

echo.
pause
@echo off
cd /d "%~dp0"

echo GitHubから最新データを取得します...
git pull origin main

echo.
pause