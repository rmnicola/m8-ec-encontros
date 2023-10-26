---
title: Pacotes e launchers
sidebar_position: 4
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Admonition from '@theme/Admonition';

# <img src={require('/img/opcional.png').default} width='35vw'/> Criando e utilizando pacotes em ROS

## 1. Criando um workspace em ROS 

O workspace de ROS é basicamente uma pasta onde se concentram um ou mais pacotes 
ROS. Ela é útil pois podemos juntar vários pacotes e compilá-los com apenas um
comando e também dar apenas um `source` para adicionar os comandos de
run/launch ao nosso sistema. 

Para criar um workspace ROS, basta criar uma pasta qualquer e, dentro dela,
adicionar uma subpasta `src`, que é onde vão ficar os nossos pacotes.

```bash
mkdir -p meu_workspace/src
```

Após isso, vamos entrar em nossa pasta `src` e adicionar um pacote de exemplo
para testarmos nosso workspace.

```bash 
cd meu_workspace/src
git clone https://github.com/ros/ros_tutorials.git -b humble 
```

Pacotes ROS costumeiramente tem dependências para serem executados. Para
garantir que temos as dependências necessárias para nosso pacote, precisamos
rodar o `rosdep`. Em nossa instalação, o `rosdep` não foi adicionado por
padrão. Precisamos, portanto, instalá-lo:

```bash 
sudo apt install python3-rosdep
```

Após a instalação, precisamos configurar o rosdep. Para isso, usaremos dois
comandos em sequência: 

```bash 
sudo rosdep init
rosdep update
```

Feito isso, basta resolver nossas dependências com: 

```bash 
cd meu_workspace #voltando para a pasta raíz do ws
rosdep install -i --from-path src --rosdistro humble -y
```

Pronto! Esse comando já vai checar todos os seus pacotes e instalar as
depedências automaticamente.

A seguir, vamos compilar o nosso pacote usando:

```bash 
colcon build
```

Pode ser que apareça um warning sobre o fim da vida do `setuptools`, mas está
tudo bem. Caso não esteja, basta forçar a instalação da versão `58.2.0` com:

```bash 
pip install setuptools==58.2.0
```

Note que surgiram as pastas `install`, `build` e `log` em seu workspace. Caso
queira subir seu ws para um repositório, não esqueça de adicionar essas pastas
ao `.gitignore`!

Para poder rodar o seu pacote, precisamos agora apenas dar `source` no script
de configuração do workspace. Fazemos isso com: 

```bash
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

Pronto! Seu workspace ROS está configurado e com um pacote funcionar. Vamos
criar o nosso próprio pacote agora?

## 2. Criando pacotes em ROS

Para criar nosso pacote, vamos utilizar o seguinte comando:

```bash 
ros2 pkg create --build-type ament_python --node-name my_node my_package
```

Note que a opção `node-name` faz com que o seu pacote já inicie com um exemplo
simples de Olá Mundo. Caso queira um pacote verdadeiramente vazio, rode: 

```bash 
ros2 pkg create --build-type ament_python <nome_do_pacote>
```

Como nosso pacote já veio com um exemplo, vamos só precisar dar build nele para
poder rodar alguma coisa dele:

```bash
colcon build
```

Como nosso ws tem dois pacotes, às vezes podemos querer especificar para
compilar apenas um (ou mais) pacotes em vez de compilar tudo o que está lá.
Podemos fazer isso com: 

```bash
colcon build --packages-select my_package
```

Após compilado, precisamos dar source no script de setup do WS:

```bash
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

Pronto! Quer rodar seu pacote? Use:

```bash
ros2 run my_package my_node
```

## 3. Criando launch files 

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Criando launch files em
ROS2](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html)
</Admonition>

## 3. Integrando launch files a pacotes ROS

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Integrando launch files a pacotes
ROS2](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Launch-system.html)
</Admonition>
