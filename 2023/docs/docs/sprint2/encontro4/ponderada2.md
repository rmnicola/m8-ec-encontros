---
title: Atividade ponderada 2
sidebar_position: 6
---

# <img src={require('/img/ponderada.png').default} width='35vw'/> Navegação com o turtlebot

## 1. Objetivo
Interagir de forma programática com o stack de navegação do ROS

## 2. Enunciado
Desenvolva um pacote em ROS com as funcionalidades de mapeamento e navegação
utilizando o turtlebot 3 (simulado ou real)

## 3. Padrão de entrega

Esses são os critérios mínimos para que eu considere a atividade como entregue.
Fique atento, pois o não cumprimento de qualquer um desses critérios pode, no
melhor dos casos, gerar um desconto de nota e, no pior deles, invalidar a
atividade.

1. A atividade deve ser feita em um repositório aberto no github. Seu link deve
   ser fornecido no card da adalove;
2. O repositório deve contar com um workspace ROS2 com pelo menos um pacote
   configurado. Deverá haver ao menos dois lançadores: um que lança todo o
   necessário para o mapeamento e outro que lança todo o necessário para
   navegação;
3. No README do repositório deve ter instruções claras de como instalar e rodar
   o pacote criado, com comandos em blocos de código e uma explicação sucinta
   do que fazem;
4. Ainda no README, deve haver um vídeo gravado demonstrando plenamente o
   funcionamento do sistema completo, mostrando tanto o mapeamento quanto a
   navegação; e
5. O prazo para a entrega desta atividade é até o dia 12/11/2023 às 23h59min.

:::tip Dica

É possível configurar um `launcher` para lançar outros `launchers`. Corram
atrás de como isso pode ser feito, não vou dar **tudo** de mão beijada =P

:::

## 4. Padrão de qualidade

O sistema desenvolvido deve:

1. Comprovadamente ser capaz de mapear de forma fidedigna um ambiente (simulado
   ou real) - até 3,0 pontos;
2. Ser capaz de navegar em um ambiente pré-mapeado **de forma programática** -
   até 3,0 pontos; 
3. Ser capaz de desviar de obstáculos de forma dinâmica (obstáculos não
   mapeados) - até 3,0 pontos; 
4. O sistema deve ser [idempotente](https://pagar.me/blog/idempotencia/). Isso
   significa, na prática, que mesmo rodando várias vezes o navegador, ele vai
   passar pelos mesmos pontos (sem tentar inicializar a pose duas vezes) - até 1,0 ponto;
