import streamlit as st
import os
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.projects import AIProjectClient

# 1. Page Configuration & Custom Theme Styling
st.set_page_config(
    page_title="AI Career Agent - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Setup Secure Azure Credentials
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://csc300-cv.services.ai.azure.com/api/projects/CVAssistant")
AZURE_AGENT_NAME = os.getenv("AZURE_AGENT_NAME", "AI-Career-Agent")
AZURE_AGENT_VERSION = os.getenv("AZURE_AGENT_VERSION", "5")

# Bypasses restricted University tenant permission blocks (401 errors)
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "")

st.title("💼 Dr. Hanem Ellethy - AI Career Agent")
st.subheader("Interactive Professional Portfolio & CV Assistant")

st.markdown(
    """
    Welcome! This conversational agent is powered by **Azure AI Foundry** and represents 
    **Dr. Hanem Ellethy**, an expert Data Scientist, AI Engineer, and University Lecturer. 
    Feel free to ask questions about research, publications, teaching philosophy, or industry collaborations.
    """
)

# Initialize Azure AI Project Client safely
@st.cache_resource
def get_project_client():
    try:
        # If student has restricted university tenant, use direct API Key authentication
        if AZURE_API_KEY:
            credential = AzureKeyCredential(AZURE_API_KEY)
        else:
            # Default fallback for standard subscriptions
            credential = DefaultAzureCredential()
            
        client = AIProjectClient(
            endpoint=AZURE_ENDPOINT,
            credential=credential
        )
        return client
    except Exception as e:
        st.error(f"Failed to authenticate with Azure AI: {e}")
        st.info("💡 **Student Tip:** If your university tenant blocks App Registration, please use the **Azure API Key** method instead of Microsoft Entra ID!")
        return None

client = get_project_client()

# 3. Chat Session State Management
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am Dr. Hanem Ellethy's AI Career Agent. Ask me anything about my academic work, AI research, or teaching experience."}
    ]

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle Live User Input & Azure Agent Querying
if user_input := st.chat_input("Ask me about Dr. Hanem's qualifications..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    if client:
        with st.chat_message("assistant"):
            with st.spinner("Consulting Dr. Hanem's CV & Knowledge Base..."):
                try:
                    openai_client = client.get_openai_client()
                    
                    response = openai_client.responses.create(
                        input=[{"role": "user", "content": user_input}],
                        extra_body={
                            "agent_reference": {
                                "name": AZURE_AGENT_NAME,
                                "version": AZURE_AGENT_VERSION,
                                "type": "agent_reference"
                            }
                        }
                    )
                    
                    output_text = response.output_text
                    st.markdown(output_text)
                    st.session_state.messages.append({"role": "assistant", "content": output_text})
                except Exception as e:
                    error_msg = f"Error querying agent: {e}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": "Sorry, I encountered an error communicating with the Azure AI model. Please check the credentials."})
    else:
        st.warning("Azure client not initialized. Please configure secrets.")
