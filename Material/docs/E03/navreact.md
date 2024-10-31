---
title: Navegação reativa
sidebar_position: 1
sidebar_class_name: autoestudo
slug: /navreact
---

import Strongest from '@site/static/img/strongest.jpg';
import Gepetada from '@site/static/img/gepetada.jpg';

# Introdução à navegação de robôs

:::warning em construção

<img 
  src={Strongest}
  alt="Strongest" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '20vh',
    marginRight: 'auto'
  }} 
/>
<br/>

Esta seção ainda é um esboço. Embora tudo o que é necessário para realizar os
seus estudos esteja aqui, ela ainda carece de uma revisão cuidadosa; o que
significa que ainda não tem o nível de qualidade que eu gostaria de entregar.
Sugiro que leia o material, mas volte novamente mais tarde para ler a versão
atualizada.

É, não deu tempo de fazer o texto inteiro a tempo =(

:::

:::warning gepetada

<img 
  src={Gepetada}
  alt="Gepetada" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '20vh',
    marginRight: 'auto'
  }} 
/>
<br/>

Esta seção contem GEPETADAS.

:::


> Navegar é preciso; viver não é preciso.
>
> *Fernando Pessoa*

Navegação reativa é uma abordagem na robótica em que o robô toma decisões
instantâneas com base em informações sensoriais obtidas em tempo real, sem a
necessidade de um mapa completo ou de planejamento prévio de rotas. Essa
técnica é particularmente útil em ambientes dinâmicos e desconhecidos, onde é
essencial reagir a obstáculos e mudanças imprevistas, adaptando o movimento
continuamente.

Na navegação reativa, o robô utiliza dados de sensores, como LIDAR,
ultrassônicos, câmeras ou sensores de proximidade, para detectar obstáculos,
identificar passagens livres e ajustar sua direção e velocidade de forma
segura. Diferente de métodos de navegação baseados em mapas, onde o caminho é
planejado antes do deslocamento, a navegação reativa segue o princípio de
estímulo-resposta, permitindo que o robô responda imediatamente a estímulos do
ambiente, como um desvio de última hora para evitar colisões.

Essa abordagem é comumente implementada com algoritmos que utilizam lógica
baseada em comportamentos, como o Braitenberg e o VFF (Virtual Force Field), ou
ainda redes neurais e métodos de aprendizado de máquina para identificar
padrões de navegação. Outra técnica popular é o método de potencial de campo,
onde o robô considera um destino atrativo e obstáculos como repulsivos,
resultando em uma trajetória que o leva ao objetivo enquanto evita colisões.

Apesar de suas vantagens em ambientes incertos e dinâmicos, a navegação reativa
tem limitações, como a falta de planejamento em longo prazo, o que pode levar o
robô a situações de impasse, como becos sem saída. Para superar essas
limitações, muitas aplicações combinam a navegação reativa com planejamento
global, criando uma abordagem híbrida onde a reatividade é usada para navegação
local enquanto um mapa geral orienta o robô em direção a seu objetivo final.

## 1. Navegação em robôs de competição

A navegação reativa é uma técnica crucial em robôs de competição, especialmente
em modalidades que exigem uma resposta rápida e precisa a mudanças no ambiente.
Em desafios como *Rescue*, *Seguidor de Linha* e *Micro Mouse*, os robôs
precisam tomar decisões instantâneas para lidar com obstáculos, desvios e
caminhos desconhecidos. Cada uma dessas competições exige que o robô adapte sua
trajetória e comportamento em tempo real, com base nos estímulos que recebe do
ambiente, sem depender de um mapa prévio ou de planejamento extensivo.

No *Rescue*, por exemplo, o robô deve navegar em um ambiente complexo que
simula uma situação de resgate, com obstáculos, superfícies irregulares e
locais que representam “vítimas”. Ele utiliza sensores, como LIDAR e
ultrassônicos, para identificar obstáculos e ajustar sua direção, reagindo
rapidamente a qualquer mudança. Algoritmos de potencial de campo são comuns,
onde obstáculos exercem uma força "repulsiva" sobre o robô, ajudando-o a
avançar em direção à área de resgate enquanto evita colisões.

