# --------------------------------------------
# app2.py
# Example 2: Widgets Gallery (Input Controls)
# --------------------------------------------

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Widgets Gallery",
    page_icon="🎛️",
    layout="centered"
)

# Title & Description
st.title("Widgets Gallery")
st.markdown(
    "This example demonstrates common Streamlit input widgets "
    "such as text input, slider, and select box."
)

st.divider()

# Input Widgets
name = st.text_input("Enter your name", "Bhavesh")
age = st.slider("Select your age", min_value=0, max_value=100, value=30)
color = st.selectbox(
    "Select your favorite color",
    ["Red", "Green", "Blue", "Yellow"]
)

# Output Section
st.subheader("User Details")

st.write(f"👤 **Name:** {name}")
st.write(f"🎂 **Age:** {age}")
st.write(f"🎨 **Favorite Color:** {color}")