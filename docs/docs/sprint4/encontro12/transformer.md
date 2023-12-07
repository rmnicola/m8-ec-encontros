---
title: Transformers
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Transformers

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

    Assistir de 45:00 até o fim.

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/ySEx_Bqxvvo" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 1. Semelhança de cossenos

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/e9U0QAFbfLI" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

A semelhança de cossenos é uma medida fundamental na compreensão da relação
entre palavras em processamento de linguagem natural. Essa técnica é amplamente
utilizada para avaliar o quão semelhantes duas palavras são em termos de
significado, com base em suas representações vetoriais. Vamos explorar como
isso funciona, utilizando um exemplo simples com vetores one-hot.

### 1.1. Conceito Básico

A semelhança de cossenos mede o cosseno do ângulo entre dois vetores no espaço
multidimensional. Valores próximos a 1 indicam um alto grau de semelhança,
enquanto valores próximos a 0 indicam pouca ou nenhuma semelhança.

### 1.2. Exemplo

Em PLN, uma forma comum de representar palavras é por meio de vetores one-hot.
Neste método, cada palavra do vocabulário é representada por um vetor onde
apenas um elemento é 1 e todos os outros são 0. O tamanho do vetor é igual ao
número de palavras no vocabulário.

Suponha que temos um vocabulário simples com apenas três palavras: ["gato", "cachorro", "ave"].

- O vetor one-hot para "gato" seria [1, 0, 0].
- Para "cachorro", [0, 1, 0].
- E para "ave", [0, 0, 1].

**Calculando a Semelhança**

Para calcular a semelhança de cossenos entre duas palavras, primeiro
representamos essas palavras como vetores one-hot. Em seguida, usamos a fórmula
da semelhança de cossenos:

$$
\text{Semelhança} = \frac{A \cdot B}{\|A\| \|B\|}
$$

onde \( A \) e \( B \) são vetores e \( \|A\| \) e \( \|B\| \) são as normas desses vetores.

**Exemplo de Cálculo**

Vamos calcular a semelhança entre "gato" e "cachorro":

- Vetores one-hot: "gato" = [1, 0, 0], "cachorro" = [0, 1, 0].
- Produto escalar: [1, 0, 0] · [0, 1, 0] = 0.
- Normas: \| [1, 0, 0] \| = 1, \| [0, 1, 0] \| = 1.
- Semelhança de cossenos: 0 / (1 * 1) = 0.

A semelhança de cossenos entre "gato" e "cachorro" é 0, indicando que, de
acordo com essa representação, as palavras são completamente diferentes. Este é
um exemplo básico e, na prática, métodos mais sofisticados como vetores densos
(word embeddings) são utilizados para capturar melhor as nuances semânticas
entre as palavras.

## 2. Vector embeddings

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/viZrOnJclY0" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 3. Seq2seq e Encoder/Decoder

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/L8HKweZIOmg" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 4. Atenção

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/PSs6nxngL6k" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 5. Transformers

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/zxQyTK8quyY" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>
