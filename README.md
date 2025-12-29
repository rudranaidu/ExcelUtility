# 📊 Excel Merge Utility (Local Streamlit App)

A lightweight **local Excel merge application** built using **Python and Streamlit**.  
This tool allows you to upload multiple Excel files, apply simple merge logic, preview the merged data, and download the final Excel file — all running locally on your machine.

No backend server, no database, no cloud deployment required.

---

## ✨ Features

- Runs locally on your machine
- Simple browser-based UI
- Upload multiple `.xlsx` files
- Merge by key or append rows
- Preview merged data
- Download merged Excel file
- Lightweight and easy to set up

---

## 🧰 Tech Stack

- **Python 3.11**
- **Streamlit** – UI framework
- **pandas** – Data processing
- **openpyxl** – Excel read/write support

---

## 📁 Project Structure


excelUtility/
├── excel_merge_app.py
├── requirements.txt
└── README.md


---

## 🧩 Prerequisites

- Python **3.10+** (recommended: 3.11)
- `pip` installed
- macOS / Linux / Windows

---

## 🛠️ Setup Instructions

### 1️⃣ Clone or Create Project Folder

```bash
mkdir excelUtility
cd excelUtility

Clone or Create Project Folder
  mkdir excelUtility
  cd excelUtility
Create Virtual Environment
  python -m venv excelenv
  source excelenv/bin/activate

Install Required Libraries
 pip install streamlit pandas openpyxl

 How to Run the Application
   source excelenv/bin/activate

Start Streamlit (recommended way)
 python -m streamlit run excel_merge_app.py

Accessing the App in Browser
   Local URL: http://localhost:8501




excelUtility/
│
├── data/
│   ├── employee_master.xlsx     ← constants
│   ├── wage_rules.json          ← configuration
│   └── generated_reports/
│       ├── attendance/
│       └── wages/
│
├── transformers/
│   ├── attendance.py
│   └── wages.py   ← (we will build)
│
└── utils/
    └── excel_writer_wages.py  ← (we will build)

For creating installer

pip install pyinstaller

pyi-makespec desktop/launcher.py --name ContractLabourApp --onefile
