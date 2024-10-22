---
title: Introdução
sidebar_position: 1
slug: /
---

# Robótica de serviço

<img 
  src="img/honored_bun.jpg"
  alt="Throughout the heavens and earth, I alone am the honored bun." 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '40vh',
    marginRight: 'auto'
  }} 
/>
<br/>

> I can't define a robot, but I know one when I see one.
>
> *Joseph F. Engelberger*

O que é um robô? 

Essa é uma pergunta que, até hoje, após mais de 10 anos trabalhando com robôs,
de vez em quando se prende em minha consciência. Não é sempre que ela se
apresenta, mas em situações bastante particulares; como quando vejo
apresentações de bilionários excêntricos reproduzindo cenas de obras
distópicas em ambientes manipulados ou quando me sento em frente a um robô
humanoide mais velho que a maioria de meus alunos, observando-o pular, dançar e
interagir com o público. Ainda não tenho uma resposta definitiva para esta
dúvida, mas posso apresentar alguns pensamentos e fatos que vão servir para
equalizar nossas expectativas quando utilizarmos o termo daqui para a frente.

O termo robô data do século XX, mais especificamente de uma obra de 1920,
*Rossum's Universal Robots*. Nesta obra, o autor tcheco *Karel Capek* apresenta
uma sociedade que emprega o uso de seres artificiais cuja missão é única e
exclusivamente servir aos humanos. A história apresenta um dilema filosófico
que passou a ser comum à temática de robôs: poderiam criaturas criadas
artificialmente ter direitos similares aos dos seres humanos? Essa indagação é
particularmente engajante, pois provoca a reflexão do que exatamente tornaria
os seres humanos diferentes de uma máquina - dotada da capacidade de pensar e
sentir - perante a moral que permeia nossa sociedade. Em sua busca por um termo
que sintetiza as máquinas apresentadas em sua obra, *Capek* pegou emprestado de
sua língua nativa o termo *robota*, que significa *trabalho forçado*. Em *RUR*,
assim como em muitas das obras de ficção ocidentais que viriam depois, a
relação de opressão entre humanos e robôs termina em uma revolução das
máquinas.

<img 
  src="https://cdn.sanity.io/images/7p2whiua/production/c07a650456a5621dc25aade40d14c3897babcfee-2048x1536.jpg?w=900&auto=format"
  alt="Robô ASIMO" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '30vh',
    marginRight: 'auto'
  }} 
/>
<br/>
<p><center>Fig. 1 - O ASIMO é um robô desenvolvido pela Honda. Embora ele tenha
sido atualizado no decorrer dos anos, o seu surgimento foi em 2000. O nome é
uma romanização de *ashi mo* - cujo significado alude ao fato de que ele possui
pernas - e ele continua a ser exposto até hoje no museu do futuro, em
Tóquio.</center></p>

Obras como a de *Capek* e futuramente as de *Isaac Asimov* alimentaram o
imaginário coletivo e condicionaram-nos a pensar em robôs como figuras
humanoides, com características antropomórficas e capacidades similares, se não
superiores, às de um ser humano. Existe, no entanto, um abismo de distância
entre os primeiros robôs dos quais temos notícias e até mesmo de robôs
humanoides clássicos como o *ASIMO*, da *Honda*, para os robôs apresentados
nessas obras de ficção científica. Não devemos, portanto, mirá-las como pauta
para nossas discuções sobre o que são robôs e como categorizá-los.

Vamos voltar um pouco no tempo. No século XVIII, o inventor francês *Jacques de
Vaucanson* produziu uma série de autômatos. Entre eles, um pato mecânico capaz
de andar, ingerir grãos, processá-los e defecá-los. A invenção de Vaucanson
flerta com a definição de robôs, pendendo para a definição deste ou de um
autômato dependendo do ponto de vista de quem o avalia.

<img 
  src="https://assets-us-01.kc-usercontent.com/9dd25524-761a-000d-d79f-86a5086d4774/1376dcd8-6266-46b7-b5ad-7a762082833a/DEVaucanson5.jpg?w=634&h=600&auto=format&q=75&fit=crop"
  alt="Pato de Vaucanson" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '30vh',
    marginRight: 'auto'
  }} 
