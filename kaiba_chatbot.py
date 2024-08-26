# kaiba_chatbot.py
import streamlit as st
import openai
import time
import os

# Setup Page
st.set_page_config(page_title="Kaiba Chatbot", page_icon = ":briefcase:", layout="wide")
ASSISTANT_ID = "asst_6xBZUgAoRz3cIetRy8WgtNnY"
THREAD_ID = "thread_4iznOMw92EXHBgcyNwpPPWeu"

# Openai Client
api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error('OpenAi API Key was not found. Please set it in Streamlit secrets or as an enviromental varible')
    st.stop()
client = openai.OpenAI(api_key=api_key)

# Creating Chat

st.image('data:image/png;base64,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')
st.title("Kaiba Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

# responses
def get_assistant_response(assistant_id,thread_id, user_input):
    try:
        # user message
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
            )

        # Thinking
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
            )
        
        # Waiting
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status == 'completed':
                break
            time.sleep(1)

        # Responses
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        # Latest Response
        return messages.data[0].content[0].text.value
    except Exception as e:
        st.error(f'Error getting assistant reponse: {str(e)}')
        return "I'm sorry, but an error occurred while processing your request."

# Displaying Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User And Ai responses
prompt = st.chat_input("Ask me anything!")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = get_assistant_response(
            ASSISTANT_ID,
            THREAD_ID,
            prompt
            )
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant","content":full_response})

# Display Id
st.sidebar.write(f'Assistant ID: {ASSISTANT_ID}')
st.sidebar.write(f'Thread ID: {THREAD_ID}')




        

    
