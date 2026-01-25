# --------------------------------------------
# app3.py
# Example 3: CSV File Uploader and Preview
# --------------------------------------------

import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="CSV Uploader",
    page_icon="📁",
    layout="centered"
)

# Title & Description
st.title("CSV File Uploader")
st.markdown(
    "Upload a CSV file to preview the dataset and view basic information."
)

st.divider()

# File Uploader
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

# Processing Uploaded File
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        st.subheader("Dataset Information")
        st.write(f"**Rows:** {df.shape[0]}")
        st.write(f"**Columns:** {df.shape[1]}")

    except Exception as e:
        st.error("Error reading the CSV file. Please upload a valid CSV.")
        st.exception(e)

else:
    st.info("Please upload a CSV file to view its contents.")