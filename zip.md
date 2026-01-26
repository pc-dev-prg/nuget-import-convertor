# Návod k použití zip.sh

Tento skript slouží k automatickému vytvoření balíčku pro klienta.

## Co skript dělá

1. Vytvoří dočasnou složku `nuget-payroll-transformer`.
2. Zkopíruje do ní všechny potřebné soubory (`main.py`, `transformer.py`, `schemas.py`, `requirements.txt`, `run.bat`, `Manual.pdf`, `README.md`).
3. Zabalí tuto složku do souboru `nuget-payroll-transformer.zip`.
4. Odstraní dočasnou složku.

## Jak skript spustit

1. Otevřete terminál v kořenové složce projektu.
2. Pokud spouštíte skript poprvé, nastavte mu práva pro spuštění:
   ```bash
   chmod +x zip.sh
   ```
3. Spusťte skript:
   ```bash
   ./zip.sh
   ```

## Výsledek

V kořenové složce vznikne soubor `nuget-payroll-transformer.zip`, který můžete odeslat uživateli. Ten si jej rozbalí a uvidí složku `nuget-payroll-transformer` se vším potřebným.
