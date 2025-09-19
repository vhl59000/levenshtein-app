import streamlit as st
from src.levenshtein import levenshtein_distance

st.set_page_config(page_title="Levenshtein", page_icon="🔤", layout="centered")
st.title("🔤 Levenshtein Distance")

s1 = st.text_input("String 1", value="kitten")
s2 = st.text_input("String 2", value="sitting")

if st.button("Compute distance"):
    d = levenshtein_distance(s1, s2)
    st.success(f"Distance = {d}")
    if max(len(s1), len(s2)) > 0:
        st.write(f"Normalized similarity ≈ {1 - d / max(len(s1), len(s2)):.3f}")
