---
title: Nós e Tópicos
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/opcional.png').default} width='35vw'/> Entendendo nós e tópicos

O sistema ROS 2 (Robot Operating System) é composto por uma série de conceitos
fundamentais que, juntos, formam a estrutura de grafo do ROS (2). Este
grafo é uma rede de elementos ROS 2 que processam dados simultaneamente. Se
fossemos visualizar este grafo, ele englobaria todos os executáveis e as
conexões entre eles.

## 1. Nós 

![](/gifs/nos.gif)

[fonte](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

Um "nó" é um dos principais elementos do ROS 2. Cada nó deve ser responsável por
uma única função modular. Por exemplo, um nó pode ser responsável por controlar
os motores das rodas ou por publicar dados de sensores, como um laser
range-finder. Os nós podem enviar e receber dados de outros nós através de
tópicos, serviços, ações ou parâmetros. Um sistema robótico completo é composto
por muitos nós trabalhando em conjunto. Em ROS 2, um único executável (programa
C++, programa Python, etc.) pode conter um ou mais nós.

### 1.1. Interagindo com Nós
Existem várias ferramentas que permitem interagir com os nós em ROS 2:

1. **ros2 run**: Este comando lança um executável de um pacote. Por exemplo,
para executar o "turtlesim", você usaria o comando `ros2 run turtlesim
turtlesim_node`.

2. **ros2 node list**: Este comando mostra os nomes de todos os nós em execução.
É útil quando você quer interagir com um nó ou quando tem muitos nós em execução
e precisa
monitorá-los.

3. **ros2 node info**: Depois de conhecer os nomes dos nós, você pode obter mais
informações sobre eles usando este comando. Ele retorna uma lista de assinantes,
publicadores, serviços e ações, ou seja, as conexões do gráfico ROS que
interagem com aquele
nó.

### 1.2. Remapeamento (Remapping)
O remapeamento permite reatribuir propriedades padrão do nó, como nomes de nós,
nomes de tópicos, nomes de serviços, etc., para valores personalizados. Por
exemplo, você pode reatribuir o nome do nó "/turtlesim" para "/my_turtle" usando
o comando `ros2 run turtlesim turtlesim_node --ros-args --remap
__node:=my_turtle`.

## 2. Tópicos

![](/gifs/topicos.gif)

[fonte](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)

O ROS 2 utiliza tópicos como um dos principais meios de comunicação entre nós. 
Os tópicos permitem que os dados sejam transmitidos entre nós, possibilitando a 
interação e a execução de tarefas complexas em sistemas robóticos. Aqui está um 
guia sobre como os tópicos funcionam no ROS 2, com base no tutorial fornecido.

### 2.1. Configuração Inicial
Antes de começar a explorar os tópicos, você precisa ter o ROS 2 e o pacote turtlesim instalados. Você deve iniciar os nós do turtlesim e do turtle_teleop_key em terminais separados usando os comandos:
```bash
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```

### 2.2. Visualizando com rqt_graph
O `rqt_graph` é uma ferramenta gráfica que permite visualizar os nós, tópicos e as conexões entre eles. Para executá-lo, use o comando:
```bash
rqt_graph
```
Você verá os nós e tópicos em execução, bem como as conexões entre eles.

### 2.3. Listando Tópicos
Para listar todos os tópicos ativos no sistema, use o comando:
```bash
ros2 topic list
```
Para ver os tipos de mensagens associados a cada tópico, adicione a opção `-t`:
```bash
ros2 topic list -t
```

### 2.4. Visualizando Dados de um Tópico
Para ver os dados sendo publicados em um tópico específico, use o comando:
```bash
ros2 topic echo <nome_do_tópico>
```
Por exemplo:
```bash
ros2 topic echo /turtle1/cmd_vel
```
Isso mostrará os dados sendo publicados no tópico `/turtle1/cmd_vel`.

### 2.5. Informações sobre um Tópico
Para obter informações sobre um tópico específico, como o número de publicadores e assinantes, use o comando:
```bash
ros2 topic info <nome_do_tópico>
```

### 2.6. Visualizando a Estrutura de uma Mensagem
Para ver a estrutura de uma mensagem de um tipo específico, use o comando:
```bash
ros2 interface show <tipo_da_mensagem>
```
Por exemplo:
```bash
ros2 interface show geometry_msgs/msg/Twist
```

### 2.7. Publicando em um Tópico
Você pode publicar dados em um tópico diretamente da linha de comando usando o comando:
```bash
ros2 topic pub <nome_do_tópico> <tipo_da_mensagem> '<dados>'
```
Por exemplo:
```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}'
```

### 2.8. Verificando a Taxa de Publicação
Para ver a taxa na qual os dados estão sendo publicados em um tópico, use o comando:
```bash
ros2 topic hz <nome_do_tópico>
```

