from GPT_ChatBot import *
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

import streamlit as st
import time

st.set_page_config(page_title="An LLM-powered Streamlit app")

st.title('🎈 Mental Health Chat Bot')

st.write('Ask Any Question:')


# Sidebar contents
with st.sidebar:
    st.title('👩‍⚕️💬 Mental Health App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [Open AI Chat-GPT](<https://platform.openai.com/docs/api-reference>)
    
    
    💡 
    ''')
    add_vertical_space(20)
    st.write('Made by Haneesha')



# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm Mental Health Chat Bot, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']




# Layout of input/response containers
response_container = st.container()
colored_header(label='', description='', color_name='blue-30')
input_container = st.container()




# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", key="input",value="",placeholder="Chat Here....")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()
    submit = st.button("Submit")



# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    
    #chatbot = hugchat.ChatBot()
    #response = chatbot.chat(prompt)
    return click(prompt)

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))