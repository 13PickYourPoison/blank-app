import streamlit as st
import pandas as pd
from database import init_db, save_to_table, load_from_table

init_db()

st.title("GreenForce 1")

# File uploader buttons
estimate_summary = st.file_uploader("Estimate Summary", type=["csv"])
production_by_tech = st.file_uploader("Prod. By Tech", type=["csv"])
sales_report = st.file_uploader("Sales Report", type=["csv"])
cancel_report_24 = st.file_uploader("2024 Cancel Report", type=["csv"])
cancel_report_25 = st.file_uploader("2025 Cancel Report", type=["csv"])

file_dict = {
    'estimate_summary': estimate_summary,
    'production_by_tech': production_by_tech,
    'sales_report': sales_report,
    'cancel_report_24': cancel_report_24,
    'cancel_report_25': cancel_report_25
}

'''# Check if files are uploaded
for name, file in file_dict.items():
    if file is not None:
        # Read the CSV into a dataframe
        df = pd.read_csv(file)
        
        # Store in session state with the correct name
        st.session_state[name] = df
        
        # Show a success message and preview
        st.success(f"{name} uploaded successfully!")
        st.write(f"Preview of {name}:")
        st.dataframe(df.head())
        '''