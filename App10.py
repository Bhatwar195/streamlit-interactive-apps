# --------------------------------------------
# app10.py
# Example 10: Interactive DataFrame Filtering
# --------------------------------------------

import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

# Page Configuration
st.set_page_config(
    page_title="Iris Data Filter",
    page_icon="🌸",
    layout="centered"
)

# Load Dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Map target values to species names
species_map = dict(enumerate(iris.target_names))
df["species"] = df["target"].map(species_map)

# Title & Description
st.title("Data Filter — Iris Dataset")
st.markdown(
    "This example demonstrates **interactive DataFrame filtering** "
    "using Streamlit widgets on the classic Iris dataset."
)

st.divider()

# Sidebar Filters
st.sidebar.header("Filter Options")

selected_species = st.sidebar.multiselect(
    "Select species",
    options=df["species"].unique(),
    default=df["species"].unique()
)

min_petal_length = st.sidebar.slider(
    "Minimum petal length (cm)",
    min_value=float(df["petal length (cm)"].min()),
    max_value=float(df["petal length (cm)"].max()),
    value=float(df["petal length (cm)"].min())
)

# Filtering Logic
filtered_df = df[
    (df["species"].isin(selected_species)) &
    (df["petal length (cm)"] >= min_petal_length)
]

# Display Results
st.subheader("Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# Summary
st.write(f"**Rows displayed:** {len(filtered_df)}")

st.info("Interactive filtering is a common pattern in data dashboards.")