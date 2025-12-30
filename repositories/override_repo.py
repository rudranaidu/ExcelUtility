import pandas as pd
from pathlib import Path

def load_overrides(path="data/employee_overrides.xlsx"):
    if not Path(path).exists():
        return {}

    df = pd.read_excel(path)
    df["EmpID"] = df["EmpID"].astype(str)
    return df.set_index("EmpID").to_dict(orient="index")

