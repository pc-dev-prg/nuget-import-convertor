#!/bin/bash

echo "[0/3] Kontrola instalace Pythonu..."
if ! command -v python3 &> /dev/null; then
    echo ""
    echo "[CHYBA] Python nebyl v tomto systému nalezen!"
    echo "Pro běh této aplikace je nutné mít nainstalovaný Python."
    echo ""
    echo "Za 5 sekund se otevře stránka pro stažení Pythonu..."
    sleep 5
    open "https://www.python.org/downloads/"
    exit 1
fi

echo "[1/3] Kontrola Python prostředí..."
if [ ! -d ".venv" ]; then
    echo "Vytvářím virtuální prostředí .venv..."
    python3 -m venv .venv
fi

echo "[2/3] Instalace závislostí..."
source .venv/bin/activate
pip install -r requirements.txt

echo "[3/3] Spouštím aplikaci..."
python main.py

read -p "Stiskněte libovolnou klávesu pro pokračování..."
deactivate