/>
<br/>
<p><center>Fig. 2 - O pato de Vaucanson era capaz de andar, sincronizando os
movimentos de suas patas com um sistema similar ao de um relógio mecânico. Era
capaz, também, de ingerir grãos, moê-los em uma série de engrenagens e
expelí-los após a "digestão".</center></p>

Sob um ponto de vista utilitarista, qualquer pessoa estaria perdoada de julgar
como frívolo o esforço em automatizar um pato, fazendo-o defecar grãos por ele
mesmo processados. Há, no entanto, uma intangibilidade com relação a utilidade
das invenções humanas. O pato de Vaucanson impressionou o então jovem *Charles
Babbage* e o influenciou na criação de uma máquina que mudaria o rumo da
sociedade e elevaria ao patamar de primeira programadora da história uma de
suas colegas e consultoras, chamada *Ada Lovelace*, mas esse é um assunto para
um outro módulo.

Foi apenas depois do desenrolar das máquinas de *Babbage* e todos aqueles que
seguiram em seu rastro que houve um novo salto no campo da robótica, dessa vez
criando aquele que pode ser chamado sem erros de o primeiro robô industrial.
Com uma patente depositada pelo inventor *George C. Devol* e aceita no ano de
1954, o *Unimation* era um manipulador movido por trilhos capaz de se
movimentar com três graus de liberdade no total, utilizando uma garra
motorizada para manipular objetos em uma linha de montagem.

<img 
  src="https://www.thehenryford.org/linkedpub-image/qY8EE1_447shRg1F7LyjmbuscyLUg_WU7vXb3cTQvhcTj2k8m7PQdRYBOY4iQFWapWU2OGZlQIZfowKuCYrNMA"
  alt="Unimation" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '30vh',
    marginRight: 'auto'
  }} 
/>
<br/>
<p><center>Fig 3. - O Unimation foi o primeiro robô instalado em uma linha de
montagem, no início dos anos 60.</center></p>

Robôs como o *Unimation* só se tornaram possível com o advento dos computadores
eletrônicos. Com eles, foi possível criar máquinas que - mais do que só se
movimentar de forma controlada - conseguiam de certa forma perceber o mundo ao
seu redor e - mesmo que de modo rudimentar - eram capazes de tomar decisões com
base na informação capturada.

Uma definição de robótica pode ser, portanto, traçada entre os pontos
históricos definidos pelo pato de *Vaucanson* e o *Unimation*, de *Devol*. Para
todos os efeitos, utilizaremos a seguinte definição para robôs:

> Um robô é uma máquina orientada a objetivos capaz de detectar, planejar e
> agir.
>
> *Peter Corke*

A definição acima, encontrada no livro **Robotics, vision and control**, do
autor *Peter Corke*, pode não ser a definição que encerra toda e qualquer
discussão a respeito de como definir um robô. Mesmo assim, ela será bastante
útil para que possamos continuar estudando os mecanismos que fazem um robô
funcionar.

## 1. Taxonomias da robótica

A categorização é uma das ferramentas mais utilizadas em nossa busca por
desvendar as leis que regem o universo que nos cerca. Talvez essa seja a
justificativa mais plausível para a nossa afinidade por taxonomias. Essa
afinidade afeta, também, o mundo da robótica. Existem duas diferentes
taxonomias para classificar e agrupar os mecanismos que podem ser chamados de
robôs; são elas a **taxonomia por tipo de movimentação** e a **taxonomia por
função**.

A taxonomia por tipo de movimentação é um tanto simples: ou um robô é *móvel*
ou não é. Sendo assim, ela é particularmente útil para distinguir o tipo de
robôs cujo estudo depende fortemente do estudo de uma cadeia cinemática fechada
daqueles em que é particularmente mais interessante entender a dinâmica que
rege sua locomoção e o desempenho dela em diversos tipos de terrenos.

A taxonomia por função apresenta um esforço mais completo de classificação das
diferentes máquinas robóticas que atuam em nossa sociedade. Nela, temos as
seguintes divisões:

* Robôs de manufatura;
* Robôs de campo;
* Robôs teleoperados; e
* Robôs de serviço.

