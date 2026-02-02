from pydantic import BaseModel, Field, validator
from typing import Optional, Any

class PayrollRecord(BaseModel):
    os_c: str = Field(..., alias="Os.č.")
    mzdova_slozka: str = Field(..., alias="Mzdová složka")
    hodnota: str = Field(..., alias="Hodnota")
    obdobi: str = Field(..., alias="Období")
    jmeno: str = Field(..., alias="Jméno")

    @validator("os_c", pre=True)
    def format_os_c(cls, v):
        if v is None: return ""
        # Convert float like 2145.0 to "2145"
        if isinstance(v, float):
            return str(int(v))
        return str(v).strip()

    @validator("jmeno", pre=True)
    def format_jmeno(cls, v):
        if v is None: return ""
        return str(v).strip()

    @validator("mzdova_slozka", pre=True)
    def format_mzdova_slozka(cls, v):
        """Truncate decimal part (e.g., 303.0000 -> 303), do NOT round."""
        if v is None: return ""
        if isinstance(v, float):
            return str(int(v))  # Truncate, not round
        # Handle string with decimals like "303,0000" or "303.0000"
        s = str(v).strip().replace(",", ".")
        try:
            return str(int(float(s)))  # Truncate decimal part
        except ValueError:
            return s

    @validator("hodnota", pre=True)
    def format_hodnota(cls, v):
        """Round to 2 decimal places (e.g., 37452.16546648 -> 37452,17)."""
        if v is None: return "0"
        # Remove thousand separators and handle floats
        s = str(v).replace(" ", "").replace(",", ".")
        try:
            num = float(s)
            rounded = round(num, 2)
            # Format with comma as decimal separator
            if rounded == int(rounded):
                return str(int(rounded))  # No decimals needed for whole numbers
            else:
                return f"{rounded:.2f}".replace(".", ",")
        except ValueError:
            return "0"

    @validator("obdobi", pre=True)
    def format_obdobi(cls, v):
        if v is None: return ""
        if isinstance(v, float):
            return str(int(v))
        return str(v).strip()
