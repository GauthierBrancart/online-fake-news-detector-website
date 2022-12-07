import streamlit as st
import requests
import time

st.markdown("# 🦇 Ask the bat")
st.markdown(" Online fake news detector.")

url_input = st.text_input(
        label="👉 Pace your URL here to check if it contains fake news...",
        key="label",
        label_visibility="visible")

params = {"text_or_url": url_input}
BASE_URI = "https://dockerapi-6uhfgb5xra-ew.a.run.app"
url = f"{BASE_URI}/pred"
response = requests.get(url=url, params=params).json()

result = st.button('Ask the bat ℹ️')

if result:
    with st.spinner('🧠 Shhht. Let her think...'):
        time.sleep(5)
        st.success(response)
