---
title: ChatGPT
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Utilizando o ChatGPT

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
        src="https://www.youtube.com/embed/5sLYAQS9sWQ" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 1. Configurando o seu acesso à API da OpenAI

Antes de mais nada, precisaremos configurar nossa chave de acesso à API da
OpenAI. Para isso, acesse o [site](https://platform.openai.com/api-keys) da
openAI. A seguir, clique em `Create new secret key` e configure uma nova chave
de acesso secreta. Note que será necessário configurar uma forma de pagamento
caso seus U$4,00 se esgotem ou expirem.

O modelo de cobrança da API do ChatGPT depende do modelo utilizado e é
calculado em incrementos de `1000 tokens`, geralmente custando alguns centavos
por cada requisição que alcance os mil tokens. Para ver quanto custa cada
modelo, acesse [esse link](https://openai.com/pricing).

**Tá, mas o que são *tokens*?**

![](/img/tokens.png)

Um token nada mais é do que a unidade básica de processamento de texto. Imagine
que cada palavra, pontuação ou até mesmo parte de uma palavra é dividida em
pequenos pedaços. Cada um desses pedaços é um "token". Os LLMs usam esses
tokens para entender e gerar texto, pois eles ajudam o modelo a processar e
analisar as informações de forma mais eficiente e detalhada. Simplificando, são
como os tijolos que constroem as frases e textos que os LLMs criam ou
interpretam.

:::tip Quer saber mais?

Para saber mais sobre tokens, leia esse
[artigo](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
do site da OpenAI

:::

Agora que você gerou sua chave de acesso, vamos direto para o primeiro exemplo
da API, certo? **ERRADO**. Utilizar a sua chave de API dentro do seu script em
Python em plain text é muito inseguro. Trata-se de uma chave a partir do qual
qualquer pessoa pode fazer requisições atreladas a um serviço que tem acesso ao
seu cartão de crédito. Vamos proteger isso um *pouquinho* melhor?

Vamos utilizar uma variável de ambiente para isso, mas também não acho adequado
utilizar variáveis de ambiente que podem prontamente ser acessadas por qualquer
pessoa que tenha acesso ao seu arquivo de configuração. Temos algumas opções
para lidar com isso:

1. Utilizar um arquivo `.env` em conjunto com a biblioteca `dotenv` do Python
   para configurar uma variável de ambiente local para o seu projeto
   (**CUIDADO!!! Precisa adicionar esse arquivo ao seu `.gitignore`**)
2. Adicionar a sua variável de ambiente a um arquivo mais discreto, como o
   `/etc/zsh/zshenv`. (Não fazer isso de forma alguma se for um PC
   compartilhado, pois setará essa variável de ambiente para todos os usuários)
3. Criar uma variável de ambiente com criptografia (opção mais segura, mas
   também a mais tediosa de configurar. Quer seguir esse caminho? Veja como
   [aqui](https://unix.stackexchange.com/questions/122886/what-are-ways-to-encrypt-a-password-inside-an-environment-variable)

Neste tutorial, vamos utilizar a primeira opção. Portanto, crie um arquiov
`.env` com:

```bash
touch .env
```

E adicione sua chave com:
```bash
echo "OPENAI_API_KEY='<sua-chave-aqui>'" >> .env
```

**CONFIGURE IMEDIATAMENTE SEU GITIGNORE PARA NÃO MANDAR A CHAVE PARA O SEU
REPOSITÓRIO POR ACIDENTE**

Segue abaixo um exemplo de gitignore para projetos em Python com `venv` e
`dotenv`:

```python showLineNumbers title=".gitignore"
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/
```

## 2. Criando um ambiente virtual com `Anaconda`

Vocês já usaram o `python-venv` para criar ambientes virtuais. Agora vamos
utilizar uma alternativa para gerenciar pacotes e ambientes virtuais: o
`Anaconda`.

Em geral, o `Anaconda` é bem mais fácil de utilizar para gerenciar ambientes
virtuais que o `pyenv`. No entanto, trata-se de um framework enorme com
diversos pacotes pré-instalados. Para ter o melhor dos dois mundos, vamos
utilizar o `miniconda`. Para instalá-lo, use:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
```

Após a instalação, podemos criar um novo ambiente virtual usando:

```bash
conda create -n llm python=3.11
```

Diferente do `pyenv`, podemos ativar os ambientes virtuais do `Anaconda` de
qualquer lugar do nosso sistema com:

```bash
conda activate llm
```

Note, também, que o conda é capaz de instalar novas versões do Python
automaticamente (a versão padrão do Ubuntu é a `3.10`)

Vamos instalar os pacotes que vamos utilizar:

```bash
conda install -c conda-forge openai python-dotenv
```

## 2. Utilizando a API da OpenAI

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
        src="https://youtube.com/embed/mVX3Z46iYTQ" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

Vamos recriar um exemplo mais simples abaixo:

```python showLineNumbers title="gpt.py"
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

print(chat_with_gpt("Explique para que serve o partial. Dê um exemplo"))
```

Pronto! Já temos uma configuração para utilizar a API da OpenAI em nossos
projetos em Python
