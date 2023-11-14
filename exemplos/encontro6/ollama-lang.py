from langchain.llms import Ollama
ollama = Ollama(base_url='http://localhost:11434', model="dexter")
print(ollama("why is the sky blue"))