Os **robôs de manufatura** são melhor representados pelos braços mecânicos que
hoje ocupam uma parcela significativa das linhas de montagem industriais.
Tratam-se de robôs feitos para ter pouca ou nenhuma interação com seres
humanos, mantendo-se fixos e com acesso a mecanismos de alimentação de insumos
como esteiras ou dispensers. A disposição de sua cadeia cinemática é feita para
maximizar a produtividade em uma linha de montagem, com movimentos de alta
velocidade e baixo consumo energético.

<img 
  src="https://revistapotencia.com.br/wp-content/uploads/2022/11/KUKA.png"
  alt="SIVOR" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '40vh',
    marginRight: 'auto'
  }} 
/>
<br/>
<p><center>Fig. 4 - O projeto SIVOR, desenvolvido no CCM - ITA, apresenta um
exemplo de uso de robôs de manufatura que foge um pouco do convencional. Nesse
projeto, um cockpit foi acoplado no final da cadeia de um robô KUKA KR1000 e,
contando com filtros que traduzem a dinâmica de uma aeronáve para o volume de
trabalho de uma plataforma robótica, pode ser utilizado para treinamento de
pilotos em ambiente de simulação.</center></p>

Os **robôs teleoperados** apresentam um desafio de transmissão de dados com a
menor latência possível e de locomoção por terrenos variados. Este tipo de robô
pode ser completamente teleoperado ou apenas receber objetivos de um operador a
distância. Um exemplo de robô completamente teleoperado são os ROV's utilizados
para inspecionar os destroços do Titanic. Por outro lado, o Mars rover, da
NASA, recebe apenas objetivos de seu operador na Terra e navega de forma
autônoma na superfície de Marte.

<img 
  src="https://oceanconservancy.org/wp-content/uploads/2023/01/JasonJr_TitanicROV_WoodsHole-1024x683.webp"
  alt="Titanic ROV" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '30vh',
    marginRight: 'auto'
  }} 
/>
<br/>
<p><center>Fig. 5 - Os destroços do navio Titanic encontram-se em uma
profundidade de aproximadamente 3800 metros. Nesta profundidade, uma embarcação
feita para carregar seres humanos teria bastante dificuldade de resistir à
pressão exercida pelo volume de água. Uma solução encontrada para inspecionar
os destroços do famoso naufrago foi o uso de robôs teleoperados.</center></p>

Os *robôs de campo* e os *robôs de serviço* apresentam como o seu maior desafio
o *mapeamento e navegação* em ambientes complexos e sem estabilidade temporal.
Sendo assim, tratam-se de robôs equipados com dois tipos de sensores:

* Os sensores *proprioceptivos* são aqueles que medem o estado do robô - a
  movimentação dos seus motores, a sua pose ou localização - em todos os
  instantes. Esses sensores são fundamentais para a implementação de
  estratégias de controle.
* Os sensores *exteroceptivos* servem para detectar o ambiente ao redor do
  robô. Entre eles, os sensores típicos envolvem LIDAR, câmeras, sensores
  infravermelho ou ultrassônicos. Sem esses sensores, seria impossível coletar
  informações necessárias para navegar em ambientes complexos.

Além disso, no caso específico dos *robôs de serviço* é de fudamental
importância estudar cuidadosamente a maneira como esses dispositivos interagem
com os seres humanos, tendo em vista que sua razão de existir envolve
satisfazer uma necessidade ou vontade de uma pessoa.

Neste módulo, nosso foco total será na *robótica de serviço*. Isso significa
que vamos estudar os dois principais desafios que envolvem o desenvolvimento
desse tipo de solução robótica:

1. Mapeamento de navegação autônoma; e
2. Interação com seres humanos utilizando interfaces simples (e.g. uma
   interface gráfica) e complexas (e.g. linguagem natural).

<img 
  src="https://provenrobotics.ai/wp-content/uploads/2023/09/2.webp"
  alt="BellaBot" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '30vh',
    marginRight: 'auto'
  }} 
