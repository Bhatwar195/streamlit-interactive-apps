# --------------------------------------------
# app16.py
# Example 16: Iris ML Classifier with Probabilities
# --------------------------------------------

import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Page Configuration
st.set_page_config(
    page_title="Iris ML Classifier",
    page_icon="🌸",
    layout="centered"
)

# Title & Description
st.title("Iris Classifier (with Probabilities)")
st.markdown(
    "This example demonstrates a **complete ML inference workflow** in Streamlit: "
    "feature input → model prediction → probability visualization."
)

st.divider()

# Load Dataset
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target
target_names = iris.target_names

# Sidebar Inputs
st.sidebar.header("Input Features")

def user_input_features():
    data = {}
    for col in X.columns:
        data[col] = st.sidebar.slider(
            col,
            float(X[col].min()),
            float(X[col].max()),
            float(X[col].mean())
        )
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Cache Model Training
@st.cache_resource
def train_model():
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X, y)
    return model

model = train_model()

# Prediction
prediction = model.predict(input_df)[0]
prediction_proba = model.predict_proba(input_df)[0]

# Display Inputs
st.subheader("🔢 Input Features")
st.dataframe(input_df, use_container_width=True)

# Prediction Output
st.subheader("🌼 Prediction")
st.success(f"Predicted Species: **{target_names[prediction]}**")

# Probability Output
proba_df = pd.DataFrame(
    prediction_proba.reshape(1, -1),
    columns=target_names
)

st.subheader("📊 Prediction Probabilities")
st.bar_chart(proba_df)

st.info(
    "The model is trained once and cached using `st.cache_resource` "
    "to avoid retraining on every interaction."
)
