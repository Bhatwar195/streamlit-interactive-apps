# --------------------------------------------
# app8.py
# Example 8: Altair Scatter Plot (Declarative)
# --------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Page Configuration
st.set_page_config(
    page_title="Altair Scatter Plot",
    page_icon="🔵",
    layout="centered"
)

# Title & Description
st.title("Altair Scatter Plot")
st.markdown(
    "This example demonstrates **Altair's declarative charting** "
    "approach with interactive scatter plots and tooltips."
)

st.divider()

# User Control
num_points = st.slider(
    "Select number of data points",
    min_value=50,
    max_value=500,
    value=200,
    step=50
)

# Data
df = pd.DataFrame({
    "x": np.random.randn(num_points),
    "y": np.random.randn(num_points),
    "size": np.abs(np.random.randn(num_points)) * 30
})

# Altair Chart
chart = (
    alt.Chart(df)
    .mark_circle(opacity=0.7)
    .encode(
        x=alt.X("x", title="X Value"),
        y=alt.Y("y", title="Y Value"),
        size=alt.Size("size", title="Magnitude"),
        color=alt.Color("size", scale=alt.Scale(scheme="viridis")),
        tooltip=["x", "y", "size"]
    )
    .interactive()
)

# Render Chart
st.altair_chart(chart, use_container_width=True)

st.info("Altair uses a declarative grammar of graphics for interactive visualizations.")