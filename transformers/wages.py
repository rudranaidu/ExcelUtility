import pandas as pd
from repositories.employee_repo import load_employee_master
from repositories.wage_rules_repo import load_wage_rules


def generate_wages_report(attendance_df):

    employees = load_employee_master()
    rules = load_wage_rules()

    results = []

    for _, att in attendance_df.iterrows():

        # --- Match employee by NAME (not EmpID) ---
        name = str(att["NAME"]).strip().upper()
        emp_match = employees[employees["Name"].str.strip().str.upper() == name]

        if emp_match.empty:
            continue   # skip if employee not found in master

        emp = emp_match.iloc[0]

        # --- Count working days from attendance (count of 'P') ---
        day_cols = [c for c in attendance_df.columns if str(c).isdigit()]
        working_days = sum(1 for d in day_cols if str(att[d]).strip().upper() == "P")

        category = emp["Category"]

        # --- Load wage rules for this category ---

        category = emp["Category"].strip().upper()
        daily_wage = rules["daily_wages"][category]
        pf_rate = rules["pf"]["employee"]
        esi_rate = rules["esi"]["employee"]

        gross_wage = working_days * daily_wage
        pf_amount = gross_wage * pf_rate
        esi_amount = gross_wage * esi_rate
        net_wage = gross_wage - pf_amount - esi_amount

        results.append({
            "EmpID": emp["EmpID"],
            "Name": emp["Name"],
            "Category": category,
            "WorkingDays": working_days,
            "DailyWage": daily_wage,
            "GrossWage": round(gross_wage, 2),
            "PF": round(pf_amount, 2),
            "ESI": round(esi_amount, 2),
            "NetWage": round(net_wage, 2),
            "UAN": emp["UAN"],
            "ESI_Number": emp["ESI"],
            "BankAccount": emp["BankAccount"],
            "BankName": emp["BankName"]
        })

    return pd.DataFrame(results)

