---
title: Expressões regulares
sidebar_position: 2
---
import Admonition from '@theme/Admonition';

# <img src={require('/img/autoestudo.png').default} width='35vw'/> Introdução à expressões regulares

Expressões regulares, também conhecidas como regex ou regexp, são padrões
utilizados para encontrar correspondências em strings de texto. Elas são
extremamente poderosas e versáteis, tornando-se uma ferramenta indispensável
para programadores, analistas de dados e qualquer pessoa que trabalhe com
processamento de texto. Este artigo tem como objetivo fornecer uma introdução
detalhada sobre o que são expressões regulares e como usá-las.

## 1. O que são Expressões Regulares?

Expressões regulares são sequências de caracteres que formam um padrão de
busca. Elas são utilizadas para realizar operações de busca e substituição em
textos, bem como para validação de formatos de dados. O poder das expressões
regulares reside em sua capacidade de descrever padrões complexos de forma
concisa.

## 2. Sintaxe Básica

A sintaxe das expressões regulares pode parecer intimidadora no início, mas com
prática e compreensão dos seus componentes básicos, ela se torna uma ferramenta
poderosa. Aqui estão alguns dos elementos fundamentais:

- **Caracteres Literais**: Correspondem exatamente ao caractere especificado.
  Por exemplo, a regex `a` corresponderá à letra "a".
- **Metacaracteres**: São caracteres especiais que têm um significado especial.
  Alguns exemplos incluem `.` (ponto) que corresponde a qualquer caractere,
  exceto quebra de linha, e `*` (asterisco) que indica zero ou mais ocorrências
  do caractere anterior.
- **Conjuntos de Caracteres**: Delimitados por colchetes `[]`, permitem definir
  um conjunto de caracteres que podem corresponder. Por exemplo, `[abc]`
  corresponderá a "a", "b" ou "c".
- **Quantificadores**: Especificam quantas vezes um caractere ou grupo de
  caracteres deve aparecer. Alguns exemplos são `+` (um ou mais), `?` (zero ou
  um) e `{n}` (exatamente n vezes).
- **Ancoragem**: `^` e `$` são utilizados para indicar o início e o fim de uma
  linha, respectivamente.
- **Grupos e Captura**: Delimitados por parênteses `()`, permitem agrupar
  expressões e capturar o texto correspondido para uso posterior.

### 2.1. Caracteres Literais
**Descrição**: Correspondem exatamente ao caractere especificado.

**Exemplo**: 
Regex: `a`

Texto: `gato`

Resultado: A regex `a` encontrará uma correspondência na letra "a" de "gato".

### 2.2. Metacaracteres
**Descrição**: São caracteres especiais que têm um significado especial.

**Exemplo**:
Regex: `g.t`

Texto: `gato`

Resultado: A regex `g.t` encontrará uma correspondência em "gat" de "gato",
pois o ponto corresponde a qualquer caractere.

#### 2.2.1. **Ponto (.)**: Corresponde a qualquer caractere, exceto quebra de linha.
- **Regex**: `a.c`
- **Texto**: `abc, adc, aec`
- **Resultado**: Corresponderá a "abc", "adc" e "aec".
   
#### 2.2.2. **Asterisco (*)**: Corresponde a zero ou mais ocorrências do caractere anterior.
- **Regex**: `lo*l`
- **Texto**: `l, lol, lool, loool`
- **Resultado**: Corresponderá a "l", "lol", "lool", "loool".

#### 2.2.3. **Mais (+)**: Corresponde a uma ou mais ocorrências do caractere anterior.
- **Regex**: `lo+l`
- **Texto**: `lol, lool, loool`
- **Resultado**: Corresponderá a "lol", "lool", "loool", mas não a "l".

#### 2.2.4. **Interrogação (?)**: Corresponde a zero ou uma ocorrência do caractere anterior.
- **Regex**: `lo?l`
- **Texto**: `l, lol`
- **Resultado**: Corresponderá a "l" e "lol".

#### 2.2.5. **Chaves ({})**: Especifica um número específico de ocorrências do caractere anterior.
- **Regex**: `lo{2}l`
- **Texto**: `lool`
- **Resultado**: Corresponderá apenas a "lool".

