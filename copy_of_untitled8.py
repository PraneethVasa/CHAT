import streamlit as st

import openai

# Set up OpenAI API credentials
st.caption("Praneeth")
openai.api_key = "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"

# Define the chatbot function

def chatbot(message):

    response = openai.Completion.create(

        engine="text-davinci-003",

        prompt=message,

        max_tokens=1000,

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
