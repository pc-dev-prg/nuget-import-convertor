@echo off
setlocal

echo [0/3] Kontrola instalace Pythonu...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [CHYBA] Python nebyl v tomto systemu nalezen!
    echo Pro beh teto aplikace je nutne mit nainstalovany Python.
    echo.
    echo Za 5 sekund se otevre stranka pro stazeni Pythonu...
    timeout /t 5
    start https://www.python.org/downloads/
    exit /b
)

echo [1/3] Kontrola Python prostredi...
if not exist .venv (
    echo Vytvarim virtualni prostredi .venv...
    python -m venv .venv
)

echo [2/3] Instalace zavislosti...
call .venv\Scripts\activate.bat
pip install -r requirements.txt

echo [3/3] Spoustim aplikaci...
python main.py

pause
deactivate
