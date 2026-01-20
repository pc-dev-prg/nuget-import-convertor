# Uživatelský manuál: Payroll Data Transformer

Tento nástroj slouží pro mzdové účetní k automatické transformaci Excel souborů (.xlsx) do specifického CSV formátu pro import do mzdových systémů.

## 📋 Předpoklady

Před prvním spuštěním se ujistěte, že máte nainstalovány následující programy:

1.  **Python 3.10 nebo novější**:
    - Stáhněte z [python.org](https://www.python.org/downloads/windows/).
    - **Důležité**: Při instalaci zaškrtněte políčko **"Add Python to PATH"**.

## 🚀 První spuštění a instalace

Aplikace je navržena tak, aby byla na Windows co nejjednodušší na spuštění:

1.  Stáhněte nebo zkopírujte složku s aplikací do vašeho počítače.
2.  Najděte soubor `run.bat` ve složce aplikace.
3.  Dvakrát na něj klikněte.
4.  Při prvním spuštění aplikace automaticky:
    - Vytvoří virtuální prostředí (`.venv`).
    - Nainstaluje všechny potřebné knihovny (Pandas, Rich, Pydantic atd.).
    - Spustí samotný program.

## 📖 Jak aplikaci používat

1.  **Spuštění**: Vždy spouštějte aplikaci pomocí souboru `run.bat`.
2.  **Výběr složky**: Po spuštění se otevře standardní Windows okno pro výběr složky. Vyberte složku, ve které se nacházejí vaše Excel soubory (.xlsx).
3.  **Zpracování**:
    - Aplikace prohledá vybranou složku i všechny její podsložky.
    - Pro každý nalezený soubor vytvoří v daném místě podsložku `/Import`.
    - Do této podsložky uloží transformovaný soubor ve formátu `.csv`.
4.  **Zpětná vazba**: V terminálu uvidíte přehlednou tabulku se stavem zpracování každého souboru.
5.  **Pokračování nebo Konec**:
    - Stiskněte **[N]** pro výběr nové složky.
    - Stiskněte **[K]** pro ukončení aplikace.

## 🛠️ Detaily transformace

Aplikace automaticky provádí tyto kroky:

- **Transformace data**: Převádí formát `202511` na `112025` (odstraňuje nuly na začátku měsíce).
- **Úprava čísel**: Odstraňuje oddělovače tisíců a převádí čárky na tečky.
- **Formát CSV**: Výstupní soubor má středník (`;`) jako oddělovač a obsahuje záhlaví sloupců podle specifikace.

## ⚠️ Řešení problémů

- **Soubor se nezpracoval**: Zkontrolujte, zda Excel obsahuje správné sloupce: `Os.č.` (sloupec A), `Mzdová složka` (sloupec C), `Hodnota` (sloupec D) a `Období` (sloupec F).
- **Chyba "Python not found"**: Ujistěte se, že máte Python nainstalovaný a přidaný do systémové cesty (PATH).
