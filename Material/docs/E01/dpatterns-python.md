---
title: Design Patterns em Python
sidebar_position: 2
sidebar_class_name: opcional
slug: /dpatterns-python
---
import SkillIssue from '@site/static/img/skill_issue.jpg';
import Gepetada from '@site/static/img/gepetada.jpg';

# Implementando design patterns em Python

:::note skill issue

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

Essa seção é composta apenas por exercícios para aprimorar suas habilidades.
Nenhuma seção de exercícios é obrigatória, mas escolher não fazer nenhuma é uma
ótima forma de criar um *skill issue* para você mesmo, no futuro.

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


## 1. Exercícios de Strategy

:::note Exercício 1

Você está desenvolvendo um sistema para calcular descontos em um e-commerce.
Existem diferentes estratégias de desconto, como:

1. **Desconto percentual** (por exemplo, 10% de desconto).
2. **Desconto fixo** (um valor fixo subtraído do total, por exemplo, R$ 50,00
   de desconto).
3. **Sem desconto** (nenhum desconto é aplicado).

Sua tarefa é implementar essas estratégias usando o **Strategy Pattern**. A
ideia é que o sistema seja flexível para mudar de estratégia de desconto
facilmente.

**Requisitos:**

1. Implemente uma classe `Pedido` que contenha o valor total do pedido.
2. Crie uma interface ou classe base chamada `DescontoStrategy` para as
   diferentes estratégias de desconto.
3. Implemente três estratégias de desconto concretas:
   - `DescontoPercentual` (aplica um desconto percentual).
   - `DescontoFixo` (aplica um desconto fixo).
   - `SemDesconto` (não aplica desconto).
4. O `Pedido` deve poder receber uma estratégia de desconto e calcular o valor
   final baseado nela.

**Exemplo de uso:**

```python
pedido = Pedido(500)  # Pedido de R$ 500,00
pedido.definir_desconto(DescontoPercentual(10))  # 10% de desconto
print(pedido.calcular_valor_final())  # Deveria imprimir 450.0

pedido.definir_desconto(DescontoFixo(50))  # R$ 50,00 de desconto
print(pedido.calcular_valor_final())  # Deveria imprimir 450.0

pedido.definir_desconto(SemDesconto())  # Sem desconto
print(pedido.calcular_valor_final())  # Deveria imprimir 500.0
```

**Instruções:**

1. Crie as classes necessárias para implementar essa estrutura.
2. Use o padrão Strategy para que seja fácil mudar a estratégia de desconto sem
   alterar a lógica do pedido.
3. Teste a aplicação de diferentes descontos no pedido.

**Dicas:**

- Lembre-se que o Strategy Pattern envolve encapsular uma família de algoritmos
  (neste caso, diferentes cálculos de desconto) e torná-los intercambiáveis.
- Sua classe `Pedido` deve aceitar diferentes estratégias de desconto sem
  precisar alterar seu código internamente.

:::

:::note Exercício 2

Você está desenvolvendo um sistema de recomendação de frete para uma loja
online. Dependendo de diferentes fatores, como peso do pacote, destino e
urgência da entrega, diferentes transportadoras são escolhidas. Sua tarefa é
implementar um sistema que use o **Strategy Pattern** para definir a estratégia
de seleção da transportadora de forma flexível.

**Requisitos:**

1. Crie uma classe `Pedido` que tenha as seguintes propriedades:
   - Peso do pacote (`peso`).
   - Destino (`destino`).
   - Urgência da entrega (`urgente`, booleano).
2. Implemente uma interface ou classe base `FreteStrategy`, que define um
   método `calcular_frete(pedido)` para calcular o custo de frete baseado nas
   características do pedido.
3. Implemente ao menos três estratégias concretas de cálculo de frete:
   - `FreteRapido`: Mais caro, mas com entrega rápida (aplica um custo
     adicional fixo para pedidos urgentes).
   - `FreteNormal`: Baseado apenas no peso e destino (desconsidera urgência).
   - `FreteEconomico`: Mais barato, mas com tempo de entrega maior (aplica
     desconto para pedidos não urgentes e com peso leve).
4. A classe `Pedido` deve receber a estratégia de frete e calcular o custo
   total de frete usando essa estratégia.

**Regras:**

- `FreteRapido`: Para pedidos urgentes, adicione uma taxa fixa de R$ 50,00 ao
  cálculo normal do frete (por peso e destino).
