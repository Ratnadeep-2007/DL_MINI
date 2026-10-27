@echo off
title Digit Recognition - Streamlit
cd /d "%~dp0"

if not exist "app.py" (
    echo [ERROR] app.py not found in "%~dp0"
    pause
    exit /b 1
)

if not exist "venv\Scripts\python.exe" (
    echo [ERROR] venv not found: "%~dp0venv"
    echo Create it and install dependencies first:
    echo   python -m venv venv
    echo   venv\Scripts\python.exe -m pip install -r requirements.txt
    pause
    exit /b 1
)

echo ============================================
echo  Digit Recognition
echo  URL: http://localhost:8501
echo  Press Ctrl+C to stop the server
echo ============================================
echo.

"venv\Scripts\python.exe" -m streamlit run app.py --server.port 8501

echo.
echo Server stopped.
pause
