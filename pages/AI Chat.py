#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:13:26 2024

@author: aashayzende
"""
import streamlit as st
from streamlit_chat import message

# Initialize chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to handle user input
def handle_user_input():
    user_input = st.text_input("Type your message here...", key="user_input")
    if user_input:
        st.session_state.chat_history.append({'message': user_input, 'is_user': True})
        # Here you should add the response generation logic
        bot_response = "This is a placeholder response."
        st.session_state.chat_history.append({'message': bot_response, 'is_user': False})
        # Clear the text input
        st.session_state.user_input = ""

# Display chat messages
for chat in st.session_state.chat_history:
    message(chat['message'], is_user=chat['is_user'])

# Input for new messages
handle_user_input()