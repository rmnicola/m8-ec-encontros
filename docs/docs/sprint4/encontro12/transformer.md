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

Após entendermos como a semelhança de cossenos é aplicada usando vetores
one-hot para representar palavras, vamos avançar para um conceito mais
sofisticado e poderoso em processamento de linguagem natural: o uso de redes
neurais para criar vetores de incorporação, conhecidos como embeddings. Esses
embeddings capturam muito mais do contexto e do significado semântico das
palavras do que os vetores one-hot.

### 2.1. Introdução aos Embeddings de Palavras

Embeddings de palavras são representações vetoriais densas onde palavras com
significados ou contextos semelhantes têm representações semelhantes. Diferente
dos vetores one-hot, que são esparsos e de grande dimensão, embeddings são
compactos e contínuos, permitindo que nuances e relações semânticas sejam
capturadas de forma mais eficiente.

### 2.2. O Papel das Redes Neurais

Redes neurais, especialmente as redes neurais profundas, são cruciais na
geração desses embeddings. Um modelo popular para isso é o Word2Vec, que
utiliza uma rede neural simples para aprender representações vetoriais de
palavras a partir de grandes conjuntos de dados textuais. O modelo pode ser
treinado de duas maneiras: Skip-gram e Continuous Bag of Words (CBOW). Ambos os
métodos visam prever palavras com base em seu contexto (ou vice-versa), e
através desse processo, o modelo aprende embeddings que refletem os padrões
semânticos e sintáticos das palavras.

### 2.3. Aplicação ao Nosso Exemplo

Retomando o nosso exemplo anterior com o vocabulário ["gato", "cachorro",
"ave"], ao invés de usar vetores one-hot, empregamos uma rede neural para
aprender embeddings para estas palavras. Suponha que após o treinamento,
obtemos os seguintes embeddings:

- "gato": [0.8, -0.1, 0.3]
- "cachorro": [0.7, -0.2, 0.4]
- "ave": [-0.1, 0.9, -0.5]

Note que estes vetores são mais densos e contêm valores em todas as dimensões.

### 2.4. Comparando com a Semelhança de Cossenos

Agora, se calculássemos a semelhança de cossenos entre "gato" e "cachorro"
usando esses embeddings, o resultado seria significativamente diferente do
exemplo com vetores one-hot. Aqui, os vetores não são ortogonais e, portanto, a
semelhança de cossenos não seria 0, indicando uma maior semelhança semântica
entre as palavras.

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

Dando sequência aos tópicos abordados anteriormente sobre a semelhança de
cossenos com vetores one-hot e o uso de redes neurais para criar embeddings de
palavras, vamos explorar agora uma aplicação avançada dessas tecnologias no
campo do processamento de linguagem natural: as tarefas de sequência para
sequência (seq2seq) com arquiteturas de encoder-decoder, utilizando camadas de
embeddings e redes LSTM (Long Short-Term Memory).

### 3.1. Tarefas Seq2Seq

As tarefas seq2seq envolvem a conversão de uma sequência de entrada em uma
sequência de saída, onde as duas sequências podem ter comprimentos diferentes.
Exemplos comuns incluem tradução automática, resumo de texto e geração de
legendas para imagens. 

### 3.2. Arquitetura Encoder-Decoder

A arquitetura encoder-decoder é um framework poderoso para lidar com tarefas
seq2seq. O encoder processa a sequência de entrada e compacta a informação em
um vetor de contexto, uma representação densa de toda a sequência de entrada. O
decoder, então, usa este vetor para gerar a sequência de saída passo a passo.

### 3.3. Camadas de Embeddings

As camadas de embeddings são utilizadas tanto no encoder quanto no decoder para
converter palavras (ou tokens) em vetores densos. Esses embeddings são
geralmente aprendidos durante o treinamento do modelo e ajudam a capturar os
significados semânticos das palavras, como discutido no artigo anterior.

### 3.4. Redes LSTM

LSTMs são uma forma especializada de redes neurais recorrentes (RNNs) que são
capazes de aprender dependências de longo prazo. Elas são ideais para tarefas
seq2seq devido à sua habilidade de manter informações relevantes ao longo de
sequências longas, evitando o problema de desvanecimento do gradiente, comum em
RNNs tradicionais.

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

Continuando nossa série de artigos sobre avanços no processamento de linguagem
natural, vamos agora focar em um conceito revolucionário que tem melhorado
significativamente o desempenho das arquiteturas de encoder-decoder: a mecânica
de atenção. Este conceito é particularmente importante em tarefas seq2seq, como
tradução automática, onde a capacidade de focar em partes específicas da
entrada durante a decodificação é crucial.

### 4.1. O Problema do Encoder-Decoder Tradicional

Nas arquiteturas encoder-decoder convencionais, todo o conteúdo da sequência de
entrada é comprimido em um único vetor de contexto fixo. Esse vetor é então
usado pelo decoder para gerar a sequência de saída. Um grande desafio aqui é
que o vetor de contexto pode se tornar um gargalo, especialmente para
sequências longas, onde é difícil para o modelo manter todas as informações
relevantes apenas nesse vetor.

### 4.2. Introdução à Mecânica de Atenção

A mecânica de atenção foi introduzida como uma solução para o problema do vetor
de contexto fixo. Em vez de forçar o modelo a depender de um único vetor de
contexto, a atenção permite que o decoder foque em diferentes partes da
sequência de entrada em cada etapa da decodificação. Isso é semelhante ao modo
como os humanos prestam atenção a diferentes partes de uma frase ou imagem
quando estão tentando entender ou responder a algo.

### 4.3. Como Funciona a Atenção

1. **Pontuação de Atenção**: Primeiramente, o modelo calcula um conjunto de
   pontuações de atenção. Estas pontuações determinam o quanto o modelo deve se
   focar em cada parte da entrada ao gerar cada palavra da saída.

2. **Pesos de Atenção**: As pontuações são então normalizadas para formar uma
   distribuição de probabilidade (pesos de atenção). Esses pesos decidem a
   importância relativa de cada palavra na entrada para a geração da próxima
   palavra na saída.

3. **Vetor de Contexto Dinâmico**: Usando esses pesos, um vetor de contexto
   ponderado é gerado para cada etapa da decodificação. Esse vetor é uma
   combinação das representações de entrada, ponderadas pela sua relevância
   atual.

4. **Decodificação com Atenção**: O decoder, em cada etapa, utiliza este vetor
   de contexto dinâmico, junto com o estado oculto anterior, para gerar a
   próxima palavra da sequência de saída.

### 4.4. Vantagens e Aplicações

A introdução da atenção melhora significativamente a capacidade dos modelos
seq2seq, especialmente em tarefas como tradução automática, onde a
correspondência entre as partes da entrada e da saída é crítica. Com atenção,
os modelos podem se concentrar em partes relevantes da entrada para cada
palavra da saída, o que é particularmente útil para lidar com frases longas e
complexas.

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
