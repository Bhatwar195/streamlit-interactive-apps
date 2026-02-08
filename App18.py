# --------------------------------------------
# app18.py
# Example 18: Text Analysis – Sentiment & WordCloud
# --------------------------------------------

import streamlit as st
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Text Analysis Demo",
    page_icon="📝",
    layout="centered"
)

# Title & Description
st.title("Text Analysis — Simple Sentiment & WordCloud")
st.markdown(
    "This example demonstrates **basic text processing**, a **simple sentiment heuristic**, "
    "and **word frequency visualization** using a WordCloud."
)

st.divider()

# Text Input
text = st.text_area(
    "Paste text here",
    "I love Streamlit. It's simple and powerful!"
)

# Simple stop words
stop_words = {"the", "is", "and", "to", "a", "of", "it", "this", "that"}

# Sentiment vocab (toy example)
positive_words = {"love", "good", "great", "nice", "awesome", "easy", "powerful"}
negative_words = {"bad", "hate", "terrible", "hard", "awful"}

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        # Preprocess text
        words = [
            w.lower().strip(".,!?:;()'")
            for w in text.split()
            if w.lower() not in stop_words
        ]

        counts = Counter(words)

        # Word frequency
        st.subheader("🔤 Top Words")
        st.write(counts.most_common(10))

        # Sentiment calculation
        pos = sum(1 for w in words if w in positive_words)
        neg = sum(1 for w in words if w in negative_words)

        sentiment = "Positive 😊" if pos >= neg else "Negative 😐"

        st.subheader("💬 Sentiment Summary")
        st.write(f"**Positive words:** {pos}")
        st.write(f"**Negative words:** {neg}")
        st.success(f"Overall Sentiment: **{sentiment}**")

        # WordCloud
        st.subheader("☁️ WordCloud")
        wc = WordCloud(
            width=500,
            height=250,
            background_color="white"
        ).generate_from_frequencies(counts)

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

st.info(
    "This is a toy NLP example using simple heuristics. "
    "Real sentiment analysis requires trained NLP models."
)
