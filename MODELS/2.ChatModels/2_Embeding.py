from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Write a poem about the beauty of nature.",
    "Explain what LangChain is in simple words.",
    "What is the difference between LLM and Chat model in LangChain?",
    "What is the difference between LLM and Chat model in LangChain?",
    "What is the difference between LLM and Chat model in LangChain?",
    "What is the difference between LLM and Chat model in LangChain?"
]

embedding_result = embeddings.embed_documents(documents)

print("Number of documents:", len(embedding_result))
print("Embedding dimension:", len(embedding_result[0]))
print("First embedding:", embedding_result[0])