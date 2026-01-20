@echo off
setlocal

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