- `FreteNormal`: Baseie o custo de frete no peso do pacote e no destino (custo
  pode ser um valor base por quilograma + uma taxa por distância).
- `FreteEconomico`: Se o pedido não for urgente e o peso for menor que 2 kg,
  aplique um desconto de 30% no custo total do frete.

**Exemplo de uso:**

```python
pedido1 = Pedido(peso=5, destino='São Paulo', urgente=True)
pedido2 = Pedido(peso=1.5, destino='Rio de Janeiro', urgente=False)

pedido1.definir_frete(FreteRapido())
print(pedido1.calcular_custo_frete())  # Custo com frete rápido

pedido2.definir_frete(FreteEconomico())
print(pedido2.calcular_custo_frete())  # Custo com frete econômico

pedido1.definir_frete(FreteNormal())
print(pedido1.calcular_custo_frete())  # Custo com frete normal
```

**Instruções:**

1. Implemente as classes necessárias para representar as diferentes estratégias
   de frete.
2. O método `calcular_frete` de cada estratégia deve levar em consideração as
   propriedades do pedido (peso, destino e urgência).
3. A classe `Pedido` deve ser capaz de trocar de estratégia dinamicamente e
   recalcular o frete.

**Desafios Extras:**

- Para simular destinos diferentes, você pode definir uma tabela de distâncias
  (ou usar uma função simples que retorna uma distância baseada no destino).
- Tente aplicar alguma validação para garantir que o peso e o destino sejam
  válidos antes de calcular o frete.
- Pense em como escalonar essa lógica no futuro, caso você precise adicionar
  novas transportadoras com suas próprias regras.

**Dicas:**

- O foco aqui é no uso do Strategy Pattern para trocar as regras de cálculo de
  frete sem alterar a estrutura do `Pedido`.
- Considere como a separação das estratégias torna o código mais flexível e
  fácil de manter, caso você queira adicionar ou modificar as regras de cálculo
  no futuro.

:::

:::note Exercício 3

Você foi contratado para desenvolver um sistema de **gestão de investimentos**
que permita aos clientes aplicar seu capital em diferentes estratégias de
investimento. Cada estratégia tem suas próprias regras para calcular os
retornos com base em fatores como o valor investido, o nível de risco e a
performance do mercado.

Sua tarefa é usar o **Strategy Pattern** para implementar várias estratégias de
investimento e permitir que o cliente escolha a estratégia mais adequada para
seus objetivos.

**Requisitos:**

1. Crie uma classe `Investimento` que tenha as seguintes propriedades:
   - Valor investido (`valor_investido`).
   - Nível de risco (`risco`, que pode ser baixo, médio ou alto).
   - Performance do mercado (`performance`, que será um valor percentual, por
     exemplo, +5% ou -3%).

2. Implemente uma interface ou classe base `EstrategiaInvestimento` com um
   método `calcular_retorno(investimento)` que calcula o retorno do
   investimento com base nas regras da estratégia.

3. Implemente pelo menos três estratégias de investimento concretas:
   - **EstrategiaConservadora**: Investimentos de baixo risco, que garantem um
     retorno mínimo, mas com ganhos limitados. Se a performance do mercado for
     negativa, o retorno é neutro.
   - **EstrategiaModerada**: Combina uma análise de risco e performance do
     mercado. Oferece maior retorno em mercados positivos, mas ainda protege
     parte do valor investido em mercados negativos.
   - **EstrategiaAgressiva**: Oferece altos retornos em mercados positivos, mas
     também pode resultar em grandes perdas se o mercado estiver negativo,
     dependendo do risco assumido.

4. O cliente deve ser capaz de trocar a estratégia de investimento
   dinamicamente e recalcular o retorno esperado.

**Detalhes de cada estratégia:**

- **EstrategiaConservadora**:
  - Retorno mínimo de 2% se o mercado for neutro ou positivo.
  - Se a performance do mercado for negativa, o retorno é 0%.

- **EstrategiaModerada**:
  - Para performance de mercado positiva, o retorno é a performance
    multiplicada por um fator de 1,5.
  - Para performance negativa, o cliente perde apenas 50% da performance
    negativa (por exemplo, se o mercado cair -6%, a perda será -3%).

