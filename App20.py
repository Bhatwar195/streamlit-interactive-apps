# --------------------------------------------
# app20.py
# Example 20: Interactive Sales Dashboard
# --------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title & Description
st.title("Mini Dashboard — Sales Explorer")
st.markdown(
    "A compact **interactive dashboard** combining data upload, filters, "
    "KPIs, charts, and CSV download."
)

st.divider()

# Data Upload
uploaded_file = st.file_uploader(
    "Upload sales CSV (columns: date, product, region, sales)",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=["date"])
else:
    # Sample fallback data
    dates = pd.date_range("2025-01-01", periods=90)
    df = pd.DataFrame({
        "date": np.random.choice(dates, 300),
        "product": np.random.choice(["A", "B", "C"], 300),
        "region": np.random.choice(["North", "South", "East", "West"], 300),
        "sales": np.random.randint(50, 500, 300)
    })

# Sidebar Filters
st.sidebar.header("Filters")

selected_products = st.sidebar.multiselect(
    "Product",
    options=df["product"].unique(),
    default=df["product"].unique()
)

selected_regions = st.sidebar.multiselect(
    "Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

date_range = st.sidebar.date_input(
    "Date Range",
    value=[df["date"].min(), df["date"].max()]
)

start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])

# Filter Data
filtered_df = df[
    (df["product"].isin(selected_products)) &
    (df["region"].isin(selected_regions)) &
    (df["date"].between(start_date, end_date))
]

# KPI
st.metric("Total Sales", int(filtered_df["sales"].sum()))

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Cumulative Sales Over Time")
    ts = (
        filtered_df
        .sort_values("date")
        .set_index("date")
        .groupby(pd.Grouper(freq="D"))["sales"]
        .sum()
        .cumsum()
    )
    st.line_chart(ts)

with col2:
    st.subheader("📊 Sales by Product")
    prod_sales = filtered_df.groupby("product")["sales"].sum()
    st.bar_chart(prod_sales)

st.divider()

# Data Preview
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(50), use_container_width=True)

# Download
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇️ Download Filtered CSV",
    data=csv_data,
    file_name="filtered_sales.csv",
    mime="text/csv"
)

st.info("This dashboard can be easily adapted to real business datasets.")