Em competições de *Seguidor de Linha*, a navegação reativa se concentra na
tarefa de manter o robô alinhado com uma linha marcada no chão, frequentemente
com curvas e desvios. O robô detecta a linha usando sensores infravermelhos ou
de cor e ajusta continuamente sua trajetória para seguir o caminho. Nesse caso,
a navegação reativa envolve um controlador de feedback, como um controlador PID
(Proporcional-Integral-Derivativo), que ajusta a direção e velocidade do robô
com base nos desvios detectados, permitindo que ele siga o caminho com
precisão, mesmo em alta velocidade.

Já na modalidade *Micro Mouse*, o robô precisa encontrar o caminho mais curto
até o centro de um labirinto desconhecido. Aqui, ele explora e aprende a
estrutura do labirinto em tempo real, utilizando sensores de proximidade para
detectar paredes e bifurcações. Durante a navegação, o robô atualiza
continuamente seu mapa mental, combinando navegação reativa com uma estratégia
básica de mapeamento para escolher o melhor caminho a seguir. Mesmo ao
enfrentar desafios como becos sem saída, ele adapta seu comportamento
rapidamente para encontrar o trajeto ideal.

A navegação reativa é a chave para o sucesso desses robôs de competição, pois
permite que se adaptem rapidamente e respondam às demandas de ambientes
dinâmicos e desafiadores, essencial para alcançar bons resultados em provas que
exigem agilidade e precisão.

:::info autoestudo obrigatório

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/ZMQbHMgK2rw" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

:::

## 2. Máquinas de estado

Máquinas de estado são uma ferramenta poderosa na programação de robôs,
especialmente para implementar a navegação reativa. Uma máquina de estado é um
modelo computacional que define um conjunto de estados possíveis para um
sistema, assim como as transições entre esses estados com base em eventos
específicos. Cada estado representa uma configuração particular ou um
comportamento que o robô deve adotar, enquanto as transições ocorrem em
resposta a estímulos ou condições no ambiente. Isso torna as máquinas de estado
ideais para gerenciar comportamentos complexos e dinâmicos de forma
estruturada, permitindo que o robô alterne entre diferentes modos de operação
de maneira eficiente e previsível.

Na navegação reativa, as máquinas de estado são especialmente úteis para
modular e organizar as ações do robô em resposta a diferentes condições
ambientais. Por exemplo, um robô que navega em um ambiente de resgate pode ter
estados como "andar", "desviar de obstáculo", "inspecionar área" e "salvar
vítima". Cada um desses estados define um comportamento distinto que o robô
deve executar, e as transições entre eles são definidas por condições como a
presença de obstáculos ou a detecção de um ponto de interesse. Quando o robô
encontra um obstáculo, ele sai do estado de “andar” e transita para o estado de
“desviar de obstáculo”, onde executa a lógica necessária para ajustar sua rota
e evitar a colisão.

As máquinas de estado ajudam a simplificar o desenvolvimento de algoritmos de
navegação reativa ao permitir que cada estado tenha um comportamento específico
e independente. Isso facilita a adição de novos comportamentos e permite um
controle modular, onde o robô pode rapidamente responder a mudanças sem
depender de um script linear de ações. A modularidade também permite a
reutilização de estados em diferentes partes do programa, economizando tempo de
desenvolvimento e ajudando na manutenção do código.

Máquinas de estado também são fundamentais na construção de compiladores, onde
elas desempenham um papel crucial no processo de análise léxica e sintática.
Durante a análise léxica, o compilador utiliza autômatos finitos, um tipo
específico de máquina de estado, para dividir o código-fonte em tokens –
unidades mínimas como palavras-chave, operadores e identificadores. A máquina
de estado lê o código caractere por caractere, mudando de estado conforme
identifica padrões e categorias de tokens, como números, variáveis ou símbolos
de operadores. Além disso, na análise sintática, máquinas de estado mais
complexas, como autômatos de pilha, ajudam a verificar se a sequência de tokens
segue a gramática da linguagem, detectando estruturas de controle, expressões e
outras construções sintáticas. Esse processo possibilita que o compilador
interprete o código de maneira precisa, identificando erros e assegurando que o
programa segue a estrutura esperada da linguagem.
:::info autoestudo obrigatório

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/kb-Ww8HaHuE" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

:::

