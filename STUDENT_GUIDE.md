
# 🚀 AI Career Agent — Student Guide

Welcome! In this lab, you will build and customize your own **AI Career Agent** using **Azure OpenAI + Streamlit**.

By the end of this guide, you will:
✅ Run the AI agent locally  
✅ Connect it to your own Azure account  
✅ Customize it for your career interests  
✅ Publish your own version  

---


## 📌 Overview
This project is a customizable AI assistant that helps with:
* **Career advice:** Automated guidance tailored to industry trends.
* **Resume feedback:** Evaluation based on targeted keyword match criteria.
* **Skill development:** Step-by-step custom training roadmaps.
* **Job preparation:** Mock interview question generation.

You will fork this template project and turn it into your own personalized portfolio piece.

---

## 🟢 Step 1: Fork the Repository

1. Go to the base repository: 👉 [hanemma7moud/ai-career-agent](https://github.com/hanemma7moud/ai-career-agent)
2. Click **Fork** (top-right corner) to create a copy in your own GitHub account.
3. Clone your forked repository to your local computer:

git clone https://github.com/YOUR-USERNAME/ai-career-agent.git
cd ai-career-agent

---

🟢 Step 2: Create Your Azure Resources
You will need an Azure Student Subscription.
✅ Create Azure OpenAI Resource



Go to 👉 https://portal.azure.com


Create:

Resource Group
Azure OpenAI resource



Inside your OpenAI resource:

Go to Model Deployments
Deploy a model such as:

gpt-4o (recommended)
or any available model






🔑 Copy Your Credentials
You will need:

API Key
Endpoint
Deployment Name


🟢 Step 3: Configure Environment Variables
Create a .env file in the root of your project:

AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your_model_name
``
⚠️ Important: Never commit your .env file to GitHub.

🟢 Step 4: Install Dependencies
Make sure you have Python installed (>=3.9 recommended)
Then run:
Shellpip install -r requirements.txtShow more lines

🟢 Step 5: Run the Application
Start the Streamlit app:
Shellstreamlit run app.pyShow more lines
Then open:
👉 http://localhost:8501
🎉 You should now see your AI Career Agent running!

🟢 Step 6: Customize Your AI Agent
This is the most important step 🚀

🎯 1. Modify the AI Behavior (Prompt)
Find where the system prompt is defined (e.g. in app.py or agent.py).
Example:
PythonSYSTEM_PROMPT = "You are a helpful AI career advisor."Show more lines
✨ Try changing it to:

Cybersecurity mentor
Data science coach
Software engineering career guide
Resume reviewer


🎯 2. Personalize for Your Career
Update the agent to focus on:

Your degree
Your career goals
Your interests

Example:
Python"You are a career coach helping computer science students prepare for backend engineering roles."Show more lines

🎯 3. Add New Features (Optional Challenges)
Try implementing:
✅ Resume feedback
✅ Skill gap analysis
✅ Career roadmap generator
✅ Interview question generator

🎯 4. Improve the UI
Edit the Streamlit interface:

Add titles
Add sections
Improve layout


🟢 Step 7: Save & Push to GitHub
After making changes:
Shellgit add .git commit -m "Customized my AI Career Agent"git push origin mainShow more lines

🟢 Step 8: Deploy Your App
✅ Option 1: Streamlit Community Cloud

Go to 👉 https://streamlit.io/cloud
Connect your GitHub account
Select your repo
Deploy 🚀


✅ Option 2: Azure (Advanced)
Deploy using:

Azure App Service
Or Container Apps


🟢 Step 9: Share Your Work 🎉
Submit:
✅ Your GitHub repo link
✅ (Optional) Live deployed app
✅ (Optional) Short demo video (1–2 min)

✅ Checklist
Mark your progress:
Markdown- [ ] Forked the repo  - [ ] Created Azure OpenAI resource  - [ ] Configured `.env` file  - [ ] Ran the app locally  - [ ] Customized the AI agent  - [ ] Pushed changes to GitHub  - [ ] Deployed the app (optional)  Show more lines

💡 Ideas for Customization
You can turn this into:

🎓 Student advisor
💼 Job application assistant
🧠 Study coach
🔐 Cybersecurity mentor
📊 Data science guide


🧑‍🏫 Need Help?
If you get stuck:

Check the README
Review your Azure credentials
Ask your instructor


🚀 Final Goal
By completing this lab, you will have:
✅ A working AI-powered application
✅ Experience with Azure OpenAI
✅ A project for your portfolio
