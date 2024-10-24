---
title: Design Patterns
sidebar_position: 1
sidebar_class_name: autoestudo
slug: /dpatterns
---

# Design Patterns

<img 
  src="https://nikku1234.github.io/img/software_design/gof.png"
  alt="Gang of four patterns." 
  style={{ 
    display: 'block',
    marginLeft: 'auto',
    maxHeight: '40vh',
    marginRight: 'auto'
  }} 
/>
<br/>

Em uma cozinha profissional, espera-se dos cozinheiros e demais
auxiliares que sejam capazes de entender o que significa um corte
*julienne* ou mesmo conhecer a diferença entre um *brunoise* e um
*mirepoix*. Espera-se, de um bom torneiro, que seja capaz de mudar
sua estratégia de acabamento superficial levando em consideração se
o encaixe de uma peça é *H7/p6* ou um *H9/d9*. De forma similar, um
projetista mecânico que se preze deve dominar os diferentes tipos de
transmissão mecânica; seja ela por correia, por pares engrenados ou mesmo um
mecanismo came seguidor. Por quê, então, deveria ser diferente com o
profissional incumbido de arquitetar e desenvolver soluções em *software*? Por
quê deveria este, e não os outros, relegar-se apenas ao uso da lógica pura,
reinventando a roda a cada novo projeto? Se a sua resposta a esse
questionamento é de que não deveria, então você já está convencido sobre a
utilidade de *design patterns*.

Segue que um *strategy pattern* ou um *observer pattern* nada mais é do que o
*brunoise* ou o *mirepoix* do engenheiro de software; isto é, são **padrões que
se repetem com frequência** e, portanto, são muito úteis de se memorizar.
Padrões de quê, exatamente? De abstração de código. A importância disso é
fundamental para a arquitetura de *software* e não deve ser menosprezada. Pois
se o código com o qual interagimos nada mais é do que fruto de uma abstração
útil de 1's e 0's, que é a linguagem natural dos computadores, então é razoável
expandir essa abstração para que seja cada vez mais fácil entregar soluções em
*software* cada vez mais complexas sem que aumente, em mesma proporção, a carga
cognitiva sobre o desenvolvedor ou time de desenvolvedores.

A engenharia de software costuma induzir um tipo de comportamento peculiar
entre aqueles que se ocupam a estudá-la. Não é nada incomum encontrar ídolos de
ferramentas ou métodos que, criando uma cruzada quixotesca, empurra ao paganismo
todos aqueles que ousam questionar os dogmas da sua religião. É justamente
pensando nessa curiosa ocorrência que logo faço questão de desmistificar
qualquer aura que paire nos arredores dos tais dos *design
patterns*, pois eles são **só padrões de construção** - criados no decorrer das
décadas em que a computação engatinhava e os engenheiros, a duras custas,
percebiam as dificuldades envolvidas em ampliar o escopo de projetos de
*software* -, padrões esses que receberam esse nome apenas na década de 90,
quando quatro autores - hoje conhecidos como *gang of four* - resolveram
categorizar e dar nomes àquelas que antes eram técnicas escondidas, que
brotavam espontâneamente na mente de desenvolvedores com algumas cicatrizes de
guerra.

Nessa busca por sintetizar essas técnicas, os quatro veteranos elencaram **23
padrões**, dividindo-os em **três tipos de padrões**:

* Os padrões **comportamentais**, que descrevem maneiras de se
  isolar responsabilidades entre objetos e criar, entre eles, meios de
  comunicação que minimizem a necessidade de refatorar o código.
* Os padrões **criacionais** são aqueles que ditam métodos de criação de
  objetos que vão além da cansada e perigosa alocação dinâmica crua.
* Por fim, os padrões **estruturais** descrevem maneiras de se compor
  estruturas complexas utilizando objetos mais simples, aglutinando-os para
  manter pedaços de código que individualmente são simples de implementar e
  consertar, mas que juntos são capazes de implementar as mais convolutas
  regras de negócio.

Note a palavra chave para cada uma dessas categorias: **objeto**. Sim, os
primeiros *design patterns* são exclusivamente focados no paradigma de
orientação a objetos. Então não, caro *rustacean* ou *gopher*, você não pode só
buscar um dos padrões descritos pela *gang of four* e aplicar em suas tenras
linguagens. Perceba, não obstante, que um padrão de construção é só isso; um
padrão. Novos padrões surgem quando as ferramentas evoluem. Busque saber quais
são os padrões comuns para os seus utensílios favoritos.

