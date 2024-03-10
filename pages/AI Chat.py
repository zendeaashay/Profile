import openai
import streamlit as st

st.title('AshGPT')
st.title("Aashay's AI Chatbox! Go ahead and ask something...")

# Connect OpenAI key
openai.api_key = st.secrets["openai_api"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define the prompt instruction
prompt_instruction = "You are an AI chatbox and your job is to tell about art."

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Prepend the prompt instruction to the user's input
    full_prompt = f"{prompt_instruction} {prompt}"
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant message in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Simulate stream of response with milliseconds delay
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "user", "content": full_prompt},  # Use full_prompt here
                {"role": "assistant", "content": full_response}
            ],
            stream=True,
        ):
            # Get content in response
            full_response += response.choices[0].delta.get("content", "")
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})