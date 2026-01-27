# --------------------------------------------
# app7.py
# Example 7: Matplotlib Integration
# --------------------------------------------

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Matplotlib Integration")

x = np.linspace(0, 10, 200)
y = np.sin(x)

# ✅ CORRECT FUNCTION
fig, ax = plt.subplots()
ax.plot(x, y, lw=2)
ax.set_xlabel("X")
ax.set_ylabel("sin(x)")
ax.grid(True)

st.pyplot(fig)