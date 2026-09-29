from langchain_openai import ChatOpenAI
# differnce between llm and chat is that llm is taking string as input and returning the output as string, whereas chat is not getting the output as string, instead getting the output as list of messages.
# about models diferfernce we are imorting the same model "GPT-3.5-turbo-Instruct" in both llm and chat, but the way they handle input and output is different.
from dotenv import load_dotenv
load_dotenv()

chat=ChatOpenAI(model="GPT-3.5-turbo-Instruct",temperature=0.7,max_completion_tokens=1000)
# temperature means the randomness of the output, higher temperature means more random output, lower temperature means more deterministic output.


chat_result= chat.invoke("Write a poem about the beauty of nature.")
# not getting the output as string, instead getting the output as list of messages.
print(chat_result)
# result will be like this:
# [{'role': 'assistant', 'content': 'Nature is a wondrous sight,\n
print(chat_result[0]['content']) # to get the output as string, we can access the content of the first message in the list.