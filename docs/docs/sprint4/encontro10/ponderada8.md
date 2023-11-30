---
title: Atividade ponderada 8
sidebar_position: 6
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/ponderada.png').default} width='35vw'/> Tradutor de áudio

## 1. Objetivo

Criar uma aplicação que integra um tradutor de texto (pode ser baseado em LLM
ou não), uma aplicação de speech-to-text e uma aplicação de text-to-speech.

## 2. Enunciado

Crie uma ferramenta de terminal capaz de receber como argumento o caminho para
um arquivo de áudio contendo a fala de uma pessoa. Após ler o arquivo
fornecido, a sua aplicação deve ser capaz de transformar o áudio em texto
corretamente, usar esse texto gerado para alimentar um tradutor de texto (e.g.
transforma um texto do português para o inglês) e, por fim, transforma o texto
traduzido em áudio novamente e reproduz para o usuário.

:::tip Dica

Caso não consiga rodar modelos mais robustos, limite-se a traduzir do portugês
para o Inglês, pois há mais ferramentas disponíveis para trabalhar com a língua
inglesa.

:::


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
4. O prazo para a entrega desta atividade é até o dia 14/12/2023 às 23h59min.

## 4. Padrão de qualidade

:::caution Aviso!

Os itens descritos no padrão de qualidade devem estar claramente apresentados
no vídeo do projeto em funcionamento.

:::

1. A aplicação desenvolvida deve ter uma interface de usuário capaz de receber
   um arquivo de áudio (sugere-se o uso do terminal por simplicidade, mas pode
   utilizar opções mais robustas) - até 1,0 ponto.
2. O sistema deve comprovadamente ser capaz de transformar o arquivo de áudio
   em texto, sendo capaz de traduzir o exemplo demonstrado sem falhas - até 3,0
   pontos.
3. O sistema deve comprovadamente ser capaz de traduzir o texto fornecido para
   a língua de sua escolha (e.g. português, inglês, japonês) - até 3,0 pontos.
4. O sistema deve comprovadamente ser capaz de sintetizar a frase traduzida,
   criando um áudio que o usuário pode ouvir com a resposta final - até 3,0
   pontos.
