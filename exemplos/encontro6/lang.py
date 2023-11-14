import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

messages = [
    SystemMessage(
        content="Você é um especialista em Python"
    ),
    HumanMessage(
        content="Explique como aplicar um monad em python. De um exmeplo"
    ),
]

print(chat(messages)['content'])
