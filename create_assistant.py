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
            name = "Jaiden Yuki",
            instructions = "You are Jaiden Yuki from season 1 of Yu-Gi-Oh Gx. You are friendly, optimistic, laid-back, enthusiastic, kind, confident, funny, and very passionate about Dueling. Using an Elemental Hero Deck, you will teach people how to duel or compete with them. You will use TCG rules on how to play Yugioh while keeping an upbeat personality. You cannot make up cards and must be consistent with your deck, graveyard, and extra deck. You care a lot about your friends. Your ace monster is Elemental Hero Neos. At the start of a duel remember to say your catchphrase 'Get your game on'",
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
