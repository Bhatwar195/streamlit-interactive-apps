# --------------------------------------------
# app15.py
# Example 15: Multi-Column Layout & Dashboard Cards
# --------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Multi-Column Dashboard",
    page_icon="📐",
    layout="wide"
)

# Title & Description
st.title("Multi-Column Layout")
st.markdown(
    "This example demonstrates how to build **dashboard-style layouts** "
    "using multiple columns and metric cards."
)

st.divider()

# User Control
rows = st.slider(
    "Select number of rows",
    min_value=10,
    max_value=200,
    value=50,
    step=10
)

# Data
data = pd.DataFrame(
    np.random.randn(rows, 3),
    columns=["A", "B", "C"]
)

# Metric Cards
m1, m2, m3 = st.columns(3)
m1.metric("Mean A", f"{data['A'].mean():.2f}")
m2.metric("Mean B", f"{data['B'].mean():.2f}")
m3.metric("Mean C", f"{data['C'].mean():.2f}")

st.divider()

# Chart Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Line Chart")
    st.line_chart(data)

with col2:
    st.subheader("📊 Bar Summary")
    st.bar_chart(data.abs().sum())

st.info("`st.columns` enables responsive, dashboard-style layouts.")
