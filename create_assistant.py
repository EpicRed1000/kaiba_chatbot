# Creating the assistant
# create_assistant.py
import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Getting Enviormental varible
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Creating the Assistant Id
def create_assistant():
    try:
        assistant = client.beta.assistants.create(
            name = "Kaiba bot",
            instructions = "You are Kaiba from Yu-Gi-Oh! Your job is to sound just like him",
            tools = [{"type":"code_interpreter"}],
            model = "gpt-4o-mini"
            )
        return assistant
    except Exception as e:
        st.error(f'error creating assistant: {str(e)}')
        return None
    
# Creating the Thread id
def create_thread():
    try:
        thread = client.beta.threads.create()
        return thread
    except Exception as e:
        st.error(f'error creating thread: {str(e)}')
        return None

if __name__ == "__main__":
    assistant = create_assistant()
    thread = create_thread()
    if assistant:
        print(f'Assistant Id {assistant.id}')
    else:
        print('fail to create assistant id')
    if thread:
        print(f'Thread Id {thread.id}')
    else:
        print('fail to create thread id')
