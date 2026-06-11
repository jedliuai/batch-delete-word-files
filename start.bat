@echo off
setlocal
cd /d "%~dp0"

where pyw >nul 2>nul
if %errorlevel%==0 (
    pyw -3 "%~dp0main.py"
    goto end
)

where pythonw >nul 2>nul
if %errorlevel%==0 (
    pythonw "%~dp0main.py"
    goto end
)

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "%~dp0main.py"
    goto end
)

where python >nul 2>nul
if %errorlevel%==0 (
    python "%~dp0main.py"
    goto end
)

echo Python 3 was not found. Please install Python 3 first.
pause

:end
endlocal
