---
title: Atividade ponderada 3
sidebar_position: 4
---

# <img src={require('/img/ponderada.png').default} width='35vw'/> Criação de um chatbot simples

## 1. Objetivo
Assimilar os conceitos relacionados à chatbots baseados em regras.

## 2. Enunciado
Desenvolva um nó de ROS que seja um chatbot capaz de entender comandos escritos
em linguagem natural para interagir com um robô de serviço fictício. O chatbot
deve fornecer ao usuário a possibilidade de enviar comandos de posição para o
robô de forma simples e intuitiva. Exemplos de comandos:

```bash
Vá para a secretaria
Dirja-se ao laboratório
Me leve para a biblioteca
```
Para cada comando registrado, o sistema deve ser capaz de extrair a intenção do
usuário a partir de um dicionário de intenções, filtradas por expressões
regulares. A partir daí, um segundo dicionário deve ser usado, capaz de
vincular intenções à funções que o robô deve executar. Para essa ponderada, o
script em Python não precisa se comunicar com o nav2 e nem com o robô, mas é
necessário dar um feedback ao usuário de que a ação foi compreendida e está
sendo executada. Por fim, está liberado o uso de frameworks como `Chatterbot` e
`NLTK`.

## 3. Padrão de entrega

Esses são os critérios mínimos para que eu considere a atividade como entregue.
Fique atento, pois o não cumprimento de qualquer um desses critérios pode, no
melhor dos casos, gerar um desconto de nota e, no pior deles, invalidar a
atividade.

1. A atividade deve ser feita em um repositório aberto no github. Seu link deve
   ser fornecido no card da adalove;
2. O repositório deve contar com um workspace ROS2 com pelo menos um nó
   configurado: o do chatbot. Sugere-se que utilize o mesmo workspace das
   outras atividades ponderadas.
3. No README do repositório deve ter instruções claras de como instalar e rodar
   o nó criado, com comandos em blocos de código e uma explicação sucinta
   do que fazem;
4. Ainda no README, deve haver um vídeo gravado demonstrando plenamente o
   funcionamento do nó criado;
5. O prazo para a entrega desta atividade é até o dia 12/11/2023 às 23h59min.

## 4. Padrão de qualidade

O sistema desenvolvido deve:

1. Comprovadamente ser capaz de compreender ao menos uma inteção do usuário: a
   de mandar o robô para um determinado ponto. Deve haver um dicionário de
   intenções e a intenção deve ser caputrada através de expressões regulares.
   Ao menos dois formatos diferentes devem ser considerados para a captura da
   intenção do usuário (e.g. "Vá para...", "Me leve até...") - até 4,0 pontos;
2. O script deve contar com um dicionário de ações, relacionando cada intenção
   com uma função a ser executada pelo robô - até 3,0 pontos;
3. O chatbot deve dar feedback ao usuário sobre a compreensão do que foi dito e
   a ação que será tomada - até 3,0 pontos.

