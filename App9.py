# --------------------------------------------
# app9.py
# Example 9: Map Visualization with Latitude & Longitude
# --------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Map Visualization",
    page_icon="🗺️",
    layout="centered"
)

# Title & Description
st.title("Map Visualization: Random Locations")
st.markdown(
    "This example plots randomly generated geographic points on a map "
    "using Streamlit’s built-in mapping functionality."
)

st.divider()

# User Controls
num_points = st.slider(
    "Select number of points",
    min_value=10,
    max_value=500,
    value=100,
    step=10
)

city = st.selectbox(
    "Select city",
    ["San Francisco", "New York", "London"]
)

# City Coordinates
city_coords = {
    "San Francisco": (37.76, -122.4),
    "New York": (40.71, -74.0),
    "London": (51.50, -0.12)
}

lat_center, lon_center = city_coords[city]

# Data Generation
df = pd.DataFrame({
    "lat": lat_center + np.random.randn(num_points) * 0.02,
    "lon": lon_center + np.random.randn(num_points) * 0.02
})

# Map Visualization
st.subheader("Map View")
st.map(df)

st.info("Streamlit uses deck.gl under the hood for fast and interactive maps.")