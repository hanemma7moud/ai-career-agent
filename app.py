import os
import streamlit as st
from openai import AzureOpenAI

st.set_page_config(page_title="AI Career Agent", page_icon="🤖", layout="centered")

st.title("💼 Chat with my AI Career Agent")
st.write("Ask me questions about my projects, certifications, or academic background.")

# 1. Fetch secure credentials from environment variables
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_OPENAI_KEY")
AGENT_ID = os.getenv("AZURE_AGENT_ID")

# Ensure keys are present
if not AZURE_ENDPOINT or not AZURE_KEY or not AGENT_ID:
    st.error("Deployment configuration missing. Please verify API keys.")
    st.stop()

# 2. Initialize the standard Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_KEY,
    api_version="2024-10-21-preview" # Framework-compatible version for Agents
)

# 3. Maintain session state for the chat thread
if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Handle live user input
if user_query := st.chat_input("Ask something (e.g., What ML tools do you know?)"):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Send message to the Azure Agent thread
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=user_query
    )

    # Trigger backend RAG/Inference processing
    with st.spinner("Agent is thinking..."):
        run = client.beta.threads.runs.create_and_poll(
            thread_id=st.session_state.thread_id,
            assistant_id=AGENT_ID
        )

    # Stream back result if successful
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=st.session_state.thread_id)
        ai_response = messages.data[0].content[0].text.value
        
        with st.chat_message("assistant"):
            st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
    else:
        st.error("Inference execution timed out or failed.")
