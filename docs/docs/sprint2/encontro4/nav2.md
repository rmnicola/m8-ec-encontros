---
title: Nav2
sidebar_position: 4
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import ReactPlayer from 'react-player'
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='40vw'/> Introdução ao Nav2

O nav2, também conhecido como Navigation2, é a segunda geração do sistema de
navegação para robôs desenvolvido para funcionar com o ROS 2. É um framework
modular e adaptável que fornece todas as ferramentas necessárias para
desenvolver e executar algoritmos de navegação em robôs, especialmente robôs
móveis. Graças à sua integração com ROS 2, o nav2 aproveita comunicações em
tempo real, segurança e outras melhorias essenciais para aplicações robóticas
modernas. Sua arquitetura é totalmente baseada em nós, serviços e ações, tendo
como uma de suas principais características o uso de árvores de comportamento
(behavior trees), que facilitam a definição de comportamento de navegação do
robô através de serviços modulares.

Entre as principais funcionalidades do nav2, destacam-se:

* Map server - funcionalidade de carregar servir e armazenar mapas;
* AMCL - funcionalidade de localização do robô em um mapa;
* Planner - planejamento de rota desviando de obstáculos;
* Controller - controle do robô enquanto segue a rota;
* Smoother - torna a rota planejada mais contínua, sem mudanças bruscas;
* Costmap 2D - converte dados de sensor em um mapas de custo representativos do
  ambiente de trabalho do robô;
* Behavior trees - construção de comportamentos complexos de forma modular;
* Recoveries - fallback em caso de falha no percurso;
* Waypoint follower - navegação através de uma sequência de pontos;
* Lifecycle Manager - gerenciamento do ciclo de vida dos nós;
* Core - sistema de plugins para habilitar seus próprios algoritmos e
  comportamentos;
* Collision monitor - monitora dados dos sensores buscando riscos iminentes de
  colisão;
* Simple commander - API em Python para interagir com o Nav2 programáticamente;

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
        src="https://www.youtube.com/embed/idQb2pB-h2Q" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

</Admonition>

## 1. Setup

Para usar o Nav2, deve-se primeiro garantir que o ROS está instalado e
configurado adequadamente. Ver [seção de configuração do
ROS](../../sprint1/encontro3/config-ros.md)

A seguir, vamos instalar três pacotes necessários para interagir com o Nav2 e,
especificamente, com o robô Turtlebot3 Burger:

<Tabs defaultValue="bash" values={[
        {label: 'Bash', value: 'bash'},
        {label: 'Zsh', value: 'zsh'},
  ]}>

<TabItem value="bash">

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*
```

</TabItem>

<TabItem value="zsh">

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup "ros-humble-turtlebot3*"
```

</TabItem>

</Tabs>

Após isso, vamos mexer em uma configuração que pode nos causar problemas mais
para frente quando formos interagir com o turtlebot, que é o algoritmo de DDS
utilizado pelo ROS. Para isso, instale o seguinte pacote: 

```bash
sudo apt install ros-humble-rmw-cyclonedds-cpp
```

A seguir, vamos adicionar uma variável de ambiente para que o ROS saiba dessa
mudança:

<Tabs defaultValue="bash" values={[
        {label: 'Bash', value: 'bash'},
        {label: 'Zsh', value: 'zsh'},
        {label: 'Zsh com a minha config.', value: 'zsh-meu'},
  ]}>

<TabItem value="bash">

```bash
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
```

</TabItem>

<TabItem value="zsh">

```bash
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.zshrc
```

</TabItem>

<TabItem value="zsh-meu">

```bash
# Nada. Já está configurado meu bem =)
# Caso esteja em uma versão antiga, só de um git pull no repo Dotfiles
cd Dotfiles && git pull origin main
```

</TabItem>

</Tabs>

A seguir, vamos mexer na configuração padrão do turtlebot para que ele use o
método adequado de localização. Vá para a pasta
`/opt/ros/humble/share/turtlebot3_navigation2/param` e modifique o arquivo
`burger.yaml`. Lá, vamos fazer uma modificação simples: na linha em que está
escrito `robot_model_type: "differential"` vamos mudar para `robot_model_type:
"nav2_amcl::DifferentialMotionModel"`.