Esta seção seria de pouca utilidade se apenas delineássemos o que é e para que
servem os tais *design patterns*, então a seguir vamos estudar alguns deles de
forma que seja relativamente simples implementá-los em seguida. Mas veja, pois
aqui também é particularmente útil voltar ao nosso exercício mental que iniciou
esta seção; se do engenheiro mecânico não se espera que seja capaz de absorver
e entender, em algumas poucas horas, como implementar e quando usar cada um dos
tipos de transmissão mecânica existentes, também não é sensato imaginar que o
projetista de *software* deve, de uma só vez, aprender tudo sobre os padrões de
abstração aqui descritos. Sendo assim, o objetivo desta seção fica restrito a
apresentar **três e apenas três** dos *design patterns* mais úteis e que,
sozinhos, provavelmente são o suficiente para lidar com a esmagadora maioria
dos projetos para um desenvolvedor iniciante.

Entenda, portanto, que esta é apenas uma introdução ao assunto e, assim como o
torneiro que passa a entender como se comunicar com o projetista mecânico, deve
partir de você desbravar e conhecer mais padrões, de modo que o seu vocabulário
se enriqueça gradativamente.

Quais são os *design patterns* que vamos estudar?

* *Strategy pattern*;
* *Observer pattern*; e
* *Factory pattern*.

Antes disso, no entanto, vamos definir alguns conceitos a partir dos quais é
possível descrever os benefícios em particular do uso da maioria dos *design
patterns*. Esses são os conceitos de **coesão** e **acoplamento**.

## 1. Coesão e acoplamento

:::info autoestudo obrigatório

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/eiDyK_ofPPM" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

:::

Embora o vídeo acima tenha sido feito para abordá-los com o viés *pythonista*,
os conceitos apresentados são partilhados entre todas as linguagens de
programação - em menor ou maior escala.

Quando um texto apresenta - em seus parágrafos, linhas e orações - uma clara
continuidade temática, sem que haja confusão entre os assuntos; ou seja, sem
que um assunto seja apresentado em um momento para que, sem cerimônia, seja
abandonado no decorrer do parágrafo para somente ser retomado em outro momento,
mas sim apresentando e findando assuntos e temas de forma contida. Quando um
texto é assim, dizemos que ele é um texto coeso. Não precisamos ir muito longe
dessa definição para entender o que significa *coesão na programação*. Quando
um sistema é construido de modo que cada classe, subrotina, módulo ou arquivo
apresenta um conceito, sem misturá-los sem motivo aparente. Quando um sistema é
feito com este cuidado, podemos dizer que existe *coesão em sua implementação*.

O exemplo abaixo, apresentado também no vídeo do canal *ArjanCodes*, é um
exemplo de código com *baixa coesão*. Embora essa seção seja agnóstica a
linguagem, o Python é útil para este tipo de exemplo por sua semelhança com
*pseudolingaugens*.

```python showLineNumbers title="codigo-baguncado.py"
def handle_stuff(d: Data, quantity: int, screen: int, screen:int, status: int, c: Color, ...):
    update_corporate_database(d, q, status)
    for i in range(0, quantity):
        profit[i] = revenue[i] - expense[i] * status
    new_color = c 
    status = SUCCESS 
    display_profits(screenX, screenY, status, d, c)
```

Um código com baixa coesão geralmente causa confusão, como o código acima
provavelmente causou em você ao lê-lo pela primeira vez. Os nomes não são
elucidativos, os conceitos se misturam e uma função se ocupa de muitas coisas
ao mesmo tempo. Segue aqui uma dica para o leitor;**sempre escolha nomes de
funções que remetem à ação nela feita**. Caso isso não seja possível, considere
a possibilidade da função estar se ocupando de mais do que deveria. Neste caso,
cabe refatorá-la, quebrando-a em partes menores.

Uma pergunta que cabe aqui é como podemos melhorar esse código, certo? Pois
vamos conversar um pouco, já que essa é uma pergunta que pode, aos poucos,
fazer florescer um dos pecados pouco perdoados em iniciantes; **nem sempre o
que está mal feito precisa ser refeito**. Quê? É isso mesmo que você leu.
**Seja pragmático**. Existem momentos em que a *arte* de programar não se
discerne muito do ato de defecar, que transforma em rei aquele que sabe atender
os chamados da natureza sem morosidade e, em sua coroação, recebe o prazer que
só o fim de um desconforto visceral consegue nos presentear. Usando um exemplo
um tanto menos escatológico: nem todo projeto precisa ser a *Capela Sistina*.

