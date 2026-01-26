# --------------------------------------------
# app5.py
# Example 5: Bar Chart – Sales by Product
# --------------------------------------------

import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Sales Bar Chart",
    page_icon="📊",
    layout="centered"
)

# Title & Description
st.title("Bar Chart – Sales by Product")
st.markdown(
    "This example visualizes product-wise sales using a bar chart "
    "and allows users to filter products."
)

st.divider()

# Sample Data
data = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Sales": [120, 300, 180, 90]
})

# Product Selection
selected_products = st.multiselect(
    "Select products to display",
    options=data["Product"].tolist(),
    default=data["Product"].tolist()
)

filtered_data = data[data["Product"].isin(selected_products)]
filtered_data = filtered_data.set_index("Product")

# Visualization
st.subheader("Sales Overview")
st.bar_chart(filtered_data)

# Insight Section
top_product = filtered_data["Sales"].idxmax()
top_sales = filtered_data["Sales"].max()

st.success(f"Top-selling product: {top_product} ({top_sales} units)")

st.info("Bar charts are useful for comparing categorical data.")