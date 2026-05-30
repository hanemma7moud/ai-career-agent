# 🤖 AI Career Agent (AI-900 Project Showcase)

Welcome to the **AI Career Agent** template repository! This project is a hands-on implementation designed for students and developers to move beyond theory and build a live, industry-grade portfolio piece. 

This framework leverages **Microsoft Foundry (2026 Standards)**, **Retrieval-Augmented Generation (RAG)**, and **Streamlit** to create an interactive, autonomous chat assistant grounded entirely in your professional CV.

🚀 **Live Demo Reference:** [Check out my live profile agent here!]([https://github.com/hanemma7moud](https://hanem-ai-agent.streamlit.app/))

---

## 🛠 Features
- **Semantic Data Grounding:** Uses your CV as a knowledge base to prevent AI hallucinations.
- **2026 Framework Alignment:** Built using the native **Microsoft Foundry** ecosystem and OpenAI deployment infrastructure.
- **Secure Secret Management:** Fully integrates with Streamlit's encrypted `secrets.toml` architecture to keep cloud keys hidden.
- **Frictionless UI:** Streamlit interface crafted for recruiters to seamlessly navigate your technical achievements.

---

## 🎁 Quickstart Guide for Students (Fork & Deploy)

Follow these exact steps to launch your own personalized Career Agent for free using your **Azure for Students** credits.

### Step 1: Fork and Star this Repository
1. Click the **⭐ Star** button in the top-right corner of this page to save it.
2. Click the **Fork** button to generate an identical copy of this project directly inside your own GitHub profile.

### Step 2: Upload Your Agent-Ready CV
1. Navigate to the `data/` directory (or the root directory) in your forked repository.
2. Replace the placeholder curriculum vitae file with your own details. 
3. Ensure you follow the modular semantic headers (`## Technical Skills`, `## Key AI Projects`) so the retrieval engine parses your context perfectly.

### Step 3: Harvest Your Microsoft Foundry Credentials
1. Log into **Microsoft Foundry** ([ai.azure.com](https://ai.azure.com)) using your university credentials.
2. Navigate to your deployed project endpoint (e.g., `gpt-4o-mini`).
3. Copy your specific connection keys:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_KEY`
   - `AZURE_OPENAI_MODEL_DEPLOYMENT_NAME`

### Step 4: Deploy Instantly to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and log in using your GitHub account.
2. Click **New app**, then select your forked repository: `[Your-Username]/ai-career-agent`.
3. Set your main file path to `app.py`.
4. **⚠️ CRITICAL (Security Step):** Before hitting deploy, click **Advanced Settings** and inject your Azure credentials securely into the Secrets panel:
   ```toml
   AZURE_OPENAI_ENDPOINT = "[https://your-resource-name.openai.azure.com/](https://your-resource-name.openai.azure.com/)"
   AZURE_OPENAI_KEY = "your-40-character-secret-key"
   AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "your-model-deployment-name"