#### 2.2.6. **Barra Vertical (|)**: Atua como um operador OR.
- **Regex**: `gato|cachorro`
- **Texto**: `Tenho um gato e um cachorro.`
- **Resultado**: Corresponderá a "gato" e "cachorro".

#### 2.2.7. **Contra-barra (\)**: Usado para escapar metacaracteres.
- **Regex**: `3\+3 = 6`
- **Texto**: `3+3 = 6`
- **Resultado**: Corresponderá a "3+3 = 6".

#### 2.2.8. **Colchetes ([])**: Define um conjunto de caracteres.
- **Regex**: `[abc]`
- **Texto**: `a, b, c, d`
- **Resultado**: Corresponderá a "a", "b" e "c".

#### 2.2.9. **Hífen (-)**: Usado dentro de colchetes para definir um intervalo de caracteres.
- **Regex**: `[a-z]`
- **Texto**: `a, m, z`
- **Resultado**: Corresponderá a qualquer letra minúscula.

#### 2.2.10. **Circunflexo (^)**: Quando usado dentro de colchetes, nega o conjunto.
- **Regex**: `[^abc]`
- **Texto**: `a, b, c, d`
- **Resultado**: Corresponderá a "d".

#### 2.2.11. **Barra Invertida (\)**: Usada para representar caracteres especiais.
- **Regex**: `\\n`
- **Texto**: `\n`
- **Resultado**: Corresponderá a "\n".

#### 2.2.12. **Parênteses (())**: Usado para agrupar expressões.
- **Regex**: `(abc)+`
- **Texto**: `abcabcabc`
- **Resultado**: Corresponderá a "abcabcabc".

#### 2.2.13. **Cifrão ($)**: Ancoragem no final da linha.
- **Regex**: `fim$`
- **Texto**: 
```
É o fim
Não é o fim
```
- **Resultado**: Corresponderá a "fim" na primeira linha.

### 2.3. Conjuntos de Caracteres
**Descrição**: Permitem definir um conjunto de caracteres que podem corresponder.

**Exemplo**:
Regex: `[gmn]ato`

Texto: `mato`

Resultado: A regex `[gmn]ato` encontrará uma correspondência em "mato", pois
tanto "g", "m" quanto "n" são aceitáveis para a primeira posição.

#### 2.3.1. **Letras específicas**:
   - **Regex**: `[aeiou]`
   - **Texto**: `apple`
   - **Resultado**: Corresponderá às letras "a" e "e" em "apple".

#### 2.3.2. **Alcance de letras**:
   - **Regex**: `[a-e]`
   - **Texto**: `dog`
   - **Resultado**: Corresponderá às letras "d" e "e".

#### 2.3.3. **Alcance de números**:
   - **Regex**: `[0-5]`
   - **Texto**: `12389`
   - **Resultado**: Corresponderá aos números "1", "2", "3" e "5".

#### 2.3.4. **Combinação de alcances**:
   - **Regex**: `[a-c0-3]`
   - **Texto**: `b2z`
   - **Resultado**: Corresponderá à letra "b" e ao número "2".

#### 2.3.5. **Negação**: Usando `^` dentro dos colchetes, você pode negar um conjunto.
   - **Regex**: `[^aeiou]`
   - **Texto**: `apple`
   - **Resultado**: Corresponderá às letras "p", "p" e "l".

#### 2.3.6. **Combinação de caracteres específicos e alcances**:
   - **Regex**: `[AaEeIiOoUu]`
   - **Texto**: `Universe`
   - **Resultado**: Corresponderá às letras "U", "i" e "e".

#### 2.3.7. **Letras e números**:
   - **Regex**: `[a-zA-Z0-9]`
   - **Texto**: `D3sign`
   - **Resultado**: Corresponderá a todas as letras e números: "D", "3", "s", "i", "g", "n".

#### 2.3.8. **Caracteres especiais**: Para corresponder a caracteres especiais, basta listá-los no conjunto.
   - **Regex**: `[*.?+]`
   - **Texto**: `a+b.c?`
   - **Resultado**: Corresponderá aos caracteres "+", ".", "?".

Estes são exemplos de como os conjuntos de caracteres podem ser usados em expressões regulares para especificar um conjunto de caracteres possíveis em uma posição específica de uma string. Eles são extremamente úteis para criar padrões flexíveis e específicos ao mesmo tempo.

