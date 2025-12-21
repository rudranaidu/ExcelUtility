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





Tech Stack

  Python 3.11
  Streamlit – UI
  pandas – data processing
  openpyxl – Excel read/write


excelUtility/
├── excel_merge_app.py
├── requirements.txt
└── README.md

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




