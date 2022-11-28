import streamlit as st
import time
st.markdown("# 🦇 Fake news bat")
st.markdown(" Online fake news detector.")
st.text_input(
        label="👉 Pace your URL here to check if it contains fake news...",
        key="label",
        label_visibility="visible")
result = st.button('Ask the bat ℹ️')

if result:
    with st.spinner('🧠 Shhht. Let her think...'):
        time.sleep(5)
        st.success('Okay, she got it! ✅')
