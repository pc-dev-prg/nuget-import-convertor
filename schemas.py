from pydantic import BaseModel, Field, validator
from typing import Optional, Any

class PayrollRecord(BaseModel):
    os_c: str = Field(..., alias="Os.č.")
    mzdova_slozka: str = Field(..., alias="Mzdová složka")
    hodnota: str = Field(..., alias="Hodnota")
    obdobi: str = Field(..., alias="Období")

    @validator("os_c", pre=True)
    def format_os_c(cls, v):
        if v is None: return ""
        # Convert float like 2145.0 to "2145"
        if isinstance(v, float):
            return str(int(v))
        return str(v).strip()

    @validator("mzdova_slozka", pre=True)
    def format_mzdova_slozka(cls, v):
        if v is None: return ""
        if isinstance(v, float):
            return str(int(v))
        return str(v).strip()

    @validator("hodnota", pre=True)
    def format_hodnota(cls, v):
        if v is None: return "0"
        # Remove thousand separators and handle floats
        s = str(v).replace(" ", "").replace(",", ".")
        try:
            return str(float(s)).replace(".0", "")
        except ValueError:
            return "0"

    @validator("obdobi", pre=True)
    def format_obdobi(cls, v):
        if v is None: return ""
        if isinstance(v, float):
            return str(int(v))
        return str(v).strip()