/>
<br/>
<p><center>Fig. 6 - O BellaBot é um robô de serviço criado para a industria
hospitaleira. Ele é bastante empregado como um robô garçom em estabelecimentos
como restaurantes e cafés. Além de sensores que o permitem mapear um ambiente e
navegar nele, detectando obstáculos em tempo real, o BellaBot apresenta uma
preocupação com a estética e a interface com o usuário.</center></p>

Antes de seguirmos em frente, vou aproveitar que tenho sua atenção para fazer
um **anúncio** de **extrema importância**. Se liga, que logo abaixo vem o
admonition:

:::danger

Esse material **NÃO** substitui de forma alguma o uso da **Adalove**. Você
**DEVE** entrar na Adalove com frequência e **REGISTRAR O SEU PROGRESSO**.
Entendeu? Ainda não? Pera aí que vou desenhar:

<img 
  src="img/aviso-adalove.png"
  alt="ACESSE A ADALOVE" 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '40vh',
    marginRight: 'auto'
  }} 
/>

:::

Beleza, agora podemos seguir em frente.

## 2. Ementa do módulo

:::warning

Essa é a **ementa oficial** do módulo. O texto é sucinto e formal pois ele faz
parte de um documento **apresentado ao MEC** no momento em que o curso é
reconhecido. A ementa é um dos itens que **obrigatoriamente** deve ser
**mostrado aos alunos**. O que estou fazendo agora? Mostrando a ementa do
módulo para vocês. Sem mais dúvidas, certo?

:::

Este módulo tem como objetivo desenvolver um sistema que integra robôs
móveis com algoritmos de mapeamento e navegação autônoma e inteligência
artificial generativa, com a finalidade de atuar como robôs de serviço capazes
de processar e gerar linguagem natural. Para tal, abordam-se os assuntos de
álgebra linear, transformação de base de rotação, quaternions, mecanismos de
atenção, transformadores, Simultaneous Localization and Mapping (SLAM), design
patterns, conceitos de processamento de linguagem natural, sintetização de voz,
fabricação digital e Computer Aided Design (CAD). A solução proposta pelos
estudantes deverá considerar aspectos como privacidade e garantir que a
construção do modelo de IA seja feita de forma cuidadosa e ética, evitando
vieses e garantindo a inclusão de dados que representem adequadamente a
diversidade da população,  fomentando a igualdade étnico-racial. Além destes
pontos, são apresentadas ferramentas de teste de interface com o usuário,
visando validar a experiência proposta. Quanto à abordagem de negócios, são
apresentados os conceitos de planejamento estratégico, estudo das ondas de
inovação tecnológica e representação técnica de projetos de engenharia. Os
estudantes também serão estimulados a exercitar a capacidade de tomada de
decisão estratégica e de entendimento de relações de poder, de teambuilding e
de networking, para se desenvolverem nas organizações onde irão atuar. Ao final
do módulo, os estudantes deverão ser capazes de compreender os conceitos
envolvidos nos algoritmos clássicos de mapeamento e localização simultânea,
estando apto a integrá-los em sistemas com inteligência artificial
generativa utilizando boas práticas de design e engenharia de software


## 2. Organização do material

Vamos conversar sobre como esse material foi organizado? Isso vai ser
importante para você não se perder por aqui e conseguir identificar rapidamente
quais seções vão ser as mais importantes para você o mais rápido possível (e
quais **valem nota** também =O). Vamos começar falando dos **ícones** que vocês
vão ver por aqui.

### 2.1. Glossário de ícones

O objetivo desse material é facilitar sua vida e diminuir a distância entre
você e as informações necessárias para que você faça um projeto espetacular.
Para isso, é essencial que as informações aqui dispostas sejam muito fáceis de
categorizar só batendo o olho. Qual a melhor forma de fazer isso? Usando ícones
padronizados. Em cada seção de conteúdo, você vai ver um **ícone à esquerda do
título da seção**. Aqui estão os ícones que você vai encontrar e o que eles
significam:

