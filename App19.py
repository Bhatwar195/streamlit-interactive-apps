# --------------------------------------------
# app19.py
# Example 19: Image Upload & Simple Classification Demo
# --------------------------------------------

import streamlit as st
from PIL import Image
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Image Upload & Classifier",
    page_icon="🖼️",
    layout="centered"
)

# Title & Description
st.title("Image Upload & Preview")
st.markdown(
    "This example demonstrates **image upload**, preview, and a **simple "
    "mock classification** based on image brightness. "
    "It can be extended using a real deep learning model."
)

st.divider()

# Image Upload
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # Load image
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Convert to array
    img_array = np.array(img)
    mean_brightness = img_array.mean()

    # Mock classification
    st.subheader("🔍 Prediction")
    if mean_brightness > 120:
        st.success("Mock Prediction: **Bright Image** ☀️")
    else:
        st.warning("Mock Prediction: **Dark Image** 🌙")

    # Show stats
    st.write(f"**Average pixel intensity:** {mean_brightness:.2f}")

else:
    st.info("Please upload an image to preview and classify it.")

st.info(
    "This is a demo classifier. Replace the logic with a "
    "pre-trained CNN (TensorFlow / PyTorch) for real-world use."
)
