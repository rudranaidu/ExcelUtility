import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MASTER_FILE = BASE_DIR / "data" / "employee_master.xlsx"

def load_employee_master():
    df = pd.read_excel(MASTER_FILE)

    # Normalize headers
    df.columns = [c.replace(" ", "").strip() for c in df.columns]

    df["EmpID"] = df["EmpID"].astype(str)
    return df