É com esse espírito leve, capaz de deixar para trás aquilo que é *legado*, que
apresento um novo código, esse como um exemplo de **coesão**:

```python title="calculadora.py" showLineNumbers
class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b
```

* Nomes suficientemente elucidativos - *check*;
* Métodos com nomes que aludem à sua função - *check*;
* Unidades de código que se ocupam de apenas uma coisa, sem misturar
  preocupações - *check*;

Acho que podemos seguir em frente, para o conceito de **acoplamento**. O
dicionário de *Oxford* define acoplamento como:

> 1. união ou ligação entre dois ou mais corpos, formando um único conjunto.
> 2. conexão, compatibilização (de fatos, ações etc.).

Na programação, dizemos que um código apresenta *alto acoplamento* quando há -
entre as classes, módulos e subrotinas - uma dependência intrínseca, tal que
seja impossível modificar um sem, antes, ter que modificar um ou todos os
outros elementos.

Como um exemplo de código com **alto acoplamento**, imagine que temos duas
classes, uma para armazenar detalhes do usuário e outra para gerenciar
autenticação:

```python showLineNumbers title="auth.py"
class DetalhesUsuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Autenticacao:
    def login(self, usuario):
        if usuario.nome == "admin":
            return True
        return False
```

Se, no futuro, a estrutura ou os métodos da classe `DetalhesUsuario` forem
alterados, pode haver um impacto direto na classe `Autenticacao`, pois ela está
acoplada à classe `DetalhesUsuario` através do uso direto do atributo `nome`.

As maneiras de se reduzir o acoplamento não são imediatamente obvias. De fato,
a maioria dos *design patterns comportamentais* tem como principal objetivo a
**diminuição do grau de acoplamento no código**. Uma outra consequência dos uso
dos *design patterns* é um **aumento da coesão do código**.

A seguir, vamos estudar mais sobre o *strategy pattern*.

## 2. Strategy pattern

:::info autoestudo obrigatório

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/WQ8bNdxREHU" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

:::

O *strategy pattern* (padrão de estratégia) é um padrão de projeto
comportamental que permite definir uma família de algoritmos, encapsulá-los e
torná-los intercambiáveis. Isso significa que você pode alterar o comportamento
de um objeto sem alterar seu código-fonte, simplesmente mudando a estratégia
que ele utiliza.

Imagine que você está dirigindo em uma estrada desconhecida, e o seu GPS
oferece diferentes rotas para chegar ao destino: a mais rápida, a mais curta,
ou a que evita pedágios. Embora o destino seja o mesmo, a estratégia para
chegar lá pode variar de acordo com a sua preferência. No mundo da programação,
o *strategy pattern* funciona de maneira similar: ele permite que você escolha,
em tempo de execução, qual algoritmo ou método utilizar para resolver um
problema específico.

Abaixo, podemos ver um exemplo de implementação de um starategy pattern em
*Python*. O exemplo apresenta um sistema de e-commerce que precisa calcular
descontos em compras. Existem diferentes estratégias de desconto, como desconto
por fidelidade, desconto sazonal, ou desconto por quantidade comprada. Queremos
aplicar diferentes estratégias de desconto sem precisar modificar o código
principal da nossa classe de cálculo.

```python title="descontos.py" showLineNumbers
from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoFidelidade(EstrategiaDesconto):
    def calcular(self, valor):
        return valor * 0.9  # 10% de desconto

class DescontoSazonal(EstrategiaDesconto):
    def calcular(self, valor):
        return valor * 0.8  # 20% de desconto

class DescontoQuantidade(EstrategiaDesconto):
    def calcular(self, valor):
        return valor * 0.85  # 15% de desconto

class CarrinhoDeCompras:
    def __init__(self, estrategia: EstrategiaDesconto):
        self.estrategia = estrategia
        self.itens = []

    def adicionar_item(self, valor):
        self.itens.append(valor)

    def calcular_total(self):
        total = sum(self.itens)
        return self.estrategia.calcular(total)

# Uso:
if __name__ == "__main__":
    carrinho = CarrinhoDeCompras(DescontoFidelidade())
    carrinho.adicionar_item(100)
    carrinho.adicionar_item(200)
    print(f"Total com desconto de fidelidade: {carrinho.calcular_total()}")  # Saída: 270.0

    carrinho = CarrinhoDeCompras(DescontoSazonal())
    carrinho.adicionar_item(100)
    carrinho.adicionar_item(200)
    print(f"Total com desconto sazonal: {carrinho.calcular_total()}")  # Saída: 240.0
```

