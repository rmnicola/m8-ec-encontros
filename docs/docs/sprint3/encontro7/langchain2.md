---
title: LangChain Pt. II
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Langchain pt II

Na seção anterior, conversamos sobre a principal vantagem do langchain:
criar um encadeamento (ou
[**correntes**](https://docs.kanaries.net/articles/langchain-chains-what-is-langchain))
de agentes usando a funcionalidade dos LLMs para executar tarefas
complexas.

**Cuma?**

Ok, eu admito que o conceito pode ser um pouco alienigena a principio,
então vamos tentar construir nossa intuição utilizando um exemplo.

Vamos imaginar um sistema simples para ajudar um viajante a encontrar um
destino de viagem de acordo com um de seus hobbys favoritos. Para fazer isso em
um sistema como o ChatGPT, podemos utilizar um prompt mais ou menos com essa
cara (vou utilizar o inglês por ser compatível com a maior parte dos modelos do
huggingface):

```
You are now my personal travel agent. Act as someone who has immense travel
experience and knows the best places in the world to do certain activities. I
want to know where I should go to eat live fish. Give the answers as a list of
items, no bigger than 5 items. For each item, create a simple sentence
justifying this choice.
```

Abaixo a resposta real que obtive do ChatGPT:

```md
...

1. **South Korea**: Visit a traditional sannakji restaurant in South Korea,
   where live octopus is a delicacy. The octopus is served freshly chopped and
   still moving, often seasoned with sesame oil.

2. **Japan**: In Japan, particularly in regions like Tokyo or Osaka, you can
   find ikizukuri, a method where the fish is prepared alive to ensure
   freshness. This is a traditional, albeit controversial, aspect of Japanese
   cuisine.

3. **China**: Certain regions in China offer dishes where live fish is quickly
   deep-fried or boiled, keeping the fish alive until just before eating. This
   is more common in rural or traditional areas.

4. **Vietnam**: In Vietnam, live fish eating can be part of the local culinary
   scene, especially in coastal areas where fresh seafood is abundant. This
   might involve dishes where the fish is lightly cooked or prepared at your
   table.

5. **Taiwan**: In Taiwan, particularly in night markets, you might find stalls
   serving dishes with live seafood, including fish. This is part of the
   diverse and adventurous street food culture.

...
```

Cortei uma parte da resposta pois o ChatGPT brigou comigo por querer comer
peixes vivos (eu não quero, é só o primeiro exemplo exótico que veio na minha
cabeça, ok?)

A resposta é boa, mas tem alguns problemas que consigo enxergar para o uso do
ChatGPT puro dessa forma:

1. Nem todo mundo sabe escrever um prompt decente. Saber escrever bons prompts
   é quase como saber fazer boas pesquisas no Google - praticamente um
   superpoder -, mas a verdade é que a maioria das pessoas não sabe fazer nem
   um, nem outro =(
2. Mesmo que eu saiba criar um bom prompt, é um tanto oneroso que o usuário
   tenha que digitar esse prompt toda vez que quiser ver em que lugares do
   mundo deve ir para fazer `X`
3. E se eu quiser criar uma série de ações um pouco mais complexa? Como um
   exemplo bobo, vamos assumir que estamos usando um modelo que é muito bom em
   gerar a primeira resposta, mas não consegue entender e nem gerar conteúdo em
   Português. Ora, nesse caso talvez eu precisasse abrir um segundo chat com um
   segundo modelo para poder gerar o prompt para o primeiro e, após receber a
   resposta em inglês, ainda enviar novamente ao "chat tradutor" para ter uma
   resposta inteligível para quem não domina a língua inglesa. Ficou mais
   chato, né?

Pois bem, o `LangChain` consegue resolver todos esses problemas. Para resolver
os problemas `1` e `2`, existem os **Prompt Templates**.

O **prompt template** nada mais é do que um... `fstring`. Sério, é só isso.
Olha só esse pedaço de código que eu retirei direto da [documentação do
langchain](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/):

```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", content="chickens")
```

Dê uma boa olhada nessa sintaxe. Viu? Pois é, é só um `fstring` com uma
abstração por cima. O Langchain é uma boa ferramenta, mas certamente sofre de
um probleminha de *overengineering* e acaba com umas abstrações que, na minha
opinião, mais complicam do que ajudam. Porém, também é minha opinião de que não
temos uma ferramenta melhor para prototipar chatbots rapidamente.

Fstring ou não, o fato é que com o langchain eu consigo rapidamente criar uma
estrutura de prompt extremamente específico em que o usuário só precisa dizer
algumas palavras e aproveitar a estrutura de um prompt bem feito.

**Tá, mas e o problema 3?**

Para esse, aí entram as **correntes**. Com o Langchain, é possível encadear
essas aplicações com o prompt super específico para criar uma estrutura de
pedidos mais complexas. Vamos criar uma restrição fictícia no ChatGPT e
imaginar que eu só consigo traduzir conteúdos em uma janela e pedir dicas de
viagem (em inglês) em outra.

Eu vou começar na janela de tradução com o seguinte pedido:

```
Traduza para o ingles o seguinte pedido:
Aja como um agente de viagens extremamente experiente e me ajude a encontrar os
melhores lugares do mundo para se tomar sorvete de baunilha. Crie uma lista com
no máximo 5 lugares e, para cada um deles, dê uma explicação de no máximo uma
frase.
```

A resposta que obtive foi:

```
Act as an extremely experienced travel agent and help me find the best places
in the world to eat vanilla ice cream. Create a list with up to 5 places and,
for each one, provide an explanation in no more than one sentence.
```

Agora, vou à janela de dicas de turismo e uso a resposta que recebi
diretamente. Recebo a nova resposta:

```
1. **Berthillon, Paris, France**: This iconic Parisian ice cream shop is
   renowned for its rich, artisanal vanilla ice cream, made with high-quality
   ingredients and traditional French techniques.

2. **Van Leeuwen Artisan Ice Cream, New York, USA**: Known for their natural
   ingredients and unique approach, their vanilla ice cream is a creamy,
   classic delight that perfectly captures the essence of pure vanilla.

3. **Giolitti, Rome, Italy**: A historic gelateria in Rome, Giolitti offers a
   luxurious vanilla ice cream that is creamy, rich, and infused with authentic
   Italian craftsmanship.

4. **Murphy’s Ice Cream, Dingle, Ireland**: Murphy's hand-makes their ice cream
   using local ingredients, and their vanilla flavor is celebrated for its
   creamy texture and deep, natural vanilla taste.

5. **Tokyo Ice Cream, Tokyo, Japan**: This spot in Tokyo offers a unique twist
   on vanilla ice cream, incorporating local Japanese ingredients to create a
   delicate and refined flavor profile.
```

Por fim, volto à janela do tradutor para que ele me dê a resposta final em
português:

```
1. Berthillon, Paris, França: Esta icônica sorveteria parisiense é famosa pelo seu
rico sorvete artesanal de baunilha, feito com ingredientes de alta qualidade e
técnicas tradicionais francesas.

2. Van Leeuwen Artisan Ice Cream, Nova York, EUA: Conhecida por seus ingredientes
naturais e abordagem única, o sorvete de baunilha deles é um deleite clássico e
cremoso que captura perfeitamente a essência da baunilha pura.

3. Giolitti, Roma, Itália: Uma histórica gelateria em Roma, a Giolitti oferece um
luxuoso sorvete de baunilha que é cremoso, rico e infundido com autêntico
artesanato italiano.

4. Murphy’s Ice Cream, Dingle, Irlanda: A Murphy's faz seus sorvetes à mão usando
ingredientes locais, e o sabor de baunilha deles é celebrado por sua textura
cremosa e profundo gosto natural de baunilha.

5. Tokyo Ice Cream, Tóquio, Japão: Este local em Tóquio oferece uma versão única
do sorvete de baunilha, incorporando ingredientes japoneses locais para criar
um perfil de sabor delicado e refinado.
```

Note que, o que fizemos, de fato, foi encadear três aplicações de LLM para
criar uma resposta possível apenas com a sua combinação. Segue um belíssimo
diagrama do que acabamos de fazer:

```
in PT ---> [Tradutor] in EN ---> [Agente] out EN ---> [Tradutor] out PT --->
```

Pois bem, isso é exatamente o que a tal da **corrente** do langchain faz. Sim,
a situação que criei conta com uma limitação forçada (o GPT4 resolve isso tudo
fácil em uma janela só), mas o fato é que cada vez mais há modelos de [LLM
especializados](https://blogs.infosys.com/emerging-technology-solutions/artificial-intelligence/large-learning-models-the-rising-demand-of-specialized-llms.html)
que superam até mesmo o GPT4 para algumas tarefas. Até mesmo a OpenAI
introduziu o conceito de [chats
customizados](https://openai.com/blog/introducing-gpts) na sua última
atualização. O fato é que LLMs conseguem produzir melhor resultados quando tem
uma tarefa simples e muito bem definida, o que significa que para criar uma
resposta a uma questão mais complexa faz total sentido o uso de encadeamentos.
