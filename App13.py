# --------------------------------------------
# app13.py
# Example 13: Caching Expensive Computations
# --------------------------------------------

import streamlit as st
import time
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Caching Example",
    page_icon="⚡",
    layout="centered"
)

# Title & Description
st.title("Caching Example")
st.markdown(
    "This example demonstrates how **`st.cache_data`** can significantly "
    "speed up expensive computations by caching results."
)

st.divider()

# Cached Function
@st.cache_data
def expensive_calc(n: int) -> pd.DataFrame:
    """Simulate an expensive computation."""
    time.sleep(2)  # Simulate delay
    return pd.DataFrame(
        np.random.randn(n, 3),
        columns=["A", "B", "C"]
    )

# User Control
n = st.slider(
    "Number of rows",
    min_value=100,
    max_value=5000,
    value=500,
    step=100
)

# Measure Execution Time
start_time = time.time()
df = expensive_calc(n)
elapsed_time = time.time() - start_time

# Display Output
st.subheader("Result Preview")
st.dataframe(df.head(), use_container_width=True)

st.write(f"⏱️ **Execution time:** {elapsed_time:.2f} seconds")

st.info(
    "On the first run, the function is slow. "
    "Subsequent runs with the same input are fast due to caching."
)
