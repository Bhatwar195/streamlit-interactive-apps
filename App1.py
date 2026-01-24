# --------------------------------------------
# app1.py
# Example 1: Hello Streamlit & Basic Widgets
# --------------------------------------------

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered"
)

# Title & Headers
st.title("Hello Streamlit")
st.header("Basic Text and Widget Demo")

st.write("This is a simple introduction to Streamlit. Use the button below:")

# Button Interaction
if st.button("Click Me"):
    st.success("Button clicked successfully!")

# Info Section
st.markdown(
    """
    **Tip:**  
    Streamlit apps automatically update when you modify and save the code.
    """
)