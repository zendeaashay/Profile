import streamlit as st
from streamlit_chat import message

# Setup the page configuration
st.set_page_config(page_title='Welcome to my page!', 
                   page_icon="🏂",
                   layout='wide',
                   initial_sidebar_state="expanded")

# Define the initial state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to handle user input
def handle_user_input():
    if 'user_input' in st.session_state and st.session_state.user_input:
        user_message = st.session_state.user_input
        st.session_state.chat_history.append({'message': user_message, 'is_user': True})
        # Here you should add the response generation logic
        bot_response = "This is a placeholder response."
        st.session_state.chat_history.append({'message': bot_response, 'is_user': False})
        # Clear the input box by resetting the value
        st.session_state.user_input = ""

# Function to clear the chat history
def clear_chat():
    st.session_state.chat_history = []

# User input text box
user_input = st.text_input("Type your message here...", key="user_input", on_change=handle_user_input)

# Display chat messages
for chat in st.session_state.chat_history:
    message(chat['message'], is_user=chat['is_user'])

# Button to clear chat history
if st.button('Clear Chat'):
    clear_chat()