### 2.4. Quantificadores
**Descrição**: Especificam quantas vezes um caractere ou grupo de caracteres
deve aparecer.

**Exemplo**:
Regex: `ca?fé`

Texto: `café`

Resultado: A regex `ca?fé` encontrará uma correspondência em "café", pois o "a" pode aparecer zero ou uma vez.

#### 2.4.1. **Asterisco (*)**: Zero ou mais ocorrências do caractere ou padrão anterior.
- **Regex**: `ma*n`
- **Texto**: `mn, man, maan, maaan`
- **Resultado**: Corresponderá a todas as strings: "mn", "man", "maan", "maaan".

#### 2.4.2. **Mais (+)**: Uma ou mais ocorrências do caractere ou padrão anterior.
   - **Regex**: `ma+n`
   - **Texto**: `mn, man, maan, maaan`
   - **Resultado**: Corresponderá a "man", "maan", "maaan", mas não a "mn".

#### 2.4.3. **Interrogação (?)**: Zero ou uma ocorrência do caractere ou padrão anterior.
   - **Regex**: `ma?n`
   - **Texto**: `mn, man, maan`
   - **Resultado**: Corresponderá a "mn" e "man", mas não a "maan".

#### 2.4.4. **Chaves ({n})**: Exatamente n ocorrências do caractere ou padrão anterior.
   - **Regex**: `ma{2}n`
   - **Texto**: `man, maan, maaan`
   - **Resultado**: Corresponderá apenas a "maan".

#### 2.4.5. **Chaves ({n,})**: n ou mais ocorrências do caractere ou padrão anterior.
   - **Regex**: `ma{2,}n`
   - **Texto**: `man, maan, maaan`
   - **Resultado**: Corresponderá a "maan" e "maaan", mas não a "man".

#### 2.4.6. **Chaves ({n,m})**: Entre n e m ocorrências do caractere ou padrão anterior.
   - **Regex**: `ma{2,3}n`
   - **Texto**: `man, maan, maaan, maaaan`
   - **Resultado**: Corresponderá a "maan" e "maaan", mas não a "man" ou "maaaan".

#### 2.4.7. **Interrogação após outro quantificador ("Lazy Matching")**:   
Em expressões regulares, os quantificadores por padrão são "gananciosos", o que
significa que eles tentarão corresponder ao máximo possível. No entanto, quando
colocamos uma interrogação após um quantificador, estamos tornando esse
quantificador "preguiçoso", ou seja, ele tentará corresponder ao mínimo
possível.

   - **Regex**: `a.+?b`
   - **Texto**: `acdcabcab`
   - **Resultado**: Corresponderá a "acdcab" em vez de capturar a string mais longa possível.

### 2.5. Ancoragem
**Descrição**: ^ e $ são utilizados para indicar o início e o fim de uma linha,
respectivamente.

**Exemplo**:
Regex: `^gato$`

Texto: `gato`

Resultado: A regex `^gato$` encontrará uma correspondência em "gato", pois a
palavra "gato" é exatamente a única coisa na linha.

#### 2.5.1. Ancoragem no Início da Linha (^)
**Regex**: `^Bom dia`

**Texto**: 
```
Bom dia, como você está?
Espero que esteja tendo um Bom dia!
```

**Resultado**: A regex `^Bom dia` corresponderá apenas à ocorrência de "Bom dia" que está no início da primeira linha.

#### 2.5.2. Ancoragem no Final da Linha ($)
**Regex**: `um Bom dia!$`

**Texto**: 
```
Bom dia, como você está?
Espero que esteja tendo um Bom dia!
```

**Resultado**: A regex `um Bom dia!$` corresponderá apenas à ocorrência de "um Bom dia!" que está no final da segunda linha.

### 2.6. Grupos e Captura
**Descrição**: Permitem agrupar expressões e capturar o texto correspondido
para uso posterior.

**Exemplo**:
Regex: `(ga|ma)to`

Texto: `gato`

Resultado: A regex `(ga|ma)to` encontrará uma correspondência em "gato", pois
tanto "ga" quanto "ma" são aceitáveis. Além disso, o "ga" correspondente é
capturado e pode ser referenciado ou usado posteriormente.

