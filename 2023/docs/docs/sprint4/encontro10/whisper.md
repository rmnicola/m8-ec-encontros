---
title: Whisper
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Utilizando o OpenAI Whisper

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[OpenAI Whisper - repositório github](https://github.com/openai/whisper)

</Admonition>

## 1. Instalando o whisper

Para instalar o whisper, rode:

```bash
pip install -U openai-whisper
```

## 2. Interagindo com o whisper no terminal

O seguinte comando transcreverá a fala em arquivos de áudio, usando o modelo
`medium`:

```bash
whisper audio.flac audio.mp3 audio.wav --model medium
```

A configuração padrão (que seleciona o modelo `small`) funciona bem para
transcrever inglês. Para transcrever um arquivo de áudio contendo fala em outro
idioma, você pode especificar o idioma usando a opção `--language`:


```bash
whisper japanese.wav --language Japanese
```

Adicionar `--task translate` irá traduzir a fala para o inglês:

```bash
whisper japanese.wav --language Japanese --task translate
```

Execute o seguinte para ver todas as opções disponíveis:

```bash
whisper --help
```

Veja
[tokenizer.py](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py)
para a lista de todos os idiomas disponíveis.

## 3. Exemplo simples

O exemplo a seguir carrega um arquivo `mp3` para que o whisper transforme-o em
texto:

```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

O próximo exemplo utiliza o argparse para criar uma ferramenta um pouco mais
robusta para interagir com o whisper no terminal:

```python
import argparse
import whisper

def main():
    parser = argparse.ArgumentParser(
            description="Transcreve áudio em texto usando o Whisper."
            )
    parser.add_argument(
            '-m', '--model', type=str, required=True,
            help="O nome do modelo a ser usado (e.g. small, medium)."
            )
    parser.add_argument(
            '-f', '--file', type=str, required=True, 
            help="Caminho para o arquivo de áudio"
            )
    args = parser.parse_args()

    model = whisper.load_model(args.model)
    result = model.transcribe(args.file)
    print(result["text"])

if __name__ == "__main__":
    main()
```

## 4. Utilizando a API da OpenAI

Apesar de não ser um modelo muito pesado (principalmente se estiver utilizando
GPU), para alguns computadores a resposta do whisper pode ser muito lenta.
Nesses casos, pode-se utilizar a API da OpenAI para rodar o modelo no servidor
deles (opção paga). O exemplo a seguir demonstra como fazê-lo:

```python
from openai import OpenAI
client = OpenAI()

with open("speech.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file, 
      response_format="text"
    )

print(transcript)
```
