import streamlit as st
import requests

API_KEY = 'av9hOuNvJJ6lVaEUt1qcOlrO0drP0R46'

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "numResults": 1,
        "maxTokens": 150,
        "temperature": 0.7,
        "topKReturn": 0,
        "topP": 1
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['completions'][0]['data']['text'].strip()
    else:
        return "Sorry, I couldn't generate a response."

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Chattfy")
st.write("Hello! How can I assist you today?")

user_input = st.text_input("You: ", key="input")

if st.button("Send"):
    if user_input.lower() not in ['exit', 'quit', 'bye']:
        response = generate_response(user_input)
        
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Chatbot: {response}")

for message in st.session_state.chat_history:
    st.write(message)

if st.button("Clear Chat"):
    st.session_state.chat_history = []
