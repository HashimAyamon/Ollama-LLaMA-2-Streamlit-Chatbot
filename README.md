# Ollama-LLaMA-2-Streamlit-Chatbot
A local AI chatbot built using Ollama (LLaMA 2) and Streamlit. Runs fully offline with no API key required.
# 🤖 LLaMA 2 Chatbot using Ollama & Streamlit

A simple and powerful **AI chatbot** built using **Ollama (LLaMA 2)** and **Streamlit**.  
This project runs **100% locally**, requires **no API key**, and works **offline**.

---

## 🚀 Features

- 💬 ChatGPT-style conversational UI
- 🧠 Powered by **LLaMA 2**
- 🖥️ Runs locally using **Ollama**
- 🌐 No internet required after model download
- 🔒 No API keys or paid services
- ⚡ Optional streaming (typing effect)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Ollama**
- **LLaMA 2**
- **Requests**

---

## 📦 Installation


https://ollama.com


Verify installation:
```bash
ollama --version

2️⃣ Download LLaMA 2 Model
ollama pull llama2

3️⃣ Install Python Dependencies
pip install streamlit requests

▶️ Run the Application
streamlit run app.py


Open your browser and visit:

http://localhost:8501

📂 Project Structure
llama2-streamlit-chatbot/
│
├── app.py
├── README.md
└── requirements.txt

📄 requirements.txt
streamlit
requests

🔄 Switch Models (Optional)

You can use other Ollama models easily:

ollama pull mistral
ollama pull llama3
ollama pull codellama


Change model in code:

"model": "mistral"

### 1️⃣ Install Ollama
Download and install Ollama from:
