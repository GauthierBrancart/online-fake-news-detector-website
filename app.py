import os
import streamlit as st
import requests

# BASE_URI = "https://dockerapi-6uhfgb5xra-ew.a.run.app/"
# BASE_URI = os.getenv('BASE_URI')
BASE_URI = st.secrets['BASE_URI']
# st.write(BASE_URI)
# st.write(st.secrets)

st.markdown("# 🦇 Ask the bat")
st.markdown(" Online fake news detector.")

url_input = st.text_input(
        label="👉 Pace your URL here to check if it contains fake news...",
        key="label",
        label_visibility="visible")

if st.button('Ask the bat ℹ️'):
    if not url_input[:4] == 'http' and len(url_input) < 100:
        st.warning("Your input does not have enough content for the bat to evaluate.\nPlease provide a longer input.")
    else:
        with st.spinner('🧠 Shhht. Let her think...'):
            params = {"text_or_url": url_input}
            url = f"{BASE_URI}/pred"
            response = requests.get(url=url, params=params).json()

        st.success(response)
