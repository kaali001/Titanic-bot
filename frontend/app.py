import streamlit as st
import requests

st.title("Titanic Dataset Chatbot 🚢")

user_input = st.text_input("Ask a question about the Titanic dataset:")

if st.button("Submit"):
    response = requests.get(f"http://127.0.0.1:8000/query?question={user_input}").json()
    
    if "response" in response:
        st.write(response["response"])
    
    if "image" in response and response["image"]:
        st.image(response["image"])
