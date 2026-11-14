---
title: github
---
## **pullコマンド**
GitHubの最新状態をローカルに取り込むコマンドです。

```
git pull origin main
```

## BAT

```powershell
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
```

# push

## BAT

```powershell
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
```

## ローカル変更を破棄

```zsh
 git restore .obsidian/workspace.json
```

## delete branch

```zsh
git push origin --delete v5
```

![[Pasted image 20261114183832.png]]