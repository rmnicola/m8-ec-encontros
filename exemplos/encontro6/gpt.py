import os
import openai
from dotenv import load_dotenv

load_dotenv()

def chat_with_gpt(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou outro modelo
        messages=[
            {"role": "system", "content": "Você é um especialista em Python"},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message['content']

# Exemplo de uso
print(chat_with_gpt("Explique para que serve o partial. Dê um exemplo"))
