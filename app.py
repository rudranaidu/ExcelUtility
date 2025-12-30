import streamlit as st
import pandas as pd
from io import BytesIO

from transformers.attendance import generate_muster_roll
from transformers.wages import generate_wages_report
from utils.excel_writer import write_muster_roll
from utils.wages_excel_writer import write_wages_report

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Contract Labour Report System", layout="wide")

# ---------------- THEME ----------------
st.markdown("""
<style>
body { background-color: #EAF2F6; }

section[data-testid="stSidebar"] { background-color: #4F7FA3; }
section[data-testid="stSidebar"] * { color: white; }

.main-header {
    background-color: #6FAFC6;
    padding: 2rem;
    border-radius: 18px;
    color: white;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.12);
}

.card {
    background: white;
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.12);
    margin-top: 1.5rem;
}

.subtitle { font-size: 1.1rem; color: #F0F8FB; }

.stButton > button, .stDownloadButton > button {
    background: #78C6A3;
    color: white;
    border-radius: 30px;
    padding: 0.6rem 2rem;
    font-weight: 600;
    border: none;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background: #6BB894;
}

h2 { color: #4F7FA3; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 📋 Report Types")
report_type = st.sidebar.radio(
    "Select Report",
    [
        "Attendance → FORM-XVI",
        "Wages Report → FORM-XVII",
        "Payroll Summary (Coming Soon)",
        "Overtime Register (Coming Soon)"
    ]
)

# ---------------- HEADER ----------------
st.markdown("""
<div class="main-header">
    <h1>📁 Contract Labour Report System</h1>
    <div class="subtitle">Generate statutory labour reports easily</div>
</div>
""", unsafe_allow_html=True)

# ---------------- ATTENDANCE ----------------
if report_type.startswith("Attendance"):
    st.markdown('<div class="card"><h2>🧾 FORM-XVI Muster Roll</h2>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Attendance Excel Sheet", type=["xlsx"], key="att_file")

    if uploaded_file:
        xls = pd.ExcelFile(uploaded_file)
        sheet_name = st.selectbox("Select Attendance Sheet", xls.sheet_names, key="att_sheet")

        df_output = generate_muster_roll(uploaded_file, sheet_name)

        st.markdown("### 🔎 Preview")
        st.dataframe(df_output, use_container_width=True)

        buffer = BytesIO()
        write_muster_roll(df_output, buffer, "NOV-2025")

        st.download_button(
            "⬇️ Download FORM-XVI Muster Roll",
            buffer.getvalue(),
            file_name="FORM_XVI_Muster_Roll.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- WAGES ----------------
elif report_type.startswith("Wages"):
    st.markdown('<div class="card"><h2>💰 FORM-XVII Wages Report</h2>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Attendance Excel Sheet", type=["xlsx"], key="wage_file")

    if uploaded_file:
        xls = pd.ExcelFile(uploaded_file)
        sheet_name = st.selectbox("Select Attendance Sheet", xls.sheet_names, key="wage_sheet")

        attendance_df = generate_muster_roll(uploaded_file, sheet_name)

        wages_df = generate_wages_report(attendance_df)

        st.markdown("### 🔎 Preview")
        st.dataframe(wages_df, use_container_width=True)

        buffer = BytesIO()
        write_wages_report(wages_df, buffer, "NOV-2025")

        st.download_button(
            "⬇️ Download FORM-XVII Wages Report",
            buffer.getvalue(),
            file_name="FORM_XVII_Wages_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    st.markdown("</div>", unsafe_allow_html=True)