#### 2.6.1. **Capturando um grupo simples**:
   - **Regex**: `(ab)+`
   - **Texto**: `ababab`
   - **Resultado**: Corresponderá a toda a string "ababab", e cada "ab" individualmente será capturado como um grupo.

#### 2.6.2. **Capturando múltiplos grupos**:
   - **Regex**: `(a)(b+)`
   - **Texto**: `abbb`
   - **Resultado**: O primeiro grupo capturará "a" e o segundo grupo capturará "bbb".

#### 2.6.3. **Referenciando grupos capturados**:
   - **Regex**: `(a|e)i\1`
   - **Texto**: `aia`, `eie`
   - **Resultado**: Corresponderá a "aia" e "eie". A referência `\1` refere-se ao conteúdo do primeiro grupo capturado.

#### 2.6.4. **Capturando grupos opcionais**:
   - **Regex**: `Feb(ruary)?`
   - **Texto**: `Feb`, `February`
   - **Resultado**: Corresponderá a "Feb" e "February". O grupo "ruary" é opcional devido ao `?`.

#### 2.6.5. **Capturando grupos com quantificadores**:
   - **Regex**: `(abc){2,}`
   - **Texto**: `abcabcabc`
   - **Resultado**: Corresponderá a toda a string "abcabcabc", indicando que o grupo "abc" ocorre 2 ou mais vezes.

#### 2.6.6. **Grupos não capturadores**: Às vezes, queremos agrupar sem capturar. Para isso, usamos `?:` no início do grupo.
   - **Regex**: `(?:ab)+c`
   - **Texto**: `ababc`
   - **Resultado**: Corresponderá a "ababc", mas o "ab" não será capturado como um grupo.

#### 2.6.7. **Nomeando grupos de captura**:
   - **Regex**: `(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})`
   - **Texto**: `2023-11-01`
   - **Resultado**: Três grupos são capturados: "year" com valor "2023", "month" com valor "11" e "day" com valor "01".

#### 2.6.8. **Alternância dentro de grupos**:
   - **Regex**: `(apple|banana|cherry)`
   - **Texto**: `I like banana`
   - **Resultado**: O grupo corresponderá à palavra "banana".

## 3. Usando Expressões Regulares

Para usar expressões regulares, você precisa de uma linguagem de programação ou
ferramenta que as suporte. A maioria das linguagens modernas, como Python,
Java, JavaScript, entre outras, possuem bibliotecas ou módulos dedicados para
trabalhar com regex.

### 3.1. Biblioteca re de Python

Aqui está um exemplo simples de como usar expressões regulares em Python:

```python
import re

texto = "Meu número de telefone é (123) 456-7890."
padrao = re.compile(r"\(\d{3}\) \d{3}-\d{4}")
resultado = padrao.search(texto)

if resultado:
    print("Número de telefone encontrado:", resultado.group())
else:
    print("Número de telefone não encontrado.")
```

Neste exemplo, usamos a expressão regular `\(\d{3}\) \d{3}-\d{4}` para buscar
por um número de telefone no formato (123) 456-7890. O `\d` corresponde a
qualquer dígito, e `{3}` especifica que queremos exatamente três dígitos.

### 3.2. Utilizando o grep 

**O que é `grep`?**

O `grep` é uma ferramenta de linha de comando disponível em sistemas Unix e
Linux que permite pesquisar um padrão específico em um ou mais arquivos. A
palavra "grep" é um acrônimo para "Global Regular Expression Print", e, como o
nome indica, o `grep` permite o uso de expressões regulares para especificar
padrões de pesquisa.

**Como funciona o `grep`?**

Em sua forma mais simples, o `grep` pesquisa um padrão em um arquivo e imprime
as linhas que contêm esse padrão. A sintaxe básica é:

```
grep 'padrão' arquivo
```

**Exemplos básicos de uso do `grep`**:

1. **Pesquisar a palavra "erro" em um arquivo de log**:
   ```
   grep 'erro' /var/log/syslog
   ```

2. **Pesquisar recursivamente em todos os arquivos de um diretório**:
   ```
   grep -r 'padrão' /caminho/do/diretório/
   ```