- **EstrategiaAgressiva**:
  - Retorno total baseado na performance do mercado.
  - Se o mercado subir, o retorno é amplificado em 2x. Se o mercado cair, a perda é total, sem mitigação.

**Exemplo de uso:**

```python
# Investimento inicial de R$ 10.000,00, com risco médio e performance do
mercado +5%
investimento = Investimento(valor_investido=10000, risco='médio',
performance=5)

investimento.definir_estrategia(EstrategiaConservadora())
print(investimento.calcular_retorno())  # Deveria imprimir o retorno com a
estratégia conservadora

investimento.definir_estrategia(EstrategiaModerada())
print(investimento.calcular_retorno())  # Deveria imprimir o retorno com a
estratégia moderada

investimento.definir_estrategia(EstrategiaAgressiva())
print(investimento.calcular_retorno())  # Deveria imprimir o retorno com a
estratégia agressiva
```

**Instruções:**

1. Implemente a classe `Investimento` que aceite a estratégia de investimento e permita calcular o retorno esperado.
2. Implemente as estratégias mencionadas, cada uma com suas regras específicas
   para calcular o retorno.
3. Certifique-se de que o cliente pode trocar de estratégia sem precisar
   modificar a lógica interna do investimento.

**Desafios Extras:**

- Implemente uma lógica para considerar o risco do cliente de forma mais
  elaborada. Por exemplo, em estratégias agressivas, o retorno pode ser ainda
  mais alto para investidores com maior apetite ao risco.
- Adicione mais estratégias de investimento com regras mais complexas, como uma
  estratégia que ajusta automaticamente o nível de risco com base na
  performance do mercado.

**Reflexão:**

- Como o uso do Strategy Pattern ajuda a manter o código flexível e adaptável a
  novas estratégias?
- Pense na extensibilidade do sistema. Como você pode adicionar novas
  estratégias sem modificar o código existente?

:::

## 2. Exercícios de Observer

:::note Exercício 4

Você está desenvolvendo um sistema simples de notificações para um aplicativo
de clima. O aplicativo permite que usuários se inscrevam para receber alertas
sempre que a previsão de temperatura mudar. Cada usuário pode ser notificado de
maneira diferente, por exemplo, por **e-mail** ou **SMS**.

Sua tarefa é implementar o **Observer Pattern** para esse sistema, onde:

1. Uma classe `EstacaoMeteorologica` será responsável por manter a temperatura
   atual e notificar os usuários registrados sempre que houver uma mudança de
   temperatura.
2. Diferentes observadores (os usuários) poderão se inscrever e ser notificados
   de acordo com suas preferências.

**Requisitos:**

1. Crie a classe `EstacaoMeteorologica`, que será o **sujeito** (subject), com
   os seguintes métodos:
   - `adicionar_observador(observador)`: Para adicionar um novo observador.
   - `remover_observador(observador)`: Para remover um observador.
   - `notificar_observadores()`: Para notificar todos os observadores sobre uma
     mudança na temperatura.
   - Um método `alterar_temperatura(nova_temperatura)` que atualiza a
     temperatura e chama o método `notificar_observadores`.

2. Crie uma interface ou classe base `Observador` que defina o método
   `atualizar(temperatura)` para os observadores.

3. Implemente dois tipos de observadores concretos:
   - **ObservadorEmail**: Notifica os usuários por e-mail.
   - **ObservadorSMS**: Notifica os usuários via SMS.

4. Cada observador deve ser notificado com a nova temperatura quando esta for
   alterada.

**Exemplo de uso:**

```python
# Criação da estação meteorológica
estacao = EstacaoMeteorologica()

# Observadores se inscrevem para receber notificações
observador_email = ObservadorEmail("user@example.com")
observador_sms = ObservadorSMS("+5511999999999")

estacao.adicionar_observador(observador_email)
estacao.adicionar_observador(observador_sms)

# Alteração de temperatura
estacao.alterar_temperatura(25)  # Notifica todos os observadores com a nova
temperatura

# Um observador pode ser removido
estacao.remover_observador(observador_sms)

# Nova alteração de temperatura
estacao.alterar_temperatura(30)  # Apenas o observador de e-mail será
notificado
```

**Instruções:**

1. Implemente a classe `EstacaoMeteorologica` com a capacidade de adicionar,
   remover e notificar observadores.
