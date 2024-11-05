--
title: Revisão ROS
sidebar_position: 1
sidebar_class_name: autoestudo
slug: /ros
---

import SkillIssue from '@site/static/img/skill_issue.jpg';

# Revisão dos conceitos básicos de ROS

:::warning alerta de skill issue

<img 
  src={SkillIssue}
  alt="Skill issue" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '20vh',
    marginRight: 'auto'
  }} 
/>
<br/>

Se você tem intenção de fazer os exercícios desta seção utilizando C++,
sugere-se fortemente que procure sobre os seguintes conceitos da linguagem:

* Ponteiros;
* Alocação dinâmica;
* Ponteiros únicos, compartilhados e fracos;
* Lambdas;
* Makefile;
* Cmake;
* Parâmetros por valor, por ponteiro, por referência e por referência
  constante.

:::

## 1. Workspaces e pacotes

> Give me six hours to chop down a tree and I will spend the first four
> sharpening the axe.
>
> *Abraham Lincoln*

Embora seja um passo frequentemente negligenciado por principiantes, a
configuração adequada de um ambiente de desenvolvimento - tal qual a faca de
um açougueiro - marca a diferença entre uma experiência de trabalho frustrante
e aquela que pode ser utilizada por anos, sem causar qualquer tipo de fadiga
antecipada. Sendo assim, para esta revisão, vamos primeiro olhar para como
criar um ambiente propício para desenvolvimento de projetos com ROS.

Existe uma diferença palpável entre linguagens de programação mais antigas -
como C++ e C - e suas irmãs mais novas e, no geral, mais bem quistas pelos
desenvolvedores - como Zig, Rust e Go -; o sistema de gerenciamento e
distribuição de projetos. Linguagens tão antigas quanto as da "família" C
surgiram quando os programadores da época ainda vislumbravam vultos no fundo da
caverna, vultos esses que eram projeções de um futuro que ainda estava longe de
existir. Tenho certeza de que uma dessas formas responsáveis por projeções
assombrosas era a de um *gerenciador de pacotes*.

Os desenvolvedores de ROS - tendo escolhido C++ como a linguagem base para o
seu novo sistema - tiveram que dar forma a esse vulto. A solução deles envolve
uma ferramenta chamada **colcon**, responsável pela construção de *workspaces*
e *pacotes*.

Um **pacote** consiste em uma unidade *coesa* de sistema desenvolvido em
ROS. Pela natureza da própria ferramente, que permite sistemas com baixíssimo
acoplamento, convencionou-se a criação de pacotes que seguem uma filosofia que
muito se assemelha ao preconizado por sistemas baseados em
[Unix](https://en.wikipedia.org/wiki/Unix_philosophy).

Pela natureza modular de pacotes, ainda se faz necessário o uso de
*workspaces*, que servem para agregar um ambiente de desenvolvimento que pode
conter um ou mais pacotes. A vantagem de se ter uma workspace é poder compilar
e distribuir pacotes que tenham forte relação entre si - como todos os pacotes
que servem para fazer um robô como o *Turtlebot* funcionar.

:::note Exercício 1

Siga o [tutorial
oficial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html#)
 e crie um *workspace* ROS.

:::

:::note Exercício 2

Crie um pacote em ROS seguindo o [tutorial
oficial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).

:::

## 2. Tópicos

Tópicos são a forma de comunicação mais comum oferecida pelo *framework* ROS.
Entenda um tópico como o canal onde se dá a comunicação entre os nós
*produtores* - ou aqueles que **publicam** algo - e os nós *consumidores* - ou
aqueles que se **inscrevem** nos tópicos -; ou seja, o tópico é um fluido que
sustenta a implementação do padrão *observer* utilizando amplamente em ROS. 

:::note Exercício 3

Utilizando Python ou C++, adicione ao seu pacote um nó capaz de *publicar* a
mensagem "Ola, mundo" em um tópico chamado "teste". Ainda no mesmo pacote, crie
um nó capaz de se **inscrever** no tópico "teste" e, consumindo a mensagem
enviada, exibe-a no terminal.

:::

:::note Exercício 4

Crie um novo pacote em seu workspace - utilizando como base o pacote que
implementa o *turtlesim* - e, nele, crie um nó capaz de enviar comandos para a
tartaruga simulada, recebendo como entrada valores digitados pelo usuário
diretamente no terminal.

:::

## 3. Serviços

Embora a estrutura oferecida pelo padrão *observer* tenha vantagens muito
claras - como a drástica diminuição do acoplamento entre os nós do sistema -,
ela não é uma bala de prata, que pode ser utilizada em qualquer ocasião sem
qualquer sorte de desvantagem. O custo cobrado por esse sistema com baixo
acoplamento é a **incapacidade de garantir sincronia** na comunicação entre os
nós. Esta qualidade, no entanto, é uma das características marcantes de um dos
padrões de arquitetura mais comum e que sustenta a esmagadora maioria dos
serviços *web*; o padrão cliente-servidor.

Em ROS, existe a possibilidade de adotar esse padrão de comunicação através do
uso de **serviços**. Quando usamos serviços, passa a existir a relação de
*cliente* e *servidor* entre os nós envolvidos. Com efeito, passa a ser
necessário que o cliente faça um *requisição*, que deve ser respondida em tempo
hábil pelo nó responsável por servir uma *resposta* ao cliente.

:::note Exercício 5

Utilizando a interface padrão *AddTwoInts*, crie um serviço que, quando
chamado, some dois valores inteiros - contidos na requisição - e retorne como
resposta o resultado da soma.

:::
