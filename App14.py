# --------------------------------------------
# app14.py
# Example 14: Download Generated Data (CSV / Excel)
# --------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="File Download Example",
    page_icon="⬇️",
    layout="centered"
)

# Title & Description
st.title("Download Example")
st.markdown(
    "This example demonstrates how to **generate data** and allow users "
    "to **download it as CSV or Excel files** using Streamlit."
)

st.divider()

# User Control
num_rows = st.slider(
    "Select number of rows",
    min_value=10,
    max_value=1000,
    value=100,
    step=50
)

# Generate Data
df = pd.DataFrame(
    np.random.randn(num_rows, 4),
    columns=["A", "B", "C", "D"]
)

# Preview
st.subheader("Data Preview")
st.dataframe(df.head(), use_container_width=True)

# ---- CSV Download ----
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name="random_data.csv",
    mime="text/csv"
)

# ---- Excel Download ----
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Data")

st.download_button(
    label="⬇️ Download Excel",
    data=buffer.getvalue(),
    file_name="random_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.info("`st.download_button` enables client-side downloads of generated data.")
