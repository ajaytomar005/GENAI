from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()

chat=Anthropic(model="claude-v1",temperature=0.7,max_completion_tokens=1000)
chat_result= chat.invoke("Write a poem about the beauty of nature.")
# not getting the output as string, instead getting the output as list of messages.
print(chat_result)