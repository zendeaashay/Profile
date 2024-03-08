from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
import streamlit as st
import requests
import PyPDF2
import os

# Function to load and display a lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to read PDF and extract the text
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

# Function to initialize the chatbot messages
def init_chatbot():
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    st.session_state.messages = []
    st.session_state.resume_text = extract_text_from_pdf("Aashay Zende - Resume.pdf")

# Initialize the chatbot if it's the first time
if "messages" not in st.session_state:
    init_chatbot()

# Display the lottie animation at the top of the page
lottie_animation_url = 'https://lottie.host/4333fb5c-1feb-490c-ba53-ffc21d1a2d1a/tPyaLx2aD3.json'
lottie_animation_json = load_lottieurl(lottie_animation_url)
if lottie_animation_json:
    st_lottie(lottie_animation_json, height=200, key="initial")

# Display the chatbot UI
st.title("AshGPT Chatbot")
openai.api_key = st.secrets["openai_api"]

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
prompt = st.chat_input("Ask me anything about my professional experience!")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        # Respond with resume text if the user asks about professional experience
        if "professional experience" in prompt.lower():
            full_response = st.session_state.resume_text
        else:
            # Use LLM to generate a response for other questions
            full_response = openai.Completion.create(
                model=st.session_state["openai_model"],
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )["choices"][0]["message"]["content"]

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
