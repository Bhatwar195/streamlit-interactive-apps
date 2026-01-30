# --------------------------------------------
# app11.py
# Example 11: Form Submission (Batch Input)
# --------------------------------------------

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Form Submission Example",
    page_icon="📝",
    layout="centered"
)

# Title & Description
st.title("Form Example")
st.markdown(
    "This example demonstrates how to use **Streamlit forms** to collect "
    "multiple inputs and process them only after submission."
)

st.divider()

# Form
with st.form("order_form"):
    name = st.text_input("Customer Name")
    quantity = st.number_input(
        "Quantity",
        min_value=1,
        max_value=100,
        value=1
    )
    submitted = st.form_submit_button("Place Order")

# Form Processing
if submitted:
    if name.strip():
        st.success(f"✅ Order placed successfully: **{name} × {quantity}**")
    else:
        st.error("❌ Please enter a valid name before submitting.")

st.info("Forms are useful when you want to submit multiple inputs together.")