3. **Pesquisar com ignorância de case (maiúsculas/minúsculas)**:
   ```
   grep -i 'erro' /var/log/syslog
   ```

4. **Pesquisar e mostrar o número da linha**:
   ```
   grep -n 'padrão' arquivo.txt
   ```

5. **Usar expressões regulares**:
   ```
   grep '^Erro:' arquivo.log
   ```

**Exemplo para verificar arquivos `.srv` entre os pacotes instalados para ROS**:

Os arquivos `.srv` no ROS (Robot Operating System) são usados para definir os
tipos de serviço. Se você quiser verificar a presença de arquivos `.srv` entre
os pacotes instalados, você pode fazer algo assim:

```
grep -r '\.srv' /caminho/para/seu/workspace_ros/src/
```

Neste exemplo, o `-r` faz uma busca recursiva no diretório especificado. O
padrão `'\.srv'` busca por arquivos que terminam com a extensão `.srv`. O `\.`
é usado para escapar o ponto, de modo que ele seja tratado literalmente, e não
como um metacaractere.

Lembre-se de ajustar `/caminho/para/seu/workspace_ros/src/` para o caminho real
do seu workspace ROS.

O `grep` é uma ferramenta poderosa e possui muitas opções adicionais. Consultar
o manual (`man grep`) é sempre uma boa ideia para explorar todas as suas
capacidades.

## 4. Dicas e Boas Práticas

- **Teste Suas Expressões Regulares**: Utilize ferramentas online como
  regex101.com para testar e depurar suas expressões regulares.
- **Seja Específico**: Quanto mais específica for sua expressão regular, menor
  a chance de corresponder a textos indesejados.
- **Atenção ao Desempenho**: Expressões regulares muito complexas podem ser
  lentas. Certifique-se de avaliar o desempenho, especialmente ao processar
  grandes volumes de texto.
Claro! Aqui estão três exemplos de expressões regulares e seus respectivos usos:

## 5. Exemplos de expressões regulares

### 5.1. Validar Endereços de E-mail

**Expressão Regular**: 
```
^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$
```

**Descrição**: 
Esta expressão regular é usada para validar endereços de e-mail. Ela verifica
se o e-mail começa com uma sequência de caracteres alfanuméricos, pontos ou
hifens, seguida de um "@", depois por outra sequência de caracteres
alfanuméricos, pontos ou hifens, e finalmente termina com um ponto seguido de
duas ou mais letras (indicando o domínio, como ".com" ou ".org").

**Exemplo de Uso**:
```python
import re

email = "nome.exemplo@email.com"
padrao = re.compile(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$")

if padrao.match(email):
    print("E-mail válido!")
else:
    print("E-mail inválido.")
```

### 5.2. Extrair Datas no Formato DD/MM/AAAA

**Expressão Regular**: 
```
(\d{2}/\d{2}/\d{4})
```

**Descrição**: 
Esta expressão regular é usada para extrair datas no formato DD/MM/AAAA de um
texto. Ela procura por duas sequências de dois dígitos separadas por uma barra,
seguidas de uma sequência de quatro dígitos.

**Exemplo de Uso**:
```python
import re

texto = "As datas são 01/01/2022 e 15/03/2023."
padrao = re.compile(r"(\d{2}/\d{2}/\d{4})")

datas_encontradas = padrao.findall(texto)
print("Datas encontradas:", datas_encontradas)
```

### 5.3. Verificar se uma Senha é Forte

**Expressão Regular**: 
```
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$
```

**Descrição**: 
Esta expressão regular é usada para verificar se uma senha é considerada forte.
A senha deve:
- Ter pelo menos 8 caracteres
- Conter pelo menos uma letra minúscula
- Conter pelo menos uma letra maiúscula
- Conter pelo menos um dígito
- Conter pelo menos um dos caracteres especiais: @$!%*?&#

**Exemplo de Uso**:
```python
import re

senha = "Exemplo@123"
padrao = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$")

if padrao.match(senha):
    print("Senha forte!")
else:
    print("Senha fraca.")
```

Estes são apenas exemplos básicos e ilustrativos do poder e versatilidade das
expressões regulares. Em situações reais, é importante testar e ajustar as
regex de acordo com as necessidades específicas do contexto em que serão
aplicadas.
