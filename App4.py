# --------------------------------------------
# app4.py
# Example 4: Line Chart with Random Data
# --------------------------------------------

import streamlit as st
import numpy as np
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Line Chart Demo",
    page_icon="📈",
    layout="centered"
)

# Title & Description
st.title("Line Chart Demo")
st.markdown(
    "This example demonstrates Streamlit's built-in line chart "
    "using randomly generated data."
)

st.divider()

# User Control
num_points = st.slider(
    "Select number of data points",
    min_value=10,
    max_value=100,
    value=50
)

# Data Generation
data = pd.DataFrame(
    np.random.randn(num_points, 3),
    columns=["A", "B", "C"]
)

# Visualization
st.subheader("Generated Line Chart")
st.line_chart(data)

# Footer Info
st.info("This visualization uses Streamlit's built-in interactive charting.")