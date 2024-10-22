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
o encaixa de uma peça é *H7/p6* ou um *H9/d9*. De forma similar, um
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
continuar essa abstração para que seja cada vez mais fácil entregar soluções em
*software* cada vez mais complexas sem que aumente, em mesma proporção, a carga
cognitiva sobre o desenvolvedor ou time de desenvolvedores.

Agora que já estabelecemos o que são e para que servem os *design patterns*,
vamos estudar alguns deles. Mas veja, pois aqui também é particularmente útil
voltar ao nosso exercício mental que iniciou esta seção; se do engenheiro
mecânico não se espera que seja capaz de absorver e entender, em algumas poucas
horas, como implementar e quando usar cada um dos tipos de transmissão mecânica
existentes, também não é sensato imaginar que o projetista de *software* deve,
de uma só vez, aprender tudo sobre os padrões de abstração aqui descritos.
Sendo assim, o objetivo desta seção fica restrito a apresentar **três e apenas
três** dos *design patterns* mais úteis e que, sozinhos, provavelmente são o
suficiente para lidar com a esmagadora maioria dos projetos.

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

Embora o vídeo acima seja particularmente focado em implementações na linguagem
Python, os conceitos apresentados são partilhados entre todas as linguagens de
programação - em menor ou maior escala.

Quando um texto apresenta - em seus parágrafos, linhas e orações - uma clara
continuidade temática, sem que haja confusão entre os assuntos; ou seja, sem
que um assunto seja apresentado em um momento para que, sem cerimônia, seja
abandonado no decorrer do parágrafo para somente ser retomado ao final do
texto, mas sim apresentando e findando assuntos e temas de forma célere,
contida. Quando um texto é assim, dizemos que ele é um texto coeso. Não
precisamos ir muito longe dessa definição para entender o que significa *coesão
na programação*. Quando um sistema é construido de modo que cada classe,
subrotina, módulo ou arquivo apresenta um conceito, sem misturá-los sem motivo
aparente. Quando um sistema é feito com este cuidado, podemos dizer que existe
*coesão em sua implementação*.

O exemplo abaixo, apresentado também no vídeo do canal *ArjanCodes*, é um
recurso útil para entender como é um código com **baixa coesão**:

```python showLineNumbers title="codigo-baguncado.py"
def handle_stuff(d: Data, quantity: int, screen: int, screen:int, status: int, c: Color, ...):
    update_corporate_database(d, q, status)
    for i in range(0, quantity):
        profit[i] = revenue[i] - expense[i] * status
    new_color = c 
    status = SUCCESS 
    display_profits(screenX, screenY, status, d, c)
```

Note que o problema já se estabelece no proprio nome dado à função. Uma dica de
ouro para o leitor; **sempre escolha nomes de funções que remetem à ação nela
feita**. Caso isso não seja possível, considere a possibilidade da função estar
se ocupando de mais do que deveria. Neste caso, cabe refatorá-la, quebrando-a
em partes menores.

A seguir, podemos notar que uma mesma função se ocupa de quatro tipos de ações,
sem que haja aparente conexão entre elas. Esse tipo de organização não é e nem
deveria ser inexistente no mundo da programação. Muitas vezes nos encarregamos
de fazer códigos que sabemos que precisam ser concluídos com urgência e, após a
sua conclusão, não vão demandar mais qualquer tipo de manutenção. Aqui há outra
dica para os desenvolvedores; **não crie complexidade onde não há a necessidade
dela existir**.

A seguir, um exemplo de um código **coeso**:

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

A seguir, falaremos sobre o **acoplamento**. A definição encontrada para a
palavra acoplamento no dicionário *Oxford* pode ser vista a seguir:

> 1. união ou ligação entre dois ou mais corpos, formando um único conjunto.
> 2. conexão, compatibilização (de fatos, ações etc.).

Na programação, dizemos que um código apresenta *alto acoplamento* quando há -
entre as classes, módulos e subrotinas - uma dependência intrínseca, tal que
seja impossível modificar um sem, antes, ter que modificar um ou todos os
outros elementos. Um exemplo elucidativo pode ser visto abaixo:

Imagine que temos duas classes, uma para armazenar detalhes do usuário e outra
para gerenciar autenticação:

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

Uma maneira de reduzir o acoplamento é através da injeção de dependência. 
Em vez de a classe `Autenticacao` depender diretamente de `DetalhesUsuario`, 
podemos passar a dependência como um parâmetro:

```python showLineNumbers title="auth_injected.py"
class Autenticacao:
    def login(self, nome_usuario):
        if nome_usuario == "admin":
            return True
        return False
```

Agora, a classe `Autenticacao` não depende diretamente da estrutura de
`DetalhesUsuario`.

A esmagadora maioria dos *design patterns* visa reduzir o acoplamento e
aumentar a coesão dos sistemas de *software* desenvolvidos.

## 2. Strategy pattern

## 3. Strategy pattern

## 4. Strategy pattern