<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center',
margin: '0' }}>
    <table>
        <tr>
            <th>Ícone</th>
            <th>Descrição</th>
        </tr>
        <tr>
            <td style={{textAlign: "center", verticalAlign: "middle"}}>
                <img src="icons/artefato.svg"/>
            </td>
            <td style={{textAlign: "left", verticalAlign: 'top', paddingTop:
            '25px' }}>
                Significa que a seção vai conter o detalhamento de um ou mais
                **artefatos** do metaprojeto.
            </td>
        </tr>
        <tr>
            <td style={{textAlign: "center", verticalAlign: "middle"}}>
                <img src="icons/autoestudo.svg"/>
            </td>
            <td style={{textAlign: "left", verticalAlign: 'top', paddingTop:
            '25px' }}>
                Significa que a seção é um autoestudo **obrigatório**.
            </td>
        </tr>
        <tr>
            <td style={{textAlign: "center", verticalAlign: "middle"}}>
                <img src="icons/opcional.svg"/>
            </td>
            <td style={{textAlign: "left", verticalAlign: 'top', paddingTop:
            '25px' }}>
                Significa que a seção é um autoestudo **opcional**.
            </td>
        </tr>
        <tr>
            <td style={{textAlign: "center", verticalAlign: "middle"}}>
                <img src="icons/ponderada.svg"/>
            </td>
            <td style={{textAlign: "left", verticalAlign: 'top', paddingTop:
            '25px' }}>
                Significa que a seção descreve o enunciado de uma atividade que
                **vale nota**.
            </td>
        </tr>
    </table>
</div>

## 3. Bibliografia

:::warning

Sou eu novamente. Só vim avisar que mostrar a bibliografia do módulo para vocês
também é **obrigatório** de acordo com o MEC. O que estou fazendo aqui? Estou
mostrando a bibliografia para vocês.

:::

### 3.1. Bibliografia básica

**COMPUTAÇÃO**

* CASTRUCCI, P. de L.; BITTAR, A.; SALES, R. M. Controle automático. 2. ed. Rio de Janeiro: LTC, 2018.

* [Link minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788521635628)

* O livro aborda os principais conceitos e técnicas em controle automático, como
sistemas de controle de malha aberta e fechada, controle PID, projeto de
controladores, análise de resposta transitória e estabilidade e controle
adaptativo. Além disso, o livro é atualizado para refletir as últimas
tendências em controle automático, tornando-se uma leitura obrigatória para
pessoas interessadas nessa área.

**COMPUTAÇÃO**

* DINIZ, P. S. R. Processamento digital de sinais: projeto e análise de sistemas. 2. ed. Porto Alegre: Bookman, 2014.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788582601242)

* Este livro abrange uma ampla gama de tópicos em processamento de sinais, desde
fundamentos de análise espectral e transformadas de Fourier, até filtros
digitais, técnicas de modulação, equalização de canal, compressão de sinal e
processamento adaptativo. Além disso, o livro inclui exemplos práticos de
implementação de algoritmos.

**COMPUTAÇÃO**

* LAMBERT, K. A. Fundamentos de Python: estruturas de dados. 1. ed. São Paulo: Cengage Learning, 2022.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9786555584288)

* O autor apresenta as principais estruturas de dados em Python, incluindo
listas, tuplas, dicionários e conjuntos. O livro é muito útil para aqueles que
desejam compreender como essas estruturas funcionam em Python e como usá-las de
forma eficiente em diferentes situações de programação. Com muitos exemplos
práticos e exercícios, o livro é uma ferramenta valiosa para o aprendizado da
linguagem de programação  Python.

**MATEMÁTICA/FÍSICA**

* LATHI, B. P. Sinais e sistemas lineares. 2. ed. Porto Alegre: Bookman, 2008.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788577803910)

* Este o livro é uma fonte rica para estudantes de engenharia, pois seu conteúdo
apresenta de forma clara e didática conceitos fundamentais de sinais e sistemas
lineares, com o objetivo de trazer ferramentas matemáticas no domínio contínuo
e discreto para que os estudantes possam modelar e manipular sistemas de
controle clássicos e modernos.

**UX**

* MORAES, D. de. Metaprojeto: o design do design. São Paulo: Blucher, 2010.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788521216308)

* O metaprojeto, como observado neste livro, é uma alternativa posta ao design,
contrapondo os limites da metodologia convencional, ao se colocar como etapa
prévia de reflexão e suporte ao desenvolvimento do projeto em um cenário
mutante e complexo. Nesse sentido, o metaprojeto, enquanto metodologia da
complexidade, pode ser considerado o projeto do projeto, ou melhor, o design do
design.

