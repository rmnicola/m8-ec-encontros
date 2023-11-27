---
title: Redes Neurais Convolucionais
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Redes neurais convolucionais

:::caution Aviso

O texto abaixo é basicamente um resumo traduzido (pelo GPT) do capítulo do
livro `Neural Networks and Depp Learning`. Se for para escolher apenas um
autoestudo para fazer (faça todos, o assunto é denso e vale a pena se expor a
mais de uma abstração), escolha o do `StatQuest`; é de **LONGE** o mais
acessível. Como tem vídeos longos e capítulos de livros, sugiro começar pelo
vídeo curto e ir consumindo o conteúdo aos poucos (mesmo que acabe indo para a
instrução sem ter visto/lido tudo)

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
        src="https://www.youtube.com/embed/NmLK_WQBxB4" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

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
        src="https://www.youtube.com/embed/HGwBXDKFk9I" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

<Admonition 
    type="info" 
    icon=<img src={require('/img/opcional.png').default} width='20vw' />
    title="Autoestudo">

[Livro Deep Learning - ler páginas
35-47](https://integrada.minhabiblioteca.com.br/reader/books/9786589881520/pageid/35)

[Livro Neural Networks and Deep learning - ler páginas
176-202](https://static.latexstudio.net/article/2018/0912/neuralnetworksanddeeplearning.pdf)

</Admonition>

As Redes Neurais Convolucionais (CNNs, do inglês Convolutional Neural Networks)
são uma forma especializada de rede neural projetada para tarefas de
classificação e reconhecimento de imagens. Essa arquitetura distinta aproveita
a estrutura espacial das imagens, ao contrário de modelos anteriores de redes
neurais que tratavam os pixels de entrada independentemente da sua disposição
espacial.

Conceitos-chave das Redes Neurais Convolucionais:

1. Campos Receptivos Locais: Em vez de conectar cada pixel de entrada a cada
   neurônio oculto, as CNNs concentram-se em regiões pequenas e localizadas da
   imagem de entrada. Por exemplo, um neurônio na primeira camada oculta pode
   estar conectado a uma região de 5x5 pixels da imagem de entrada, formando um
   'campo receptivo local'. Esta abordagem reflete a forma como as informações
   visuais são processadas nos sistemas biológicos, onde neurônios específicos
   respondem a estímulos em uma pequena região do campo visual.

2. Pesos e Viéses Compartilhados: As CNNs utilizam pesos e vieses
   compartilhados em diferentes posições da imagem de entrada. Isso significa
   que o mesmo detector de características (definido por um conjunto de pesos e
   um viés) é aplicado em várias localizações da imagem de entrada. Esse design
   explora a invariância translacional nas imagens - características como
   bordas, cantos e texturas são úteis independentemente de onde apareçam na
   imagem.

3. Camadas de Pooling: As CNNs frequentemente incluem camadas de pooling para
   reduzir o tamanho espacial da representação, diminuindo o número de
   parâmetros e a computação na rede. Isso também contribui para a invariância
   translacional da rede.

4. Redes Profundas com Múltiplas Camadas: O uso de camadas convolucionais e de
   pooling permite que as CNNs sejam profundas (com muitas camadas), o que é
   benéfico para classificar imagens complexas. Redes mais profundas podem
   aprender uma hierarquia de características, desde bordas simples nas camadas
   iniciais até padrões complexos nas camadas mais profundas.

5. Eficiência no Treinamento: Os pesos e vieses compartilhados nas CNNs não
   apenas ajudam a capturar as hierarquias espaciais nas imagens, mas também
   reduzem o número de parâmetros em comparação com redes totalmente
   conectadas. Isso torna as CNNs mais rápidas para treinar e mais eficientes
   em termos de recursos computacionais.

6. Prevalência no Reconhecimento de Imagens: Devido à sua eficácia no manuseio
   de dados de imagem, as CNNs se tornaram a arquitetura padrão para a maioria
   das tarefas de reconhecimento de imagens. Elas são particularmente adequadas
   para tarefas onde o reconhecimento de hierarquias espaciais de
   características é crucial, como no reconhecimento de escrita à mão ou
   identificação de características faciais.

Em resumo, as Redes Neurais Convolucionais são uma ferramenta poderosa no campo
do reconhecimento de imagens, oferecendo uma arquitetura que espelha certos
aspectos dos sistemas de visão biológica e é particularmente adequada para
tarefas envolvendo dados espaciais
