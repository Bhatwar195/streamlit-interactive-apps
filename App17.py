# --------------------------------------------
# app17.py
# Example 17: Linear Regression (Synthetic House Prices)
# --------------------------------------------

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Linear Regression Demo",
    page_icon="📉",
    layout="centered"
)

# Title & Description
st.title("Linear Regression — House Price (Synthetic)")
st.markdown(
    "This example demonstrates a **simple regression workflow**: "
    "generate synthetic data → fit a linear model → visualize predictions."
)

st.divider()

# User Control
np.random.seed(0)
n_points = st.slider(
    "Number of data points",
    min_value=20,
    max_value=300,
    value=100,
    step=10
)

# Generate Synthetic Data
X = np.random.rand(n_points, 1) * 50 + 50   # Size in square meters
y = 2000 + 50 * X.flatten() + np.random.randn(n_points) * 1000

df = pd.DataFrame({
    "Size (sqm)": X.flatten(),
    "Price": y
})

# Cache Model Training
@st.cache_resource
def train_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_regression(X, y)
pred_y = model.predict(X)

# Metrics
r2 = r2_score(y, pred_y)

# Visualization (sort for clean line)
sort_idx = np.argsort(X.flatten())

fig, ax = plt.subplots()
ax.scatter(df["Size (sqm)"], df["Price"], alpha=0.6, label="Data")
ax.plot(
    X.flatten()[sort_idx],
    pred_y[sort_idx],
    color="red",
    lw=2,
    label="Regression Line"
)
ax.set_xlabel("Size (sqm)")
ax.set_ylabel("Price")
ax.set_title("House Price vs Size")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Model Summary
st.subheader("📊 Model Summary")
st.write(f"**Coefficient (price per sqm):** {model.coef_[0]:.2f}")
st.write(f"**Intercept:** {model.intercept_:.2f}")
st.write(f"**R² Score:** {r2:.3f}")

st.info(
    "This is a synthetic example meant to demonstrate regression concepts "
    "and visualization, not a real pricing model."
)