**MATEMÁTICA/FÍSICA**

* NALON, J. A. Introdução ao processamento digital de sinais. Rio de Janeiro: LTC, 2009.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/books/978-85-216-2615-2)

* Este livro trata de conteúdo importante para estudantes de engenharia, pois
aborda tópicos importantes como séries de Fourier, transformadas de Fourier
entre outros, fundamentais em diversas áreas da engenharia, com explicações
claras e exemplos práticos. 

**COMPUTAÇÃO**

* PICHETTI, R. F.; JUNIOR, C. A. C.; ALVES, J. V. da S.; et al. Computação gráfica e processamento de imagens. Porto Alegre: SAGAH, 2022.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9786556903088)

* Os autores exploram os principais conceitos e técnicas em computação gráfica e
processamento de imagens, incluindo a teoria da cor, transformações
geométricas, filtragem e reconhecimento de padrões. Com exemplos práticos, o
livro é uma ferramenta para aprimorar as habilidades, com aplicações em jogos,
animação, design gráfico, visão computacional e processamento de imagens.

**COMPUTAÇÃO**

* RUSSELL, S. J.; NORVIG, P. Inteligência artificial: uma abordagem moderna. 4. ed. Rio de Janeiro: LTC, 2022.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788595159495)

* Este livro abrange tópicos como aprendizado de máquina, processamento de
linguagem natural e visão computacional, fornecendo uma visão abrangente e
prática, sendo uma referência essencial para os estudantes interessados em
explorar as aplicações modernas da IA.

**NEGÓCIOS**

* SCHIAVINI, J. M.; MARANGONI, E. Marketing digital e sustentável. Porto Alegre: SAGAH, 2019.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9786581739034)

* O crescimento do marketing digital gera implicações nas estratégias e conceitos
atuais de marketing. Esse livro aborda quais são os novos conceitos e
definições advindas do marketing digital e as novas tendências da área.

**COMPUTAÇÃO**

* SHAW, Z. A. Aprenda Python 3 do jeito certo: uma introdução muito simples ao incrível mundo dos computadores e da codificação. Rio de Janeiro: Alta Books, 2019.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788550809205)

* É um livro altamente recomendado para aqueles que desejam aprender Python de
forma prática e acessível. Com muitos exemplos e exercícios, o livro é voltado
para iniciantes e oferece uma base sólida em Python 3, cobrindo os principais
conceitos e recursos da linguagem. Além disso, o livro é atualizado
regularmente para refletir as mudanças mais recentes na linguagem Python.

**COMPUTAÇÃO**

* SILVA, F. M.; LEITE, M. C. D.; OLIVEIRA, D. B. Paradigmas de programação. Porto Alegre: SAGAH, 2019.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788533500426)

* O livro possui uma abordagem didática e clara, os autores exploram os
principais paradigmas de programação, incluindo programação funcional,
programação orientada a objetos e programação concorrente. O livro é
especialmente útil para aqueles que desejam compreender as diferenças entre
esses paradigmas e quando aplicá-los em diferentes situações de programação.

**COMPUTAÇÃO**

* SILVA, R. F. da. Deep Learning. São Paulo: Platos Soluções Educacionais S.A., 2021.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9786589881520)

* O livro aborda de forma clara e concisa os conceitos de redes neurais e deep
learning, que são essenciais para a construção de sistemas autônomos. Além
disso, o livro apresenta exemplos práticos e uma abordagem ética, o que é
fundamental em um campo em constante evolução e que tem grande impacto na
sociedade.

**LIDERANÇA**

* SORDI, J. O. Administração da informação: fundamentos e práticas para uma nova gestão do conhecimento. São Paulo: Saraiva, 2015.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788502634817)

* Considerando o contexto informacional atual, este livro descreve estratégias
práticas que as organizações utilizam para a gestão de seu conhecimento. 

**LIDERANÇA**

* TAJRA, S. F. Comunicação e negociação: conceitos e práticas organizacionais. São Paulo: Saraiva, 2014.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788536511054)