2. Crie a classe base `Observador` com o método `atualizar(temperatura)`.
3. Implemente os observadores concretos, como `ObservadorEmail` e
   `ObservadorSMS`.
4. Teste o sistema alterando a temperatura e verificando se os observadores são
   notificados corretamente.

**Dicas:**

- O padrão **Observer** é útil quando você quer garantir que várias classes
  dependentes sejam notificadas automaticamente sempre que houver uma mudança
  de estado no "sujeito".
- Para implementar o `notificar_observadores`, faça um loop sobre todos os
  observadores registrados e chame o método `atualizar` para cada um.

:::

:::note Exercício 5

Você está desenvolvendo um sistema de **monitoramento de ações** para uma
corretora. O sistema monitora várias empresas e notifica diferentes
investidores sempre que o preço de uma ação muda. Cada investidor pode estar
interessado em uma ou mais empresas, e o sistema deve ser capaz de enviar
notificações apenas sobre as ações que o investidor escolheu acompanhar.

Sua tarefa é implementar o **Observer Pattern**, onde:

1. A classe `BolsaDeValores` monitora os preços das ações e notifica os
   investidores interessados quando há uma mudança.
2. Cada investidor pode se inscrever para monitorar uma ou mais ações de
   diferentes empresas e deve ser notificado apenas sobre as ações que ele está
   acompanhando.

**Requisitos:**

1. Crie a classe `BolsaDeValores`, que será o **sujeito** (subject), com os
   seguintes métodos:
   - `adicionar_observador(empresa, observador)`: Adiciona um observador para
     uma empresa específica.
   - `remover_observador(empresa, observador)`: Remove um observador de uma
     empresa.
   - `notificar_observadores(empresa)`: Notifica todos os observadores registrados para uma empresa específica quando o preço da ação mudar.
   - Um método `alterar_preco(empresa, novo_preco)` que atualiza o preço de uma
     ação e chama o método `notificar_observadores`.

2. Crie uma interface ou classe base `Investidor`, que define o método
   `atualizar(empresa, preco)` para os observadores.

3. Implemente a classe concreta `InvestidorConcreto`, que representa um
   investidor que será notificado sobre mudanças nos preços das ações das
   empresas que ele está acompanhando.

**Exemplo de uso:**

```python
# Criação da bolsa de valores
bolsa = BolsaDeValores()

# Investidores
investidor_1 = InvestidorConcreto("Investidor 1")
investidor_2 = InvestidorConcreto("Investidor 2")

# Investidores se inscrevem para acompanhar diferentes empresas
bolsa.adicionar_observador("Apple", investidor_1)
bolsa.adicionar_observador("Google", investidor_1)
bolsa.adicionar_observador("Google", investidor_2)

# Alteração de preço para as ações da Apple e Google
bolsa.alterar_preco("Apple", 150)  # Apenas Investidor 1 será notificado
bolsa.alterar_preco("Google", 200)  # Ambos os investidores serão notificados

# Investidor 1 para de acompanhar Google
bolsa.remover_observador("Google", investidor_1)

# Nova alteração de preço para Google
bolsa.alterar_preco("Google", 210)  # Apenas Investidor 2 será notificado
```

**Instruções:**

1. Implemente a classe `BolsaDeValores` com a capacidade de gerenciar
   observadores para diferentes empresas.
2. Crie a classe base `Investidor` com o método `atualizar(empresa, preco)`.
3. Implemente a classe `InvestidorConcreto`, que armazena o nome do investidor
   e recebe as notificações de mudança de preço das ações que ele está
   acompanhando.
4. Teste o sistema alterando os preços das ações de diferentes empresas e
   verificando se apenas os investidores interessados são notificados.

**Regras adicionais:**

- Um investidor pode acompanhar várias empresas, mas só receberá notificações
  sobre as empresas que escolheu acompanhar.
- Quando o preço de uma ação é alterado, o sistema deve notificar todos os
  observadores inscritos para aquela empresa, mas não para as outras.
- Pense em como lidar com a remoção de observadores de forma eficiente.

**Dicas:**

- Para a classe `BolsaDeValores`, você pode usar um dicionário onde a chave é o
  nome da empresa e o valor é uma lista de observadores inscritos para aquela
  empresa.
- O **Observer Pattern** permite que os observadores sejam desacoplados do
  objeto que os notifica, tornando o sistema mais flexível para futuras
  mudanças.

