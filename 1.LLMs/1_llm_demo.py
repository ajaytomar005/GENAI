from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


llm=OpenAI(model="GPT-3.5-turbo-Instruct")
result= llm.invoke("Write a poem about the beauty of nature.") 
# // taking string as inpout and returning the output as string//
print(result)