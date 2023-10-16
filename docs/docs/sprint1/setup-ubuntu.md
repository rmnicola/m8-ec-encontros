---
title: Instalação do Ubuntu
sidebar_position: 1
---

# Instalação do Ubuntu em cartão SD

## Criando um disco de boot

O primeiro passo para instalar o Ubuntu é a criação de um disco de boot.
Para isso, vamos utilizar o [Balena Etcher](https://etcher.balena.io/) e baixar
a imagem oficial do [Ubuntu 22.04](https://releases.ubuntu.com/22.04.3/ubuntu-22.04.3-desktop-amd64.iso).
A captura de tela abaixo resume o processo:

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/XePk0-KYkrg"
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

## Instalando o Ubuntu

A seguir, vai ser necessário reiniciar o computador com o disco de boot plugado
em sua porta USB. Durante o processo de inicialização, você precisará apertar a 
tecla `F12` para entrar no menu de `boot`. Você precisará escolher o dispositivo
que vai usar para o boot do sistema. Escolha o seu disco que acabou de usar para
gravar o Ubuntu.

Se tudo deu certo, você vai ser levado direto para a tela de instalação do 
Ubuntu. A partir daí, siga as instruções abaixo:

<div style={{ textAlign: 'center' }}>
    <iframe 
        style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }}
        src="https://www.youtube.com/embed/qMEGwP0PqTk" 
        frameborder="0" 
        allowFullScreen>
    </iframe>
</div>

### Particionando o cartão SD 

Ao criar as partições do cartão SD, sugiro a seguinte configuração mínima:

* Partição do tipo EFI com `500MB`. Essa partição serve para que o firmware da 
placa mãe consiga iniciar o processo de boot do sistema operacional. O bootloader 
utilizado vai ser instalado aqui (no caso do Ubuntu, GRUB).
* Partição do tipo EXT4 com o restante do tamanho do cartão SD com mountpoint 
em `/`. Essa partição é a raíz do seu sistema operacional.

Considerações sobre SWAP e partição montada em `/home`:

* A partição de SWAP serve para armazenar o que está na memória RAM no momento 
em que o sistema entra em modo de hibernação. Como o cartão SD que estamos 
usando tem 64GB e os notebooks comumente tem 16GB de RAM hoje em dia, uma partição 
de SWAP fica pouco viável.

* A partição montada em `/home` normalmente é utilizada por questões de segurança 
de dados. É mais fácil configurar ferramentas de backup se você tiver essa separação.
Diferente da raíz do sistema (`/`), o diretório casa (`/home`) guarda apenas arquivos
relacionados aos usuários do sistema.

