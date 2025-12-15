import streamlit as st
import requests
import json

st.set_page_config(page_title="LLaMA2 Chatbot", layout="centered")
st.title("🤖 LLaMA 2 Chatbot (Ollama)")

OLLAMA_URL = "http://localhost:11434/api/generate"

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare request
    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }

    # Call Ollama
    response = requests.post(
        OLLAMA_URL,
        data=json.dumps(payload)
    )

    result = response.json()["response"]

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": result})
    with st.chat_message("assistant"):
        st.markdown(result)
