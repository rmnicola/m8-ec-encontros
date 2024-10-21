---
title: Ponderadas
sidebar_position: 2
slug: /ponderadas
---

# Atividades Ponderadas do Módulo

<img 
  src="https://i.imgur.com/Sfmg0N8.jpeg"
  alt="Puck is not amused" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    marginRight: 'auto',
    maxHeight: '30vh'
  }} 
/>
<br/>

## 1. Funcionamento das Ponderadas no Módulo 11

As atividades ponderadas são essenciais para avaliar o progresso dos estudantes
na compreensão dos temas centrais do módulo. Frequentemente, elas representam
um recorte do conteúdo estudado. Neste módulo, as atividades propostas terão
maior profundidade e complexidade. 

Entretanto, aumentar a complexidade e escopo de todas as atividades seria
inviável devido a restrições de tempo. A solução encontrada foi oferecer
liberdade de escolha: o estudante deverá concluir apenas **3 atividades
ponderadas dentre as 6 disponíveis**, selecionando aquelas que considerar mais
interessantes para aprofundamento.

### 1.1. Notas e Entregas

Para viabilizar essa escolha no sistema da Adalove, foram cadastradas três
atividades ponderadas genéricas. As notas das **3 atividades com maior
pontuação** serão publicadas nessas atividades genéricas. Caso o estudante não
conclua 3 atividades dentro do prazo, as atividades restantes receberão nota 0.

### 1.2. Prazos

Apesar das atividades na Adalove exibirem prazos nas semanas 8, 9 e 10, cada
atividade ponderada possui um prazo específico, que será divulgado nesta seção,
na descrição de cada atividade e no Github Classrooms.

### 1.3. Pré-requisitos

Algumas atividades possuem pré-requisitos (exemplo: a atividade 5 exige a
conclusão da atividade 4). Essas dependências serão claramente indicadas aqui e
no enunciado da atividade.

### 1.4. Github Classrooms

Em breve mais detalhes.

## 2. Ponderadas

### 2.1. P1 - Processador de 8 Bits

**Pré-requisitos:** Nenhum.

**Descrição:** Nesta atividade, você construirá um processador de 8 bits
completo em um simulador de lógica. Explore arquiteturas simples como o SAP
(Simple as Possible) e implemente registradores, circuitos lógicos e E/S. Além
disso, desenvolva um conjunto enxuto de microcódigo.

**Prazo:** 08/09/2024

**Mais detalhes:** Em breve.

### 2.2. P2 - Visão Computacional em um ESP32

**Pré-requisitos:** Nenhum.

**Descrição:** Resolva um problema de visão computacional utilizando apenas um
microcontrolador (recomenda-se o ESP32). Considere um modelo que seja eficaz e
execute em um microcontrolador com recursos limitados.

**Prazo:** 21/09/2024

**Mais detalhes:** [link](./p2.md)

### 2.3. P3 - Concorrência em Microcontroladores

**Pré-requisitos:** P2.

**Descrição:** Utilize um framework de concorrência (sugestão: FreeRTOS) para
adicionar uma tarefa ao sistema de visão computacional da P2. Gerencie as
tarefas para executar a verificação de visão computacional e comunicar os
resultados a outro dispositivo sem fio.

**Prazo:** 21/09/2024

**Mais detalhes:** [link](./p3.md)

### 2.4. P4 - Framework de Inferência para Deep Learning

**Pré-requisitos:** Nenhum.

**Descrição:** Desenvolva o código-base para um framework de inferência
minimalista capaz de carregar e executar um arquivo de modelo em formato aberto
(exemplo: ONNX).

**Prazo:** 08/10/2024

**Mais detalhes:** [link](./p4.md)

### 2.5. P5 - Paralelismo para CPUs

**Pré-requisitos:** P4.

**Descrição:** Implemente paralelismo utilizando CPU no framework de inferência
da P4. Utilize ferramentas como OpenMP, MPI ou recursos nativos de paralelismo
de linguagens de sistema (não Python).

**Prazo:** 08/10/2024

**Mais detalhes:** [link](./p5.md)

### 2.6. P6 - Paralelismo para GPUs

**Pré-requisitos:** P4.

**Descrição:** Adicione paralelismo utilizando GPU ao framework de inferência
da P4. Devido a restrições, utilize CUDA (ROCm é permitido, mas não
recomendado) ou ferramentas de abstração como Bend.

**Prazo:** 10/10/2024

**Mais detalhes:** Em breve.

