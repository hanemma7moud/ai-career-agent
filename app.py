import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

response = client.chat.completions.create(
    model=os.getenv("DEPLOYMENT_NAME"),  # IMPORTANT
    messages=[
        {"role": "system", "content": "You are a helpful AI career assistant."},
        {"role": "user", "content": "Tell me what you can help with"}
    ]
)

print(response.choices[0].message.content)
