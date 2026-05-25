import os
import streamlit as st
from openai import AzureOpenAI

st.set_page_config(page_title="AI Career Agent", page_icon="🤖")

st.title("💼 Chat with my AI Career Agent")
st.write("Ask me about my projects, skills, and experience.")

# Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = "AI-Career-Agent"  # change if needed

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("Ask me anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are an AI career assistant that answers questions about Hanem's background, projects, and skills."},
            *st.session_state.messages
        ]
    )

    reply = response.choices[0].message.content

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
