import pandas as pd

def find_header_row(raw):
    for i in range(len(raw)):
        val = str(raw.iloc[i, 0])
        if val.startswith("PE"):
            return max(i - 1, 0)
    raise ValueError("Could not locate attendance table")

def generate_muster_roll(input_file, sheet_name):
    raw = pd.read_excel(input_file, sheet_name=sheet_name, header=None)

    header_row = find_header_row(raw)
    df = pd.read_excel(input_file, sheet_name=sheet_name, header=header_row)

    # Keep only real employee rows
    df = df[df.iloc[:, 0].astype(str).str.startswith("PE")]

    output = pd.DataFrame()
    output["SL"] = range(1, len(df) + 1)
    output["NAME"] = df.iloc[:, 1]

    # Detect numeric day columns correctly
    for col in df.columns:
        if isinstance(col, int) and 1 <= col <= 31:
            output[col] = df[col].apply(lambda x: "P" if x == 1 else "A")

    # Append Present column
    gt_col = [c for c in df.columns if "GRAND" in str(c).upper()][0]
    output["Present"] = df[gt_col]

    return output

