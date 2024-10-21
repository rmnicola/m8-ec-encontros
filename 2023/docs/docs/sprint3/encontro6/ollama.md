---
title: Ollama
sidebar_position: 4
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Hospedando seu próprio modelo

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
        src="https://www.youtube.com/embed/rIRkxZSn-A8" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 1. Instalando o Ollama

Para instalar o ollama em `Linux` ou `WSL`, basta rodar o comando abaixo:

```bash
curl https://ollama.ai/install.sh | sh
```

## 2. Rodando modelos direto no terminal

Para rodar modelos diretamente no terminal, utilize o comando `ollama run`.

```bash
ollama run dolphin2.2-mistral
```

Note as similaridades entre o ollama e o docker. Se você não tiver o modelo que
está querendo rodar, ele baixa o modelo automaticamente.

## 3. Interagindo com o modelfile

As similaridades com o docker não terminam por aí. Assim como é possível criar
um `dockerfile` para definir novas imagens de containers a partir de
imagens-base, é possível criar um `modelfile` para definir novos modelos a
partir de modelos-base. Vamos criar um modelo especializado com o seguinte
modelfile:

```bash
FROM dolphin2.2-mistral

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system prompt
SYSTEM """
From now on you're only allowed to answer as Dexter from the episode 'Omelette
du fromage' where he only ever says 'Omelette du fromage'.
"""
```

Ainda tem um [bug não
resolvido](https://github.com/jmorganca/ollama/issues/613) que faz com que o
usuário `ollama` não seja capaz de ler o seu `Modelfile`. Para resolver isso,
vamos usar um comando um pouco inseguro, mas aceitável se você for o único
usuário do seu computador. Sugiro não usar esse comando na sua HOME:

```bash
chmod -R o+rx .
```

Isso vai fazer com que o `Modelfile` seja acessível pelo usuário `ollama`.

Para criar o novo modelo, rode:

```bash
ollama create dexter -f Modelfile
```

E agora, para rodá-lo:

```bash
ollama run dexter
```

## 4. Hospedando seus modelos locais

Quer saber como servir seus modelos do `ollama` através de uma API REST? Bom,
se você está usando Linux e instalou utilizando o comando do começo dessa
seção, meus parabéns, você já tem um servidor de `ollama` rodando. Vamos
testar? Rode no seu terminal:

```bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "dexter",
  "prompt":"Why is the sky blue?"
}'
```

Note que, por padrão, o `ollama` devolve um json por chunk gerado. Se quiser
esperar a resposta inteira para receber apenas uma resposta, use:

```bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "dexter",
  "prompt":"Why is the sky blue?",
  "stream":false
}'
```

## 5. Integração com LangChain

Por fim, vamos integrar nosso servidor `ollama` com um script usando langchain?
Veja o exemplo abaixo: 

```python showLineNumbers title="ollama-lang.py"
from langchain.llms import Ollama
ollama = Ollama(base_url='http://localhost:11434',
model="dexter")
print(ollama("why is the sky blue"))
```

## 6. Conceitos básicos de quantização

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
        src="https://www.youtube.com/embed/ZKdMbQq5T30" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>