:::

## 3. Exercícios de Factory

:::note Exercício 6

Você deve criar uma classe **`ShapeFactory`** que seja responsável por criar
diferentes tipos de formas geométricas: **Círculo** e **Quadrado**. Cada forma
terá um método `draw()` que exibirá uma mensagem indicando que a forma foi
desenhada.

**Requisitos:**
1. Crie uma classe abstrata **`Shape`** que tenha um método abstrato `draw()`.
2. Crie duas classes concretas, **`Circle`** e **`Square`**, que herdem de
   `Shape` e implementem o método `draw()`.  
   - O método `draw()` de `Circle` deve imprimir `"Desenhando um círculo"`.
   - O método `draw()` de `Square` deve imprimir `"Desenhando um quadrado"`.
3. Implemente a classe **`ShapeFactory`** que possui um método estático
   **`get_shape(shape_type)`**:
   - Se `shape_type` for `"circle"`, ele deve retornar uma instância de
     `Circle`.
   - Se `shape_type` for `"square"`, ele deve retornar uma instância de
     `Square`.
   - Se `shape_type` for inválido, retorne `None`.
4. No programa principal, use a fábrica para criar uma forma com base em uma entrada do usuário e chame o método `draw()` da forma retornada.

**Exemplo de uso:**
```python
forma = ShapeFactory.get_shape("circle")
forma.draw()  # Deve exibir: "Desenhando um círculo"

forma = ShapeFactory.get_shape("square")
forma.draw()  # Deve exibir: "Desenhando um quadrado"
```

**Dicas:**
- Utilize o módulo `abc` para criar a classe abstrata.
- Verifique o tipo de forma passado no método `get_shape`.

Esse exercício é bom para entender como o **Factory Pattern** funciona e como
ele pode ser usado para instanciar diferentes objetos sem expor a lógica de
criação ao cliente.

:::

:::note Exercício 7

Você foi contratado para desenvolver um sistema de pagamento online que suporta
diferentes métodos de pagamento: **Cartão de Crédito**, **PayPal**, e
**Bitcoin**. Cada método de pagamento tem suas particularidades, mas todos
devem fornecer uma interface comum para processar o pagamento.

Neste exercício, você vai usar o **Factory Pattern** para criar instâncias de diferentes estratégias de pagamento e o **Strategy Pattern** para encapsular a lógica específica de cada método de pagamento.

**Requisitos:**

1. **Interface de Pagamento**: Crie uma interface (ou classe abstrata)
   `PaymentStrategy` com o método `process_payment(amount)` que será
   implementado por cada estratégia de pagamento.
   
2. **Estratégias de Pagamento**:
   - `CreditCardPayment`: Implementa a estratégia para pagamento com cartão de
     crédito.
   - `PaypalPayment`: Implementa a estratégia para pagamento via PayPal.
   - `BitcoinPayment`: Implementa a estratégia para pagamento com Bitcoin.
   
3. **Factory de Pagamentos**: Implemente uma fábrica `PaymentFactory` que, dado
   um tipo de pagamento (ex: "credit", "paypal", "bitcoin"), retorne a
   instância apropriada da estratégia de pagamento.

4. **Processo de Pagamento**: Crie uma classe `PaymentProcessor` que usa a
   **Factory** para obter a estratégia de pagamento e depois processa o
   pagamento com base no valor fornecido.

**Detalhes adicionais:**
- Cada estratégia deve simular o processamento, exibindo mensagens como
  "Processando pagamento de X via Cartão de Crédito", etc.
- Se o tipo de pagamento for desconhecido, a fábrica deve lançar uma exceção.

**Exemplo de uso esperado:**

```python
processor = PaymentProcessor()
processor.process("credit", 100)
processor.process("paypal", 200)
processor.process("bitcoin", 300)
```

Saída esperada:

```
Processando pagamento de 100 via Cartão de Crédito
Processando pagamento de 200 via PayPal
Processando pagamento de 300 via Bitcoin
```

**Passos para guiar sua solução:**

1. Comece criando a interface `PaymentStrategy`.
2. Implemente as classes de pagamento específicas que seguem essa interface.
3. Crie a `PaymentFactory` para instanciar as estratégias baseadas em um identificador.
4. Implemente a classe `PaymentProcessor` que usa a fábrica para processar os
   pagamentos.

:::
