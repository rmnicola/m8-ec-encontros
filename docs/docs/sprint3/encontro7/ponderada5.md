---
title: Atividade ponderada 5
sidebar_position: 4
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/ponderada.png').default} width='35vw'/> Construção de um chatbot com LLM e RAG

## 1. Objetivo
Melhoria do chatbot desenvolvido na ponderada anterior, agora utilizando
técnicas de leitura de documentos.

## 2. Enunciado

Utilizando um LLM (local ou API externa), crie um chatbot simples com
instruções customizadas para ajudar um usuário a pesquisar normas de segurança
em ambientes industriais. O sisema deve contar com uma interface gráfica e
responder de forma sucinta e clara sobre o que lhe foi perguntado. O sistema
ainda deve ser capaz de contextualizar suas respostas a partir do seguinte
documento: 

[Workshop rules and safety
considerations](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety)

Exemplo de prompt:

```bash
>>> Who is allowed to operate a lathe? What protective gear should be used to
>>> do it?
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
4. O prazo para a entrega desta atividade é até o dia 29/11/2023 às 23h59min.

## 4. Padrão de qualidade

:::caution Aviso!

Os itens descritos no padrão de qualidade devem estar claramente apresentados
no vídeo do projeto em funcionamento.

:::

1. Utilizar o langchain para criar a interface com o modelo de LLM utilizado
   (pode ser openAI ou modelos do huggingface/ollama) - até 2,0 pontos;
2. Criar uma interface gráfica simples para o chatbot - até 2,0 pontos;
3. Responder de forma concisa aos prompts do usuário - até 2,0 pontos;
4. O sistema deve considerar como contexto o arquivo/documento/página fornecida
   no enunciado da atividade - até 4,0 pontos.

