---
title: Quaternions
sidebar_position: 5
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Representação de coordenadas por quaterions

:::tip Disclaimer

Este texto foi retirado e traduzido 
de https://eater.net/quaternions sem mais alterações. Honestamente, eu não 
saberia como deixar essa explicação melhor =)

:::

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
        src="https://www.youtube.com/embed/zjMuIxRvygQ" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 1. Visualizando quaternions

### 1.1. Quaternions e rotação 3D

Um dos principais usos práticos dos quaternions é em como eles descrevem a
rotação 3d. Estes primeiros dois módulos ajudarão você a construir uma intuição
de quais quaternions correspondem a quais rotações 3d, embora exatamente como
isso funciona permanecerá, por enquanto, um mistério. Análogo a abrir o capô de
um carro pela primeira vez, todas as partes serão expostas a você, especialmente
à medida que você examina mais de perto, mas entender como tudo se encaixa virá
com o tempo. Aqui estamos apenas olhando para o "o quê", antes do "como" e do
"porquê".

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw'/>
    title="Quaternions e rotação 3D (intro)" >

<a href="https://eater.net/quaternions/video/intro">Vídeo interativo</a>

</Admonition>

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Double cover">

<a href="https://eater.net/quaternions/video/doublecover">Vídeo interativo</a>

</Admonition>

### 1.2. Projeção estereográfica

Uma coisa que torna os quaternions tão desafiadores é que eles existem e atuam
em quatro dimensões, o que é extremamente difícil (impossível?) de visualizar.
Felizmente, podemos construir uma intuição para a multiplicação de quaternions e
como ela calcula a rotação em 3d apenas focando nos quaternions unitários,
aqueles que estão a uma distância 1 da origem. Estes formam uma hiperesfera no
espaço 4d, que ainda é realmente difícil de pensar, mas felizmente os
matemáticos têm uma ferramenta à sua disposição que torna mais fácil pensar 
sobre uma hiperesfera completa nos limites de nosso mundo 3d: Projeção estereográfica.

É mais fácil começar a entender essa ideia em um contexto de dimensão inferior,
como mapear a superfície de uma esfera em um plano 2d. Os entusiastas da
geografia entre vocês saberão que existem muitas táticas diferentes para exibir
a superfície da terra em um plano 2d. Aqui está como ficaria usando uma projeção
estereográfica: 

![](/img/stereo_globo.png)

Em princípio, isso realmente se estenderia para preencher todo o espaço 2d, com 
a Antártica se estendendo até o infinito. Talvez um método como este, que distorce 
lo hemisfério sul de forma tão dramática a ponto de dar aos pinguins um território 
infinito, pareça muito pior do que outros tipos de projeção. Mas para um matemático, 
esta projeção apresenta uma série de propriedades interessantes. Por exemplo, 
qualquer círculo desenhado na superfície da terra permanece um círculo após esta 
projeção. Além disso, não há cortes estranhos ou descontinuidades (desde que 
consideremos todos os caminhos para fora convergindo para um único "ponto no infinito"). 
Quando chegarmos à visualização da multiplicação de quaternions, que é toda sobre 
pensar em rotações contínuas, a ideia de círculos permanecendo círculos e evitando 
cortes estranhos será realmente bem-vinda.

Para entender como isso funciona, começaremos em duas dimensões e avançaremos a partir daí.

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Projeção estereográfica 2D">
<a href="https://eater.net/quaternions/video/stereo2d">Vídeo interativo</a>
</Admonition>

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Projeção estereográfica 3D">
<a href="https://eater.net/quaternions/video/stereo3d">Vídeo interativo</a>
</Admonition>

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Projeção estereográfica 4D">
<a href="https://eater.net/quaternions/video/stereo4d">Vídeo interativo</a>
</Admonition>

### 1.3. Multiplicação de Quaternions

Como você multiplica dois números complexos? Bem, você começa usando a lei
distributiva. 

$$
(2+3i)(4+5i)=2\cdot4+2\cdot5i+3i\cdot4+3i\cdot5i
$$

E então usa a regra que \(i^2 = -1\) para simplificar ainda mais.

$$
2\cdot4+\color{purple}2\cdot5i+3i\cdot4\color{default}+\color{red}3\cdot5i^2\\
\color{default}=(2\cdot4-\color{red}3\cdot5\color{default})+(\color{purple}
2\cdot5+3\cdot4\color{default})i\\
=-7+22i
$$

Multiplicar dois quaternions é mais complicado, mas em princípio não muito
diferente. Existem algumas regras de como ii, jj e kk se multiplicam entre si, e
a multiplicação é realizada distribuindo e simplificando.

$$
ij = -ji = k \\
jk = -kj = i \\
ki = -ik = j,
$$

Isso é o que os computadores fazem, e é o que seu computador está fazendo nas
visualizações que você verá abaixo. Mas saber como calcular produtos é apenas
uma forma de entender a multiplicação. Assim como a multiplicação por números
reais é mais compreensível ao visualizar um processo de escala ou compressão, e
entender a multiplicação complexa é facilitado ao entender como eles rotacionam
pontos no plano, a multiplicação de quaternions pode ser entendida olhando como
ela transforma o espaço quadridimensional.

Esta não é uma ideia simples nem uma visualização simples, mas com alguma
paciência, entender a multiplicação de quaternions desta maneira pode
esclarecer por que a multiplicação de quaternions descreve a rotação 3d da
maneira que o faz. Limitaremos nossa visão desta ação à hiperesfera unitária,
conforme visualizada sob uma projeção estereográfica preenchendo a totalidade
do nosso espaço 3d.

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Multiplicação de quaternions">
<a href="https://eater.net/quaternions/video/quatmult">Vídeo interativo</a>
</Admonition>

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Rotação de quaternions">
<a href="https://eater.net/quaternions/video/rotation">Vídeo interativo</a>
</Admonition>

## 2. Quatérnios em ROS

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Fundamentos de quatérnios
](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Quaternion-Fundamentals.html)

</Admonition>
