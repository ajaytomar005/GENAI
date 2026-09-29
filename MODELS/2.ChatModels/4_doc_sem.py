from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from numpy import array
load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimension=300)
documents = [
    "Write a poem about the beauty of nature.",
    "Explain what LangChain is in simple words.",
    "What is the difference between LLM and Chat model in LangChain?",
    "What is the difference between LLM and Chat model in LangChain?",
    "What is the difference between LLM and Chat model in LangChain?",
    "Is LangChain a good framework for building chatbots?"
]


embedding_result = embeddings.embed_documents(documents)
query = "What is the difference between LLM and Chat model in LangChain?"
query_embedding = embeddings.embed_query(query)
similarities = cosine_similarity(array(embedding_result), array(query_embedding).reshape(1, -1))
most_similar_index = similarities.argmax()
most_similar_document = documents[most_similar_index]
print("Most similar document:", most_similar_document)
print("Number of documents:", len(embedding_result))
print("Embedding dimension:", len(embedding_result[0]))
print("First embedding:", embedding_result[0])  