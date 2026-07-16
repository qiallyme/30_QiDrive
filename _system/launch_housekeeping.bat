@echo off
setlocal
cd /d "%~dp0"
title QiLabs Housekeeping Console

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "C:\QiLabs\00_QiLabs.workspace\toolbox\tools\checkers\housekeeping\housekeeping_ui.py"
  goto :end
)

where python >nul 2>nul
if %errorlevel%==0 (
  python "C:\QiLabs\00_QiLabs.workspace\toolbox\tools\checkers\housekeeping\housekeeping_ui.py"
  goto :end
)

echo.
echo Python was not found. Install Python 3 or add it to PATH.
echo.
pause

:end
endlocal
