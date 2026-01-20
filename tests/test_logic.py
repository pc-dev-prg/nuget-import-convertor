import pytest
from transformer import PayrollTransformer
from schemas import PayrollRecord

def test_date_transformation():
    transformer = PayrollTransformer()
    # YYYYMM -> [M]YYYY
    assert transformer.transform_date("202511") == "112025"
    assert transformer.transform_date("202501") == "12025"
    assert transformer.transform_date("202410") == "102024"
    assert transformer.transform_date("202409") == "92024"

def test_number_formatting():
    # Os.č. validation
    rec = PayrollRecord(**{
        "Os.č.": 2145.0,
        "Mzdová složka": 305.0,
        "Hodnota": "5 000,00",
        "Období": "202511"
    })
    assert rec.os_c == "2145"
    assert rec.mzdova_slozka == "305"
    assert rec.hodnota == "5000"
    
    rec2 = PayrollRecord(**{
        "Os.č.": "1111",
        "Mzdová složka": "305",
        "Hodnota": "1500.50",
        "Období": "202511"
    })
    assert rec2.hodnota == "1500.5"

def test_empty_values():
    rec = PayrollRecord(**{
        "Os.č.": None,
        "Mzdová složka": None,
        "Hodnota": None,
        "Období": None
    })
    assert rec.os_c == ""
    assert rec.hodnota == "0"