Pronto! Tudo configurado para fazermos nosso primeiro mapa e nossa primeira
navegação!

## 2. Criando um mapa

Para criar nosso mapa, vamos primeiro precisar de um robô. Está com o seu
turtlebot aí do lado? Ótimo! Só garanta que ele está no mesmo `ROS_DOMAIN_ID` e
ignore a próxima instrução. Não está com o robô? Beleza também, pois podemos
usar o Gazebo. Para isso, rode o seguinte comando:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world_launch.py
```

:::caution Atenção

Pode ser que esse comando trave ao rodar pela primeira vez. Quando isso
aconteceu, tive sucesso ao mudar o modelo do robô (`TURTLEBOT_MODEL`) para
`waffle`. Após isso, o Gazebo abriu e, curiosamente, consegui mudar novamente
para o `burger` e também abriu sem problemas. Tente fazer isso também se tiver
probleams.

:::

Esse comando deve abrir uma janela com um mundo de teste e um turtlebot já
carregado. Vamos mover o robô? Para isso, use: 

```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

Siga as instruções que aparecem no terminal para movimentar o robô.

:::tip Dica

Não é possível mover o robô se a janela do terminal com o teleop não estiver em
foco. Isso pode deixar meio atabalhoado ver o robô e comandá-lo ao mesmo tempo.
Que tal pedir ajuda ao amigo do lado e já testar a configuração de rede do ROS2
de vocês?

:::

A seguir, vamos usar outro lançador para rodar os nós necessários para criar o
mapa. Rode: 

```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True 
```

:::tip Dica 

Notou o argumento `use_sim_time:=True`? Para mapear um ambiente com o robô
real, basta que essa variável seja `False`

:::

Se tudo deu certo, você deve ter agora uma segunda janela aberta, dessa vez com
um software chamado Rviz. O Rviz é uma ferramenta de visualização 3D para o ROS
que permite aos usuários visualizar dados de sensores, estados de robôs,
trajetórias e outros aspectos relacionados à robótica em tempo real.

E é isso! Já estamos mapeando! Mova seu robô pelo ambiente e você vai perceber
que o mapa vai aos poucos sendo construído. Quando seu mapa já não tiver quase
nenhum ponto indefinido, você pode salvá-lo no seu computador para usar mais
para frente durante a navegação. Para isso, rode: 

```bash 
ros2 run nav2_map_saver map_saver_cli -f <nome-do-mapa>
```

Substitua o `nome-do-mapa` pelo local onde quer gravar seu mapa. Eu coloquei
dentro da minha pasta `Documents`, então o comando ficou assim: 

```
mkdir -p ~/Documents/Maps 
ros2 run nav2_map_saver map_saver_cli -f ~/Documents/Maps/my-map
```

Prontinho! Você agora deve ter um arquivo de imagem (`pgm`) e outro arquivo com
metadados sobre o mapa (`yaml`). É só disso que precisa para poder navegar na
próxima etapa!

Apenas como ponto de comparação, meu mapa nesse momento estava assim:
<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
    <img src={require ("/img/my-map.png").default} width="40%"/>
</div>

## 3. Navegando no mapa criado

Estamos quase lá! Agora, para que possamos navegar usando nosso mapa, vamos
usar os seguintes lançadores:

```bash
# Se ainda estiver com o gazebo aberto, não precisa disso
ros2 launch turtlebot3_gazebo turtlebot3_world_launch.py
```

E:

```bash
# Substitua o arquivo-do-mapa pelo local onde está o seu mapa
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=<arquivo-do-mapa>.yaml
```

Se tudo deu certo, você deve estar com o Gazebo e o Rviz abertos novamente.
Toda a nossa navegação vai acontecer na janela do Rviz. Lá, você primeiro vai
setar a initial pose e depois vai mandar poses para que o robô navegue até
elas. Veja o `gif` abaixo para uma referência visual do processo:

<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
    <ReactPlayer playing controls
    url={require('/video/nav_turtle.webm').default} width="100%"/>
</div>

## 4. Usando o Simple Commander API

<Admonition 
    type="note" 
    icon=<img src={require('/gifs/loading.gif').default} width='20vw' />
    title="Work in progress...">
</Admonition>
