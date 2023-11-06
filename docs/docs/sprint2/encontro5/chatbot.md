---
title: Rule based chatbot
sidebar_position: 3
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Rule based chatbots

<Admonition 
    type="note" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Construindo um chatbot baseado em regras em
Python](https://datasciencedojo.com/blog/rule-based-chatbot-in-python/#)

</Admonition>

Embora seja possível utilizar ferramentas prontas como o `Chatterbot` ou o
`NLTK`, elas são indicadas para sistemas com muitas variações de respostas. Na
verdade, um chatbot simples pode ser feito com um programa bem mais enxuto. A
seguir, vamos ver a criação de um chatbot simples que se comunica com o
usuário.

## 1. Criação de um chatbot simples

### 1.1. Escopo do chatbot 

Vamos começar definindo o escopo do chatbot. Para o nosso exemplo, vamos criar
uma aplicação extremamente simples para apenas detectar quando o usuário
cumprimenta o chatbot e responde adequadamente.

**Exemplo de interação:**

```
Usuário: Bom dia, tudo bem?
R: Bom dia! Comigo está tudo ótimo, e com você?
```

### 1.2. Criando expressões regulares

A primeira coisa que vamos desenvolver é a expressão regular para detectar que
o usuário teve a intenção de cumprimentar o chatbot. Embora seja possível
apenas detectar a frase `Bom dia, tudo bem?`, essa solução não é nada robusta.
Afinal, se o usuário disser `Boa tarde` ou mesmo deixar de usar pontuação ou
letras maiúsculas o sistema já não conseguiria detectar a intenção
corretamente.

:::tip Dica

Sempre que houver aqui uma expressão regular, recomenda-se fortemente testá-la
no [regex101](https://regex101.com)

:::

Vamos partir da premissa de que não temos intimidade com expressões regulares,
portanto faz mais sentido irmos construindo nossa expressão aos poucos e
considerando cada caso possível, um de cada vez. Vamos começar detectando o
cumprimento do usuário. Vamos considerar que o usuário pode dar bom dia, boa
tarde ou boa noite. A expressão regular fica: 

```bash
(Bom dia|Boa tarde|Boa noite)
```

<details><summary>Explicação do chat gepeto</summary>
A expressão regular `(Bom dia|Boa tarde|Boa noite)` usa um mecanismo chamado
alternância para combinar uma de várias opções diferentes. Aqui está o que cada
parte faz:

- `( ... )`: Os parênteses são usados para agrupar partes da expressão regular.
  Eles não apenas agrupam a expressão, mas também criam o que é conhecido como
  um grupo de captura. Isso significa que o texto que corresponde a esta parte
  da expressão pode ser "capturado" para uso posterior.

- `Bom dia`: Esta é uma sequência literal que corresponderá exatamente ao texto
  "Bom dia".

- `Boa tarde`: Assim como "Bom dia", esta é outra sequência literal que
  corresponderá exatamente ao texto "Boa tarde".

- `Boa noite`: E esta é mais uma sequência literal, correspondendo exatamente
  ao texto "Boa noite".

- `|`: Este é o operador de alternância, e funciona como um "ou" lógico. Isso
  significa que a expressão regular corresponderá a "Bom dia" OU "Boa tarde" OU
  "Boa noite".

Portanto, essa expressão regular procura por uma de três diferentes saudações.
Se qualquer uma das saudações especificadas aparecer no texto de destino, a
expressão regular considerará isso uma correspondência.
</details>

:::tip Dica

O ChatGPT é **muito** bom para criar ou explicar expressões regulares. Use-o em
conjunto com o regex101.

:::

Temos alguns problemas aqui. O primeiro é que não estamos capturando a próxima
parte da expressão, em que o usuário pode perguntar se está tudo bem. O segundo
problema é que se o usuário não usar letras maiúsculas no começo das palavras,
o padrão não é reconhecido. É possível resolver isso direto na aplicação em
Python, mas vamos explorar um pouco mais as opções de regex. Vejamos como pode
ficar:

```bash
\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))
```

<details><summary>Explicação do chat gepeto</summary>

A expressão regular `\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))` é um pouco mais
complexa do que a anterior e possui diversas partes:

- `\b`: É um metacaractere que representa um limite de palavra (word boundary).
  Isso significa que o padrão seguinte deve começar no início de uma palavra.

- `(?: ... )`: É um grupo de não captura. Grupos de não captura agrupam
  múltiplas partes de uma expressão regular juntas sem capturar o texto que
  corresponde a essa parte para uso posterior. Eles são usados para aplicar
  quantificadores a partes da expressão, mas sem a sobrecarga de armazenar a
  captura.

- `[Bb]`: É um conjunto de caracteres que corresponderá a 'B' maiúsculo ou 'b'
  minúsculo.

- `o[am]`: Segue a mesma lógica do conjunto anterior, correspondendo a "oa" ou
  "om", o que permite a formação das palavras "Boa" ou "Bom".

- `\s`: Corresponde a qualquer espaço em branco, como espaços, tabs, etc.

- `(tarde|dia|noite)`: É um grupo de captura que vai corresponder a uma das
  palavras "tarde", "dia" ou "noite".

Portanto, essa expressão regular vai corresponder a "Bom dia", "Bom tarde",
"Bom noite", "Boa dia", "Boa tarde", "Boa noite", com qualquer combinação de
maiúsculas e minúsculas para "Bom/Boa", devido ao `[Bb]` e `[oa]`, e apenas se
essas combinações aparecerem como palavras isoladas no texto, por causa do
`\b`.

Aqui estão alguns exemplos de como esta expressão regular funcionaria:

- "Bom dia" → Corresponde (e captura "dia")
- "boa tarde" → Corresponde (e captura "tarde")
- "BoM Noite" → Corresponde (e captura "noite")
- "abomdia" → Não corresponde (porque "abomdia" não começa no limite de uma
  palavra devido à ausência de espaço ou separador de palavras antes de "bom")

</details>

Acho que agora conseguimos uma expressão legal para capturar nossa primeira
intenção! Vamos para a segunda? Agora vamos ver se o usuário perguntou se o
chatbot está bem? Para isso, vamos direto para uma expressão regular mais
robusta:

```bash
\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?
```

<details><summary>Explicação do chat gepeto</summary>
A expressão regular
`\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?` busca
por várias expressões que podem ser usadas para perguntar informalmente como
alguém está. Aqui está o que cada parte da expressão faz:

- `\b`: Indica um limite de palavra, o que significa que o padrão deve ocorrer
  no início de uma palavra.

- `(?:[Tt]udo)?`: É um grupo de não captura que procura pela palavra "Tudo" ou
  "tudo". O `?` depois do grupo de não captura indica que a presença da palavra
  "Tudo" ou "tudo" é opcional.

- `\s?`: Corresponde a zero ou um espaço em branco (espaço, tabulação, etc.). A
  questão `?` significa que o espaço pode ou não estar presente.

- `(?: ... )`: São grupos de não captura usados para agrupar expressões
  alternativas sem capturar o que foi correspondido.

- `(?:[bB]em)`: Este grupo de não captura vai corresponder à palavra "bem" ou
  "Bem".

- `(?:[bB]ão)`: Este grupo de não captura vai corresponder à palavra "bão" (uma
  forma coloquial de "bom" em português) ou "Bão".

- `(?:[fF]irme)`: Este grupo de não captura vai corresponder à palavra "firme"
  ou "Firme".

- `(?:em\sriba)`: Este grupo de não captura vai corresponder à expressão "em
  riba" (provavelmente uma forma coloquial de "em cima").

- `\?`: Corresponde a um ponto de interrogação literal, indicando que a
  expressão que está sendo buscada provavelmente é uma pergunta.

Juntando tudo isso, a expressão regular pode corresponder a várias formas de
perguntar informalmente como alguém está, incluindo a presença ou ausência da
palavra "Tudo" no começo e também considerando variações comuns de escrita e
coloquialismos. Por exemplo, ela pode corresponder a:

- "Tudo bem?"
- "tudo bão?"
- "Bem?"
- "bão?"
- "Firme?"
- "em riba?"

A expressão é flexível o suficiente para pegar diferentes variações de
espaçamento e capitalização.
</details>

### 1.3. Criando um dicionário de intenções 

Agora que já temos nossas expressões regulares, vamos criar um dicionário para
mapear as intenções do usuário. Para isso, crie um arquivo python:

```bash
touch test-chatbot.py
```

Nesse arquivo, vamos adicionar o seguinte:
```python title="test-chatbot.py" showLineNumbers
#! /bin/env python3

import re

intent_dict = {
    r"\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))": "greetings",
    r"\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?": "genki"
}

command = input("Digite o seu comando: ")
for key, value in intent_dict.items():
    pattern = re.compile(key)
    groups = pattern.findall(command)
    if groups:
        print(f"Encontrei a seguinte intenção: {value}")
```

Deixe o script executável com:
```bash
chmod +x test-chatbot.py
```

E execute-o com:

```bash
./test-chatbot.py
```

Note que as expressões regulares ainda não estão perfeitas. Brinque um pouco
com elas, talvez até criando novas expressões com intenções redundantes, para
que o chatbot fique um pouco mais inteligente.

### 1.4. Atrelando a intenção a uma ação

Apenas identificar a intenção não é o suficiente para criar um chatbot capaz de
executar ações mais complexas. Vamos agora criar um dicionário que linka
intenções à ações. Edite o código anterior e deixe-o assim:

```python title="test-chatbot.py" showLineNumbers
#! /bin/env python3
import re

def greet_back(time_of_day):
    if time_of_day == "dia":
        return f"Bom {time_of_day}!"
    else:
        return f"Boa {time_of_day}!"

def genki_back(_):
    return "Comigo está tudo bem, e com você?"

intent_dict = {
    r"\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))": "greetings",
    r"\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?": "genki"
}

action_dict = {
        "greetings": greet_back,
        "genki": genki_back
}

command = input("Digite o seu comando: ")
for key, value in intent_dict.items():
    pattern = re.compile(key)
    groups = pattern.findall(command)
    if groups:
        print(f"{action_dict[value](groups[0])}", end=" ")
print()
```

Pronto! Temos o nosso **pequeno** chatbot configurado e funcional!

## 2. Exercícios propostos

Criando...
