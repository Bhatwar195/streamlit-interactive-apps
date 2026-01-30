# --------------------------------------------
# app12.py
# Example 12: Progress Bar & Long Task Simulation
# --------------------------------------------

import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Progress Bar Demo",
    page_icon="⏳",
    layout="centered"
)

# Title & Description
st.title("Progress Bar Demo")
st.markdown(
    "This example demonstrates how to provide **progress feedback** "
    "during a long-running task using Streamlit."
)

st.divider()

# Button to start task
if st.button("Start Long Task"):
    progress_bar = st.progress(0)
    status_text = st.empty()

    for step in range(100):
        time.sleep(0.02)  # Simulate work
        progress_bar.progress(step + 1)
        status_text.text(f"Processing step {step + 1} of 100")

    status_text.empty()
    st.success("✅ Task completed successfully!")

st.info("Progress indicators improve user experience during long computations.")