
import streamlit as st
import os
from openai import AzureOpenAI


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

st.title("💼 AI Career Agent")

user_input = st.text_input("Ask me something:")

if user_input:
    response = client.chat.completions.create(
        model="career-model",
        messages=[
            {"role": "system", "content": "You are a helpful AI career assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)


