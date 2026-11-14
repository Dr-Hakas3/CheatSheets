@echo off
cd /d "C:\Users\user\Desktop\Study\GitHub\CheatSheets"

echo ==================================
echo GitHub Push
echo ==================================

git status
echo.

git add .
git commit -m "Update cheat sheets"
git push origin main

echo.
echo Finished.
pause