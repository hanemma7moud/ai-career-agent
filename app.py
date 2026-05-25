import os
import streamlit as st
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


st.set_page_config(page_title="AI Career Agent", page_icon="🤖", layout="centered")

st.title("💼 Chat with my AI Career Agent")
st.write("Ask me questions about my projects, certifications, or academic background.")

# 1. Fetch configurations from Environment Variables
FOUNDRY_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT") # e.g., https://<your-resource>.services.ai.azure.com
AGENT_ID = os.getenv("AZURE_AGENT_ID")                 # e.g., AI-Career-Agent:5

if not FOUNDRY_ENDPOINT or not AGENT_ID:
    st.error("Configuration variables missing. Please check your environment variables settings.")
    st.stop()

# 2. Initialize the Native Project Client using Entra ID 
@st.cache_resource
@st.cache_resource
def get_project_client():
    credential = DefaultAzureCredential()

    return AIProjectClient(
        subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"),
        resource_group_name=os.getenv("AZURE_RESOURCE_GROUP"),
        project_name=os.getenv("AZURE_PROJECT_NAME"),
        credential=credential
    )

project_client = get_project_client()

# 3. Maintain session state thread ID natively via nested Foundry namespace
if "thread_id" not in st.session_state:
    thread = project_client.agents.create_thread()
    st.session_state.thread_id = thread.id

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display historical conversation messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Handle live user queries
if user_query := st.chat_input("Ask something about my machine learning background..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Append user input message into the live thread context
    project_client.agents.create_message(
        thread_id=st.session_state.thread_id,
        role="user",
        content=user_query
    )

    # Execute backend agent inference processing using the nested runs namespace
    with st.spinner("Agent is analyzing your request..."):
        run = project_client.agents.create_and_process_run(
            thread_id=st.session_state.thread_id,
            agent_id=AGENT_ID
        )

    # Retrieve answer payloads once execution successfully completes
    if run.status == "completed":
        messages = project_client.agents.list_messages(thread_id=st.session_state.thread_id)
        
        # Get latest assistant message safely
        ai_response = None
        for msg in reversed(messages.data):
            if msg.role == "assistant":
                ai_response = msg.content[0].text.value
                break

        # Pull the latest text block value safely from the message payload data array
        ai_response = messages.data[0].content[0].text.value
        
        with st.chat_message("assistant"):
            st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
    else:
        st.error(f"Inference execution failed with status: {run.status}")
