import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct-v0.3",
    messages=[
        {"role": "user", "content": "what is photosynthesis?"}
    ],
    max_tokens=1024
)

print(response.choices[0].message.content)