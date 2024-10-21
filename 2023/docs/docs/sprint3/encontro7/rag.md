---
title: RAG
sidebar_position: 3
---
import Admonition from '@theme/Admonition';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> RAG

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
        src="https://www.youtube.com/embed/T-D1OfcDW1M" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

Uma das tarefas mais comuns para se utilizar um LLM é a de "conversar com
documentos". No entanto, o modelo com maior capacidade para contexto de prompts
se limita a aproximadamente 300 páginas de texto. Para contornar esse problema,
precisaremos visitar alguns assuntos relacionados a como carregar, transformar,
guardar e buscar textos relevantes ao prompt do nosso usuário.

![](/img/retrieval.jpg)
Retirado de [langchain
documentation](https://python.langchain.com/docs/modules/data_connection/).

## 1. Carregadores e transformadores

Para conseguir utilizar documentos em conjunto com LLMs o que precisamos fazer?
Sim! Ler os documentos =)

Para conseguir ler os documentos de diferentes formatos, o Langchain implementa
uma [série de
submódulos](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
com os quais é possível interagir com variados tipos de arquivo (`txt`, `pdf`,
artigos do `arxiv`, repositórios do `github`). É isso, não tem muito o que
falar aqui. Quer interagir com um tipo de documento específico? Procure pelo
submódulo na documentação do Langchain.

A seguir, precisamos decidir como armazenar o texto. Afinal, não faz sentido
algum simplesmente pegar o texto como um todo e armazenar tudo de uma vez só,
em um único `embedding`. Sendo assim, temos que decidir **como vamos divir o
texto**.

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
        src="https://www.youtube.com/embed/n0uPzvGTFI0" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

Aqui vemos que o langchain traz ferramentas para dividir os texto em `chunks`
com tamanho pré-definidos. Aqui é interessante notar que a decisão de
`chunksize` e `chunk overlap` influenciam diretamente na performance da nossa
aplicação com RAG.

## 2. Vector embeddings

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
        src="https://www.youtube.com/embed/gQddtTdmG_8" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 3. Vector storage

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
        src="https://www.youtube.com/embed/dN0lsF2cvm4" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

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
        src="https://www.youtube.com/embed/ySus5ZS0b94" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 4. Exemplos

## 4.1. RAG simples com FAISS

<Tabs defaultValue="openai" values={[
        {label: 'OpenAI', value: 'openai'},
        {label: 'Ollama', value: 'ollama'},
  ]}>

<TabItem value="openai">

```python showLineNumbers title="rag.py"
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.vectorstores import FAISS

vectorstore = FAISS.from_texts(
    ["Bread - (0.0, 1.0, 2.0)\nMilk - (1.0, 2.0, 0.0)"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model="gpt-3.5-turbo")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

for s in chain.stream("Where is the bread?"):
    print(s.content, end="", flush=True)
```

</TabItem>

<TabItem value="ollama">

```python showLineNumbers title="rag-ollama.py"
from langchain.llms import Ollama
from langchain.embeddings import GPT4AllEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.vectorstores import FAISS

vectorstore = FAISS.from_texts(
    ["Bread - (0.0, 1.0, 2.0)\nMilk - (1.0, 2.0, 0.0)"], embedding=GPT4AllEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="mistral")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

for s in chain.stream("Where is the bread?"):
    print(s, end="", flush=True)
```

</TabItem>

</Tabs>

## 4.2. RAG usando documento `txt` c/ ChromaDB

<Tabs defaultValue="openai" values={[
        {label: 'OpenAI', value: 'openai'},
        {label: 'Ollama', value: 'ollama'},
  ]}>

<TabItem value="openai">

```python showLineNumbers title="rag-document.py"
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# load the document and split it into chunks
loader = TextLoader("./data/items.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model="gpt-3.5-turbo")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

for s in chain.stream("Where is the bread?"):
    print(s.content, end="", flush=True)

```

</TabItem>

<TabItem value="ollama">

```python showLineNumbers title="rag-document-ollama.py"
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# load the document and split it into chunks
loader = TextLoader("./data/items.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="mistral")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

for s in chain.stream("Where is the bread?"):
    print(s, end="", flush=True)
```

</TabItem>

</Tabs>
