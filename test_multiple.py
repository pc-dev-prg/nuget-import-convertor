from transformer import PayrollTransformer
from pathlib import Path

def test_multiple():
    t = PayrollTransformer()
    # Ensure nested directory works too
    nested = Path("subdir")
    nested.mkdir(exist_ok=True)
    import shutil
    shutil.copy("202511_1803_305_1.xlsx", nested / "202511_Nested.xlsx")
    
    files = t.find_files(Path("."))
    print(f"Total files found: {len(files)}")
    for f in files:
        success, msg = t.process_file(f)
        print(f"Processing {f}: {success} - {msg}")

if __name__ == "__main__":
    test_multiple()