* Este livro tem como objetivo apresentar técnicas de comunicação que ajudam
lideranças a construírem acordos, estabelecerem uma cultura de respeito dentro
das organizações e a fomentar processos claros e alinhados aos objetivos dos
colaboradores e da organização.

**MATEMÁTICA/FÍSICA**

* ZILL, D. G. Matemática avançada para engenharia. 3. ed. Porto Alegre: Bookman, 2011. v. 1. 

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/books/9788577804771)

* Este livro é essencial para estudantes de engenharia, pois oferece uma visão
clara e concisa dos principais conceitos matemáticos necessários para a prática
da profissão. O volume 1 aborda Equações Diferenciais Ordinárias, Transformadas
de Laplace, entre outros tópicos, de forma didática e objetiva.

### 4.2. Bibliografia complementar

**COMPUTAÇÃO**

* BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788536530253)

* O livro aborda tópicos como tipos de dados, estruturas de controle, funções,
arquivos, módulos e muito mais. O livro é especialmente útil para aqueles que
desejam compreender a lógica da programação em Python e aplicá-la em projetos
práticos, como desenvolvimento web, científico, de jogos e automação de
tarefas.

**UX**

* BROWN, T. Design thinking: uma metodologia poderosa para decretar o fim das velhas ideias. Rio de Janeiro: Alta Books, 2020.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788550814377)

* Esta obra apresenta as emoções, a mentalidade e os métodos necessários para
elaborar o design de um produto a uma experiência ou estratégia, de modo
inovador. Este livro é um guia para líderes criativos que buscam propor o
design thinking em todas as facetas de suas organizações, produtos ou serviços
para descobrir novas alternativas para os negócios e para a sociedade como um
todo.

**NEGÓCIOS**

* CASAS, A. L. L. Marketing digital. 1. ed. Barueri: Atlas, 2022.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9786559771103)

* Livro de referência no estudo do Marketing brasileiro, apresenta novidades e
discute os mais modernos assuntos da área, como storytelling, economia de
compartilhamento, neuromarketing e content marketing.

**NEGÓCIOS**

* TURCHI, S. R. Estratégia de marketing digital e e-commerce. 2. ed. São Paulo: Atlas, 2018.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788597015409)

* A obra tem por objetivo apresentar, de forma acessível, uma visão abrangente
sobre as diversas estratégias de marketing digital e e-commerce, por meio da
exposição de artigos, ideias, pesquisas e também casos de grandes empresas,
multinacionais e pequenas e médias empresas.

**NEGÓCIOS**

* ZEITHAML, V. A.; PARASURAMAN, A. A excelência em serviços: como superar as expectativas e garantir a satisfação completa de seus clientes. 1. ed. São Paulo: Saraiva, 2014.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788502225572)

* Serviços de qualidade superior tem se revelado uma estratégia competitiva
vencedora e um maior desafio para as empresas Nessa obra os autores desenvolvem
uma ferramenta que permite mensurar de forma qualitativa e quantitativamente o
grau de satisfação dos clientes, considerando as cinco dimensões da qualidade
dos serviços: tangibilidade, confiabilidade, responsividade, segurança e
empatia.

**MATEMÁTICA/FÍSICA**

* CENGEL, Y. A. Equações diferenciais. Porto Alegre: AMGH, 2014.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/books/9788580553499)

* O livro é uma fonte fundamental para estudantes de engenharia, abordando de
forma clara e abrangente os principais tópicos e aplicações das equações
diferenciais. É uma ferramenta valiosa para compreender e resolver problemas
complexos em diversas áreas da matemática aplicada e engenharia.

**LIDERANÇA**

* COSTA, R. L. da; ANTÓNIO, N. S. Aprendizagem organizacional: ferramenta no processo de mudança. Coimbra: Conjuntura Actual, 2017. 

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9789896942601)

* A gestão do conhecimento depende de uma organização comprometida com o
aprendizado constante. Esta obra descreve esse processo apontando para os
diferenciais competitivos de uma boa estratégia de aprimoramento e mudança
organizacional. 

**COMPUTAÇÃO**

* DORF, R. C.; BISHOP, R. H. Sistemas de controle modernos. 13. ed. Rio de Janeiro: LTC, 2018.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788521635147)

