#!/usr/bin/env python3
"""Quick test script without GUI - processes all xlsx files in current directory."""

from pathlib import Path
from transformer import PayrollTransformer

if __name__ == "__main__":
    transformer = PayrollTransformer()
    root_dir = Path(".")
    
    files = transformer.find_files(root_dir)
    print(f"Nalezeno {len(files)} souborů")
    
    for file_path in files:
        print(f"\nZpracovávám: {file_path}")
        success, message = transformer.process_file(file_path)
        status = "✅ OK" if success else "❌ CHYBA"
        print(f"  {status}: {message}")
    
    print("\n✅ Hotovo! Výsledky jsou ve složce Import/")
