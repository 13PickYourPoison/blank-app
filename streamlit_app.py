import streamlit as st
import pandas as pd

st.title("GreenForce 1")

# File uploader button
estimate_summary = st.file_uploader("Estimate Summary", type=["csv"])
production_by_tech = st.file_uploader("Prod. By Tech", type = ["csv"])
sales_report = st.file_uploader("Sales Report", type = ["csv"])
_24_cancel_report = st.file_uploader("2024 Cancel Report", type = ["csv"])
_25_cancel_report = st.file_uploader("2025 Cancel Report", type = ["csv"])

file_dict = {
    estimate_summary : 'estimate_summary',
    production_by_tech : 'production_by_tech',
    sales_report : 'sales report',
    _24_cancel_report: '_24_cancel_report',
    _25_cancel_report: '_25_cancel_report'
}
# Check if files are uploaded

for file, name in file_dict.items():
    if file is not None:
        name = pd.read_csv(file)
        st.session_sate['name'] = file
        st.success("File uploaded successfully")

#if estimate_summary is not None:
    # Read the CSV file
    df = pd.read_csv(estimate_summary)
    
    # Save the dataframe to session state so it persists between reruns
    st.session_state['estimate_data'] = df
    
    st.success("File successfully uploaded!")