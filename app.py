import streamlit as st
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 1. Page Configuration & Custom Theme Styling
st.set_page_config(
    page_title="AI Career Agent - Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Setup Secure Azure Credentials
# To avoid hardcoding credentials, we read them from environment variables.
# When deploying to streamlit.app, configure these in the "Secrets" settings!
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://csc300-cv.services.ai.azure.com/api/projects/CVAssistant")
AZURE_AGENT_NAME = os.getenv("AZURE_AGENT_NAME", "AI-Career-Agent")
AZURE_AGENT_VERSION = os.getenv("AZURE_AGENT_VERSION", "5")

# Optional: Set local environment fallback credentials for local testing
# DO NOT commit actual keys or passwords to GitHub!
if "AZURE_TENANT_ID" not in os.environ:
    # Streamlit Cloud injects secrets directly into environment variables.
    # If running locally, you can load them from a local .env file.
    pass

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
        # DefaultAzureCredential will automatically pick up:
        # 1. AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID in Streamlit Secrets
        # 2. Or managed identity credentials when deployed in Azure
        credential = DefaultAzureCredential()
        client = AIProjectClient(
            endpoint=AZURE_ENDPOINT,
            credential=credential
        )
        return client
    except Exception as e:
        st.error(f"Failed to authenticate with Azure AI: {e}")
        st.info("💡 Did you configure your Streamlit Secrets? Check the setup guide below!")
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
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Query Azure AI Agent
    if client:
        with st.chat_message("assistant"):
            with st.spinner("Consulting Dr. Hanem's CV & Knowledge Base..."):
                try:
                    # Get OpenAI client from Azure project
                    openai_client = client.get_openai_client()
                    
                    # Call the custom agent configured in Azure AI Foundry
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
