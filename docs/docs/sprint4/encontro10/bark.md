---
title: Text-to-speech
sidebar_position: 3
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Utilizando o Bark

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Repositório do Bark](https://github.com/suno-ai/bark)

</Admonition>

## 1. Instalando o bark

```bash
pip install git+https://github.com/suno-ai/bark.git
```

## 2. Exemplo simples utilizando o bark

```python
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import simpleaudio as sa

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# Convert the audio array to int16 format (required by simpleaudio)
audio_array_int16 = (audio_array * 32767).astype("int16")

# Play audio directly
play_obj = sa.play_buffer(audio_array_int16, 1, 2, SAMPLE_RATE)
play_obj.wait_done()  # Wait until audio finishes playing
```

## 3. Utilizando o ljspeech

O bark é um modelo consideravelmente pesado, fazendo com que seja bem difícil
utilizá-lo sem GPU. Utilizar modelos de sintetização de fala mais simples pode
ser uma solução aceitável.

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[Huggingface ljspeech](https://huggingface.co/NeuML/ljspeech-jets-onnx)

</Admonition>

## 3.1. Instalando o ljspeech

Para conseguir rodar o ljspeech com o exemplo do site acima, é necessário
instalar os seguintes pacotes:

```bash
pip install txtai[pipeline-audio] soundfile
```

## 3.2. Exemplo simples

```bash
import soundfile as sf
import simpleaudio as sa

from txtai.pipeline import TextToSpeech

# Build pipeline
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

# Generate speech
speech = tts("Say something here")

# Write to file
sf.write("out.wav", speech, 22050)

# Read the file
wave_obj = sa.WaveObject.from_wave_file("out.wav")

# Play audio
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until audio finishes playing
```

## 4. Utilizando a api da OpenAI

<Admonition 
    type="info" 
    icon=<img src={require('/img/autoestudo.png').default} width='20vw' />
    title="Autoestudo">

[OpenAI Text-to-speech](https://platform.openai.com/docs/guides/text-to-speech)

</Admonition>

Novamente, uma opção válida é utilizar a API paga da OpenAI para ter à
disposição modelos mais avançados de Text-to-speech sem precisar rodá-los
localmente. Segue um exemplo em Python:

```python
from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
```
