from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import PyPDF2

# Function to load and display a Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to read PDF and extract text
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

# Initialize the app and chat history
def init_chatbot():
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    st.session_state.messages = []

    # Load resume text from the PDF and set it as a part of session state
    st.session_state.resume_text = extract_text_from_pdf("./data/Aashay Zende - Resume.pdf")

# Function to load and index data
@st.cache_resource(show_spinner=False)
def load_data():
    with open("path/to/your/resume.pdf", "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        doc = Document(content=text)
        # Proceed with creating the ServiceContext and VectorStoreIndex
        service_context = ServiceContext.from_defaults(...)
        index = VectorStoreIndex.from_documents([doc], service_context=service_context)
        return index

# Initialize the chatbot if it's the first time
if "messages" not in st.session_state:
    init_chatbot()

# Display the Lottie animation at the top of the page
lottie_animation_url = 'https://lottie.host/4333fb5c-1feb-490c-ba53-ffc21d1a2d1a/tPyaLx2aD3.json'
lottie_animation_json = load_lottieurl(lottie_animation_url)
if lottie_animation_json:
    st_lottie(lottie_animation_json, height=200, key="initial")

# Display the chatbot UI
st.title("AshGPT Chatbot")
openai.api_key = st.secrets["openai_api"]

# Load and index data
index = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

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

        # Generate response using the chat engine
        response = chat_engine.chat(prompt)
        message_placeholder.markdown(response.response)
        st.session_state.messages.append({"role": "assistant", "content": response.response})