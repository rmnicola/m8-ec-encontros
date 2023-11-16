---
title: Intro
sidebar_position: 1
slug: /
---

# Desenvolvimento de um robô de serviço

O módulo atual vai lidar com o desenvolvimento de um robô de serviço. Assim como
vimos no módulo 6, vamos voltar a trabalhar com robôs móveis. Dessa vez, no entanto, 
vamos nos aprofundar nos conceitos de mapeamento e localização simultânea (SLAM) 
e integrar a plataforma robótica (e o ROS) com modelos de processamento de linguagem
(LLMs).

A seguir, um resumo em português claro e conciso do que deve ser desenvolvido em 
cada sprint.

### Sprint 1 

Entendimento do projeto. Aspectos de negócio, ética e usabilidade assim como a 
elicitação de requisitos funcionais e não funcionais.

### Sprint 2

Primeira entrega completa do projeto. O que isso significa? Significa uma versão 
que o cliente pode usar tranquilamente, seguindo os preceitos do 
[desenvolvimento em espiral](https://medium.com/contexto-delimitado/o-modelo-em-espiral-de-boehm-ed1d85b7df).
O que, exatamente, vamos entregar?

1. Um software desenvolvido para ROS que implementa SLAM em um robô móvel;
2. Um sistema de interface de usuário por terminal, onde o usuário pode digitar
comandos para o robô;
3. Um sistema de chatbot básico utilizando expressões regulares para compreender
os comandos enviados pelo usuário e linkar com a ação adequada no robô; e
4. Documentação e manual de usuário para essa versão do projeto.

### Sprint 3

Aprimoramento do sistema de chatbot. O que antes era baseado em regras simples
e expressões regulares agora passa a usar LLM (local ou API externa). Para esta
entrega, espera-se:

1. Sistema de navegação e mapeamento ainda funcional;
2. Interface de usuário (pode ser terminal ou já ter um frontend) por chatbot,
   só que agora utilizando LLM e atendendo a mais do que só comandos simples. O
   sistema deve ser capaz de ler arquivos PDF e usá-los para contextualizar a
   resposta;
3. Deve haver um nó responsável por realizar o log do sistema (grupo está livre
   para definir o que ficará salvo no log operacional).

### Sprint 4

:::info
Em construção. Volte mais tarde =D
:::

### Sprint 5

:::info
Em construção. Volte mais tarde =D
:::


