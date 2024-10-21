---
title: LangChain Pt. I
sidebar_position: 3
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Elevando o potencial das LLMs com LangChain

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/aywZrzNaKjs" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 1. Conceitos básicos do LangChain

1. **Framework para Modelos de Linguagem**: LangChain é uma estrutura de
   programação destinada ao desenvolvimento de aplicações que utilizam modelos
   de linguagem. Ele oferece uma interface padrão para "cadeias", facilitando a
   integração com outras ferramentas e possibilitando cadeias de ponta a ponta
   para aplicações comuns.

2. **Open Source e Orientado a Dados**: Como um framework open source,
   LangChain permite a criação de experiências personalizadas e enriquecidas ao
   se conectar com diversas fontes de dados. Ele é descrito como "data-aware" e
   "agentic", o que significa que as aplicações desenvolvidas com ele podem
   interagir com o ambiente e conectar-se a outras fontes de dados.

3. **Componentes Modulares**: Os principais componentes do LangChain incluem
   "LLM Wrappers", "Prompt Template" e índices para recuperação de informações
   relevantes. Esses componentes são blocos de construção modulares, prontos e
   fáceis de usar para desenvolver aplicações poderosas.

4. **Usos e Aplicações**: LangChain é utilizado em várias aplicações, incluindo
   análise e resumo de documentos, chatbots e análise de código. Isso demonstra
   sua versatilidade e capacidade de se adaptar a diferentes necessidades e
   contextos.

5. **Agentes e Ferramentas**: Os agentes no LangChain são componentes
   reutilizáveis que podem executar tarefas específicas, como geração de texto,
   tradução de idiomas e resposta a perguntas. Além disso, existem ferramentas
   que são bibliotecas de funções auxiliares no desenvolvimento de diversas
   aplicações.

6. **Facilitação do Desenvolvimento**: O LangChain atua como uma orquestração
   para o desenvolvimento de aplicações, simplificando o uso de LLMs em
   diferentes contextos, desde cálculos algébricos até a geração de saídas
   gráficas.

## 2. Integrando o LangChain com a API da OpenAI

### 2.1. Reproduzindo o exemplo anterior com LangChain

Antes de mais nada, vamos instalar o langchain com:

```bash
conda install langchain -c conda-forge
```

A seguir, vamos criar um novo arquivo e adicionar o seguinte script:

```python showLineNumbers title="lang.py"
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

print(chat(messages))
```

Note que o langchain já espera por padrão que a API Key esteja em uma variável
de ambiente chamada `OPENAI_API_KEY`. Por isso não é necessário carregá-la
explícitamente.

### 2.2. Streaming de `chunks`

Quando rodamos os dois primeiros scripts que fizemos, foi possível notar que
houve um significativo atraso entre o pedido e a resposta do sistema. Isso se
dá pois, por padrão, tanto a API da OpenAI como o Langchain esperam a resposta
estar pronta para exibir tudo de uma vez. Para ter uma funcionalidade mais
parecida com o ChatGPT, podemos fazer um streaming de `chunks`. Veja o exemplo
abaixo:

```python showLineNumbers title="lang_streaming.py"
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=512)

for chunk in llm.stream("Escreva uma música sobre monads em Python"):
    print(chunk, end="", flush=True)
```
