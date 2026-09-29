import os
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=100
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke(
    "Explain what LangChain is in simple words."
)

print(response.content)