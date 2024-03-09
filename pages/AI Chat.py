import streamlit as st
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.prompts import load_prompt

# Title for your AI resume chatbox
st.title("AshGPT")

# Load OpenAI API key
openai.api_key = st.secrets["openai_api"]

# Initializing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Load and index resume data
@st.cache_resource(show_spinner=False)
def load_data():
    # Path to your CSV file
    data_source = "Aashay_Zende_Info.csv"
    
    # Load resume data from CSV
    loader = CSVLoader(file_path=data_source, encoding="utf-8")
    data = loader.load()
    
    # Create embeddings for your resume data
    embeddings = OpenAIEmbeddings()
    vectors = FAISS.from_documents(data, embeddings)
    
    # Create a retriever for the indexed data
    retriever = vectors.as_retriever()
    
    # Initialize the conversational retrieval chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key),
        retriever=retriever,
        return_source_documents=True,
        verbose=True,
        combine_docs_chain_kwargs={"prompt": "You are a chatbot knowledgeable about Aashay Zende's resume."}
    )
    return chain

chain = load_data()

# Handle user input
prompt = st.chat_input("Ask me anything about my professional experience!")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = chain({"question": prompt})["answer"]
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})