* O livro Sistemas de Controle Modernos é uma leitura fundamental para estudantes
e profissionais de engenharia que desejam aprender sobre sistemas de controle.
Os autores exploram os principais conceitos e técnicas em sistemas de controle
modernos, incluindo sistemas de controle de malha aberta e fechada, controle
PID, projeto de controladores, análise de resposta transitória e estabilidade,
controle adaptativo e muito mais.

**COMPUTAÇÃO**

* FRIGERI, S. R.; JUNIOR, C. A. C.; ROMANINI, A. Computação gráfica. Porto Alegre: SAGAH: 2018.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788595026889)

* Os autores exploram as principais técnicas em computação gráfica, incluindo
modelagem geométrica, iluminação, shading, texturização e animação. Com
exemplos, o livro é uma ferramenta valiosa para quem busca aprimorar suas
habilidades em computação gráfica e aplicá-las em projetos práticos, como
desenvolvimento de jogos, simulações e animações.

**LIDERANÇA**

* LEWICKI, R. J.; SAUNDERS, D. M.; BARRY, B. Fundamentos de negociação. 5. ed. Porto Alegre: AMGH, 2014.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788580553864)

* O livro ensina estratégias para negociações complexas e difíceis, bem como
técnicas para lidar com diferentes tipos de negociadores, aborda as emoções e
os comportamentos envolvidos na negociação, fornecendo uma compreensão mais
profunda do processo de negociação.

**ORIENTAÇÃO**

* MARTIN, R. C. Desenvolvimento ágil limpo: de volta às origens. Rio de Janeiro: Alta Books, 2020. 

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788550816890)

* Esta obra traz uma revisão do manifesto ágil e a forma como ele é utilizado na
entrega de valor com o projeto. Ele traz uma visão do framework Scrum e outras
ferramentas ágeis do ponto de vista dos desenvolvedores, refletindo sua
experiência ao longo dos anos e como este manifesto foi revisitado.

**UX**

* MILANI, A. M. P. et al. Visualização de dados. 1. ed. Porto Alegre: SAGAH, 2020.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9786556900278)

* Este livro mostra diferentes formas de processamento, análise e apresentação de
dados para que o leitor esteja apto a utilizá-los da forma mais proveitosa
possível. Para tal, discute-se desde a história desse campo até as mais
modernas técnicas e abordagens que permitem a elaboração de visualizações de
dados claras, úteis e atualizadas.

**MATEMÁTICA/FÍSICA**

* ORSINI, L. Q. Curso de circuitos elétricos. 2. ed. São Paulo: Blucher, 2004. v. 2. 

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/books/9788521215264)

* O livro é uma ferramenta essencial para estudar séries e transformadas de
Fourier, oferecendo explicações claras e exemplos práticos. Sua abordagem
abrangente e sua segunda edição atualizada o tornam uma fonte valiosa para a
compreensão aprofundada desses tópicos fundamentais em circuitos elétricos.

**NEGÓCIOS**

* READE, D. V.; ROCHA, M.; OLIVEIRA, S. L. I. de; CHERNIOGLO, A. Marketing B2B. São Paulo: Saraiva, 2015.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/reader/books/978-85-02-63884-6)

* Este volume da coleção Marketing em Tempos Modernos é focado no mercado B2B e
na sua crescente globalização e complexidade. A obra aborda a importância do
bom relacionamento entre as empresas e seus clientes e fornecedores, pois tais
parcerias estratégicas permitem a criação de diferenciais competitivos,
fundamentais para o sucesso de toda a cadeia de suprimentos da qual essas
organizações fazem parte. 

**UX**

* SOBRAL, W. S. Design de interfaces: introdução. São Paulo: Saraiva, 2019.

* [Link para minha biblioteca](https://integrada.minhabiblioteca.com.br/#/books/9788536532073)

* Esta obra aborda o que são interfaces e sua evolução ao longo do tempo, até
chegarem à Interface Homem-Computador (IHC). Propõe o estudo das fases de um
projeto, incluindo métodos de construção e documentação. Discorre sobre as
estratégias de prototipagem adotadas no desenvolvimento do design e comenta a
lista de princípios para orientar o designer durante esse processo criativo.
