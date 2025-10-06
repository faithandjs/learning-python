import streamlit as st

st.title("My First Python Web App 🚀")
st.write("Hello, world! This is running in my browser.")

name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome, {name}!")
