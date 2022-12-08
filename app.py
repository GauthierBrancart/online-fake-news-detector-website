import streamlit as st
import requests

st.markdown("# 🦇 Ask the bat")
st.markdown(" Online fake news detector.")

url_input = st.text_input(
        label="👉 Pace your URL here to check if it contains fake news...",
        key="label",
        label_visibility="visible")


if st.button('Ask the bat ℹ️'):
    with st.spinner('🧠 Shhht. Let her think...'):
        params = {"text_or_url": url_input}
        BASE_URI = "http://localhost:8080"
        url = f"{BASE_URI}/pred"
        response = requests.get(url=url, params=params).json()

    st.success(response)
