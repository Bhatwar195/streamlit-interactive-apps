# --------------------------------------------
# app6.py
# Example 6: Area Chart – Temperature Over Time
# --------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Temperature Area Chart",
    page_icon="🌡️",
    layout="centered"
)

# Title & Description
st.title("Area Chart – Temperature Over Time")
st.markdown(
    "This example visualizes simulated daily temperature data "
    "using an area chart, which is effective for showing trends over time."
)

st.divider()

# User Controls
num_days = st.slider(
    "Select number of days",
    min_value=7,
    max_value=60,
    value=30
)

base_temp = st.slider(
    "Base temperature (°C)",
    min_value=10,
    max_value=30,
    value=20
)

# Data Generation
dates = pd.date_range(start="2025-01-01", periods=num_days)
temperatures = np.cumsum(np.random.randn(num_days)) + base_temp

df = pd.DataFrame(
    {"Temperature (°C)": temperatures},
    index=dates
)

# Visualization
st.subheader("Temperature Trend")
st.area_chart(df)

# Insights
st.subheader("Summary Statistics")
st.write(f"**Average Temperature:** {df.mean().values[0]:.2f} °C")
st.write(f"**Maximum Temperature:** {df.max().values[0]:.2f} °C")

st.info("Area charts are useful for visualizing magnitude and trends over time.")