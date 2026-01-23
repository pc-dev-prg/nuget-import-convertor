import pandas as pd
import csv
from pathlib import Path
from typing import List, Dict, Tuple
from schemas import PayrollRecord

class PayrollTransformer:
    def __init__(self):
        self.column_mapping = {
            0: "Os.č.",
            1: "Jméno",
            2: "Mzdová složka",
            3: "Hodnota",
            5: "Období"
        }

    @staticmethod
    def transform_date(period: str) -> str:
        """
        Converts YYYYMM to [M]YYYY (removing leading zero from month).
        Example: 202501 -> 12025, 202511 -> 112025
        """
        if len(period) != 6:
            return period
        
        year = period[:4]
        month = period[4:]
        
        # Remove leading zero
        if month.startswith("0"):
            month = month[1:]
            
        return f"{month}{year}"

    def process_file(self, file_path: Path) -> Tuple[bool, str]:
        try:
            # Read Excel without header to use index-based mapping
            df = pd.read_excel(file_path, header=None)
            
            # Map columns
            df_mapped = df.rename(columns=self.column_mapping)
            
            # Filter rows that have Os.č. and are not the header row
            # Header typically has "Os.č." or similar in the first column, or the first column is numeric
            records = []
            errors = []

            for index, row in df_mapped.iterrows():
                # Skip header (usually index 0 or row with column names as strings)
                # or empty rows (Os.c. is NaN)
                os_c_val = row.get("Os.č.")
                if pd.isna(os_c_val) or str(os_c_val).strip() == "Os.č.":
                    continue
                
                # Also skip rows where "Mzdová složka" is not a number (e.g. the header labels)
                mzdova_val = row.get("Mzdová složka")
                if pd.isna(mzdova_val) or str(mzdova_val).strip() == "Mzdová složka":
                    continue

                # Skip if "Hodnota" is NaN (no data to import)
                hodnota_val = row.get("Hodnota")
                if pd.isna(hodnota_val):
                    continue

                jmeno_val = row.get("Jméno")

                try:
                    data = {
                        "Os.č.": os_c_val,
                        "Jméno": jmeno_val,
                        "Mzdová složka": mzdova_val,
                        "Hodnota": hodnota_val,
                        "Období": row["Období"]
                    }
                    record = PayrollRecord(**data)
                    records.append(record)
                except Exception as e:
                    errors.append(f"Row {index+1}: {str(e)}")

            if not records:
                return False, "No valid records found in file."

            # Create output directory
            output_dir = file_path.parent / "Import"
            output_dir.mkdir(exist_ok=True)
            
            output_file = output_dir / f"{file_path.stem}.csv"
            
            # CSV Specification: Delimiter ;
            # POD (500), L0001 (Os.č.), L0004 (0), OBD (upravené datum), L4901 (Mzdová složka), L4902 (Hodnota), L4907 (A)
            
            with open(output_file, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                # Write Header
                writer.writerow(["POD", "L0001", "L0004", "OBD", "L4901", "L4902", "L4907", "JMENO"])
                
                for rec in records:
                    obd = self.transform_date(rec.obdobi)
                    writer.writerow([
                        "500",         # POD
                        rec.os_c,      # L0001
                        "0",           # L0004
                        obd,           # OBD
                        rec.mzdova_slozka, # L4901
                        rec.hodnota,   # L4902
                        "A",            # L4907
                        rec.jmeno      # JMENO
                    ])
            
            return True, f"Successfully processed {len(records)} records."

        except Exception as e:
            return False, f"Unexpected error: {str(e)}"

    def find_files(self, root_dir: Path) -> List[Path]:
        return list(root_dir.rglob("*.xlsx"))
