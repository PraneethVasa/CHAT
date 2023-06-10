import streamlit as st

import openai

# Set up OpenAI API credentials

openai.api_key = "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"

# Define the chatbot function

def chatbot(message):

    response = openai.Completion.create(

        engine="text-davinci-003",

        prompt=message,

        max_tokens=100,

        temperature=0.6,

        n=1,

        stop=None,

    )

    return response.choices[0].text.strip()

# Set the title and description of the web app

st.title("ChatGPT")

st.write("Welcome to the ChatGPT demo! Enter a message and the model will respond.")

# Get user input

message = st.text_input("User Input")

# Handle user input and generate a response

if st.button("Send"):

    if message:

        with st.spinner("Generating response..."):

            response = chatbot(message)

        st.success(response)

    else:

        st.warning("Please enter a message.")

# Add a link to the OpenAI API

st.markdown("[Powered by OpenAI](https://openai.com)")
