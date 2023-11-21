---
title: LCEL
sidebar_position: 3
---
import Admonition from '@theme/Admonition';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> LCEL

Espero que eu tenha conseguido explicar bem `o que` faz o LangChain e tenha
sido convincente sobre o `por que` de usarmos uma ferramenta como ele, pois
agora vamos para o `como`.

Na semana passada, exploramos alguns exemplos simples utilizando o Langchain.
Dessa vez, vamos olhar para o abismo de mais uma abstração desnecessariamente
complexa: o LangChain Expression Language (LCEL).

Não vou ficar reproduzindo exatamente o que é dito na documentação do
LangChain. Se quiser ver a explicação canônica, vai [até lá e
leia](https://python.langchain.com/docs/expression_language/). Aqui eu vou só
explicar o motivo de eu seguir no meu material utilizando essa linguagem em vez
de continuar no modo "antigo" de se trabalhar com o Langchain. Seguem os meus
principais motivos:

1. Suporte à chamadas assíncronas com mais facilidade;
2. Linguagem mais sucinta para trabalhar com o `Streamable callback`; e 
3. Material preparado para o futuro. É. Eu não quero ter que reescrever isso
   aqui =P

## 1. Chain simples

Vamos começar com o encadeamento mais simples possível:

```
input ---> [prompt] ---> [modelo] ---> output
```

Em todos os nossos exemplos, vamos usar majoritariamente o `stream`, pois é o
que acredito fazer mais sentido para a nossa aplicação.

O protocolo utilizado como base para quase tudo no LCEL é o `Runnable`. Com
ele, é possível encadear etapas de uma corrente e até mesmo executá-las de uma
forma relativamente sucinta. Vamos ver o exemplo mais básico:

<Tabs defaultValue="openai" values={[
        {label: 'OpenAI', value: 'openai'},
        {label: 'Ollama', value: 'ollama'},
  ]}>

<TabItem value="openai">

```python showLineNumbers title="simple-chain.py"
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template(
"""
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. For each item, create a simple sentence
justifying this choice.
"""
)

chain = prompt | model

for s in chain.stream({"activity": "eat live fish"}):
    print(s.content, end="", flush=True)
```

</TabItem>

<TabItem value="ollama">

```python showLineNumbers title="simple-chain-ollama.py"
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

model = Ollama(model="mistral")
prompt = ChatPromptTemplate.from_template(
"""
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. For each item, create a simple sentence
justifying this choice.
"""
)

chain = prompt | model

for s in chain.stream({"activity": "eat live fish"}):
    print(s, end="", flush=True)
```

</TabItem>

</Tabs>

:::caution Aviso

Para poder usar o código acima com a API da OpenAI, lembre-se de configurar a
sua chave de API no sistema.

:::

## 2. Encadeando múltiplos modelos

Agora vamos recriar o nosso exemplo com o `tradutor` e o agente:

<Tabs defaultValue="openai" values={[
        {label: 'OpenAI', value: 'openai'},
        {label: 'Ollama', value: 'ollama'},
  ]}>

<TabItem value="openai">

```python showLineNumbers title="travel-agent.py"
from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

model1 = ChatOpenAI(model="gpt-3.5-turbo")
model2 = ChatOpenAI(model="gpt-4")

prompt1 = ChatPromptTemplate.from_template("""
Apenas traduza o texto a seguir:
{text}
"""
)

prompt2 = ChatPromptTemplate.from_template( """
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. Only respond with the list of 5 items, no
summarizing statement, forewords or warnings or even explanations are required.
"""
)

chain1 = prompt1 | model1

chain2 = {"activity": chain1} | prompt2 | model2

chain3 = {"text": chain2} | prompt1 | model1

for s in chain3.stream({"text": "caminhar na praia"}):
    print(s.content, end="", flush=True)
print()
```

</TabItem>

<TabItem value="ollama">

```python showLineNumbers title="travel-agent-ollama.py"
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

model1 = Ollama(model="mistral")
model2 = Ollama(model="dolphin2.2-mistral")

prompt1 = ChatPromptTemplate.from_template("""
Apenas traduza o texto a seguir:
{text}
"""
)

prompt2 = ChatPromptTemplate.from_template( """
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. Only respond with the list of 5 items, no
summarizing statement, forewords or warnings or even explanations are required.
"""
)

chain1 = prompt1 | model2

chain2 = {"activity": chain1} | prompt2 | model1

chain3 = {"text": chain2} | prompt1 | model2

for s in chain3.stream({"text": "caminhar na praia"}):
    print(s, end="", flush=True)
print()
```

</TabItem>

</Tabs>

:::caution Aviso

Trocar de modelos utilizando o ollama é relativamente rápido... **SE** você
tiver um computador poderoso. Se estiver executando esse exemplo apenas na CPU,
existe uma boa chance dele nem rodar. Se não quiser pagar para usar a API da
OpenAI, rode o exemplo do ollama no Colab.

:::

## 3. Usando passthroughs

Existe uma outra maneira de trabalhar com o input dos modelos que não envolve
um dicionário como parâmetro na chamada do método `stream`. Francamente, só vou
mostrar isso aqui pois não quero que fiquem confusos por um motivo bobo. Seguem
os dois exemplos usando o `RunnablePassthrough`:

<Tabs defaultValue="openai" values={[
        {label: 'OpenAI', value: 'openai'},
        {label: 'Ollama', value: 'ollama'},
  ]}>

<TabItem value="openai">

```python showLineNumbers title="simple-runnable"
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template(
"""
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. For each item, create a simple sentence
justifying this choice.
"""
)

chain = prompt | model

for s in chain.stream({"activity": "eat live fish"}):
    print(s.content, end="", flush=True)
```

</TabItem>

<TabItem value="ollama">

```python showLineNumbers title="simple-chain-ollama.py"
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

model = Ollama(model="mistral")
prompt = ChatPromptTemplate.from_template(
"""
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. For each item, create a simple sentence
justifying this choice.
"""
)

chain = prompt | model

for s in chain.stream({"activity": "eat live fish"}):
    print(s, end="", flush=True)
```

</TabItem>

</Tabs>

:::caution Aviso

Para poder usar o código acima com a API da OpenAI, lembre-se de configurar a
sua chave de API no sistema.

:::

## 2. Encadeando múltiplos modelos

Agora vamos recriar o nosso exemplo com o `tradutor` e o `agente`:

<Tabs defaultValue="openai" values={[
        {label: 'OpenAI', value: 'openai'},
        {label: 'Ollama', value: 'ollama'},
  ]}>

<TabItem value="openai">

```python showLineNumbers title="travel-agent.py"
from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

model1 = ChatOpenAI(model="gpt-3.5-turbo")
model2 = ChatOpenAI(model="gpt-4")

prompt1 = ChatPromptTemplate.from_template("""
Apenas traduza o texto a seguir:
{text}
"""
)

prompt2 = ChatPromptTemplate.from_template( """
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. Only respond with the list of 5 items, no
summarizing statement, forewords or warnings or even explanations are required.
"""
)

chain1 = prompt1 | model1

chain2 = {"activity": chain1} | prompt2 | model2

chain3 = {"text": chain2} | prompt1 | model1

for s in chain3.stream({"text": "caminhar na praia"}):
    print(s.content, end="", flush=True)
print()
```

</TabItem>

<TabItem value="ollama">

```python showLineNumbers title="travel-agent-ollama.py"
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate

model1 = Ollama(model="mistral")
model2 = Ollama(model="dolphin2.2-mistral")

prompt1 = ChatPromptTemplate.from_template("""
Apenas traduza o texto a seguir:
{text}
"""
)

prompt2 = ChatPromptTemplate.from_template( """
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. Only respond with the list of 5 items, no
summarizing statement, forewords or warnings or even explanations are required.
"""
)

chain1 = prompt1 | model2

chain2 = {"activity": chain1} | prompt2 | model1

chain3 = {"text": chain2} | prompt1 | model2

for s in chain3.stream({"text": "caminhar na praia"}):
    print(s, end="", flush=True)
print()
```

</TabItem>

</Tabs>

## 3. Runnable passthroughs

Existe uma maneira alternativa de chamar o método `stream` para aqueles que não
gostam do fato dele precisar de um dicionário para ser chamado. Se você está
entre essas pessoas, seus problemas foram resolvidos! Behold:

<Tabs defaultValue="simple" values={[
        {label: 'Exemplo simples', value: 'simple'},
        {label: 'Encadeamento', value: 'travel'},
  ]}>

<TabItem value="simple">

```python showLineNumbers title="simple-runnable.py"
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap, RunnablePassthrough

model = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template(
"""
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. For each item, create a simple sentence
justifying this choice.
"""
)

chain = {"activity": RunnablePassthrough()} | prompt | model

for s in chain.stream("eat live fish"):
    print(s.content, end="", flush=True)
```

</TabItem>

<TabItem value="travel">

```python showLineNumbers title="travel-agent-runnable.py"
from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap, RunnablePassthrough

model1 = ChatOpenAI(model="gpt-3.5-turbo")
model2 = ChatOpenAI(model="gpt-4")

prompt1 = ChatPromptTemplate.from_template("""
Apenas traduza o texto a seguir:
{text}
"""
)

prompt2 = ChatPromptTemplate.from_template( """
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to {activity}. Give the answers as a list of
items, no bigger than 5 items. Only respond with the list of 5 items, no
summarizing statement, forewords or warnings or even explanations are required.
"""
)

chain1 = {"text": RunnablePassthrough()} | prompt1 | model1

chain2 = {"activity": chain1} | prompt2 | model2

chain3 = {"text": chain2} | prompt1 | model1

for s in chain3.stream("caminhar na praia"):
    print(s.content, end="", flush=True)
print()
```

</TabItem>

</Tabs>
