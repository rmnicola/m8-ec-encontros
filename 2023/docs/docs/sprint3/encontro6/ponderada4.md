---
title: Atividade ponderada 4
sidebar_position: 6
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/ponderada.png').default} width='35vw'/> Construção de um chatbot com LLM

## 1. Objetivo

Desenvolvimento de um chatbot utilizando LLM.

## 2. Enunciado

Utilizando um LLM (local ou API externa), crie um chatbot simples com
instruções customizadas para ajudar um usuário a pesquisar normas de segurança
em ambientes industriais. O sisema deve contar com uma interface gráfica e
responder de forma sucinta e clara sobre o que lhe foi perguntado.

Exemplo de prompt:

```bash
>>> Quais EPIs são necessários para operar um torno mecânico?
```

## 3. Padrão de entrega

Esses são os critérios mínimos para que eu considere a atividade como entregue.
Fique atento, pois o não cumprimento de qualquer um desses critérios pode, no
melhor dos casos, gerar um desconto de nota e, no pior deles, invalidar a
atividade.

1. A atividade deve ser feita em um repositório aberto no github. Seu link deve
   ser fornecido no card da adalove;
2. No README do repositório deve ter instruções claras de como instalar e rodar
   o sistema criado, comandos em blocos de código e uma expliação sucinta do
   que fazem;
3. Ainda no README, deve haver um vídeo gravado demonstrando plenamente o
   funcionamento do nó criado;
4. O prazo para a entrega desta atividade é até o dia 21/11/2023 às 23h59min.

## 4. Padrão de qualidade

O chatbot desenvolvido deve:

1. Utilizar o langchain para criar a interface com o modelo de LLM utilizado
   (pode ser openAI ou modelos do huggingface/ollama) - até 4,0 pontos;
2. Utilizar o gradio para criar uma interface gráfica simples para o chatbot -
   até 3,0 pontos;
3. Responder de forma concisa aos prompts do usuário. Para isso, deve-se criar
   um prompt de sistema que contextualiza todas as respostas do modelo
   utilizado - até 3,0 pontos.
