import streamlit as st
import time
import requests
from GEofnd.interface.main import predict
st.markdown("# 🦇 Ask the bat")
st.markdown(" Online fake news detector.")
url_input = st.text_input(
        label="👉 Pace your URL here to check if it contains fake news...",
        key="label",
        label_visibility="visible")
url = "http://127.0.0.1:8000"
response = requests.get(url=url, params="url").json
result = st.button('Ask the bat ℹ️')

if result:
    with st.spinner('🧠 Shhht. Let her think...'):
        time.sleep(5)
        st.success(f'{predict(url_input)}')
        st.markdown(f"The information provided by this link is {predict} ")