No exemplo acima, temos uma interface `EstrategiaDesconto` que define o método
`calcular`. As classes `DescontoFidelidade`, `DescontoSazonal` e
`DescontoQuantidade` implementam essa interface, fornecendo diferentes
estratégias de cálculo de desconto. A classe `CarrinhoDeCompras` recebe uma
estratégia de desconto no seu construtor, permitindo que o comportamento de
cálculo seja alterado dinamicamente.

## 3. Observer pattern

:::info autoestudo obrigatório

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/oNalXg67XEE" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

:::

O *observer pattern* (padrão de observador) é um padrão de projeto
comportamental que estabelece uma dependência um-para-muitos entre objetos, de
maneira que quando um objeto muda de estado, todos os seus dependentes são
notificados e atualizados automaticamente.

Se hoje, quando chegar em casa, você sentar no conforto de sua cadeira *gamer*
e receber uma notificação de que um dos criadores de conteúdo que você segue
tem um novo vídeo a disposição, saiba que isso é um exemplo prático do padrão
*observer* em funcionamento. Outro bom exemplo é o robô com nome de tartaruga
que torturou seus sonhos há alguns meses e espera, ansioso, para reencontrá-lo
em breve. Ao utilizar o ROS você - entre uma espraguejada e outra - deve ter
trabalhado com *subscribers* e *publishers*.

No exemplo abaixo, apresenta-se um sistema de publicações onde usuários podem
se inscrever para receber notificações quando novos artigos são publicados.

```python title="publicacoes.py" showLineNumbers
from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, artigo):
        pass

class Usuario(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, artigo):
        print(f"{self.nome} foi notificado sobre um novo artigo: {artigo.titulo}")

class Artigo:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

class Publicador:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador: Observador):
        self.observadores.append(observador)

    def remover_observador(self, observador: Observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, artigo):
        for observador in self.observadores:
            observador.atualizar(artigo)

    def publicar_artigo(self, titulo, conteudo):
        artigo = Artigo(titulo, conteudo)
        self.notificar_observadores(artigo)

# Uso:
if __name__ == "__main__":
    publicador = Publicador()

    usuario1 = Usuario("Alice")
    usuario2 = Usuario("Bob")
    usuario3 = Usuario("Carlos")

    publicador.adicionar_observador(usuario1)
    publicador.adicionar_observador(usuario2)

    publicador.publicar_artigo("Design Patterns em Python", "Conteúdo do artigo...")

    # Saída:
    # Alice foi notificado sobre um novo artigo: Design Patterns em Python
    # Bob foi notificado sobre um novo artigo: Design Patterns em Python

    publicador.remover_observador(usuario1)
    publicador.adicionar_observador(usuario3)

    publicador.publicar_artigo("Observer Pattern", "Conteúdo do artigo...")

    # Saída:
    # Bob foi notificado sobre um novo artigo: Observer Pattern
    # Carlos foi notificado sobre um novo artigo: Observer Pattern
```

## 4. Factory pattern

:::info autoestudo obrigatório

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/s_4ZrtQs8Do" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

:::

O *factory pattern* (padrão de fábrica) é um padrão de projeto criacional que
fornece uma interface para criar objetos em uma superclasse, mas permite que
subclasses alterem o tipo de objetos que serão criados. Ele encapsula a lógica
de criação de objetos, promovendo o desacoplamento do código.

Imagine entrar em uma sorveteria e pedir um sorvete. Você não se preocupa em
como o sorvete é feito; apenas escolhe o sabor e aguarda o atendente lhe
entregar a delícia gelada. Nos bastidores, a sorveteria tem todo um processo
para criar o sorvete conforme o seu pedido. Na programação, o *factory pattern*
atua como essa sorveteria: ele abstrai a criação de objetos, permitindo que
você solicite o que precisa sem se preocupar com os detalhes de construção.
