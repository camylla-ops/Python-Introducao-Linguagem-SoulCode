## Comentários em Python

Os comentários em Python são trechos de texto que são ignorados pelo interpretador Python durante a execução do programa. Eles são usados para adicionar notas, explicações ou anotações ao código fonte, facilitando a compreensão do programa para outros desenvolvedores ou para si mesmo no futuro.

Existem duas formas de criar comentários em Python:

1. Comentários em linha: São criados utilizando o símbolo de cerquilha (#) e tudo que vem após ele na mesma linha é considerado um comentário. Por exemplo:

   ```python
   # Este é um comentário em linha
   
2. Comentários em bloco: São criados utilizando três aspas duplas ("") no início e no fim do bloco de comentário. Por exemplo:

  ```python
    """
    Este é um comentário
    em bloco que pode
    ocupar várias linhas.
   """
```
## Variáveis em Python

são nomes utilizados para armazenar dados. Elas são criadas atribuindo um valor a um nome específico. Exemplo:

``` python
idade = 25
nome = "Maria"
```

##  Manipulação de dados

1. Tipos de variáveis a serem usadas

Inteiro (integer): Utilizado para armazenar números inteiros, sem casas decimais. Exemplo:

``` python
idade = 25. 
```
Ponto flutuante (float): Utilizado para armazenar números com casas decimais. Exemplo: 
``` python
altura = 1.75.
``` 
String (string): Utilizado para armazenar texto. As strings são delimitadas por aspas simples ('') ou aspas duplas (""). Exemplo:

``` python
nome = "Maria".
```

Booleano (boolean): Utilizado para armazenar valores verdadeiro (True) ou falso (False). Exemplo: 
``` python
tem_carteira = True
```

2. Saída de dados em Python

Em Python, você pode exibir a saída de dados utilizando a função print(). A função print() permite exibir texto, variáveis e outros valores na saída do programa. Aqui estão alguns exemplos de como usar a função print() para exibir a saída de dados em Python:

Exemplo 1: Exibindo uma mensagem simples:

``` python
print("Olá, mundo!")
```

Saída:
``` python
Olá, mundo!
``` 
Exemplo 2: Exibindo o valor de uma variável:
``` python
nome = "Maria"
print("Olá,", nome)
``` 
Saída:
``` python
Olá, Maria
``` 
Exemplo 3: Exibindo cálculos e formatação:

``` python
idade = 25
altura = 1.75
imc = idade / (altura ** 2)
print("Seu IMC é:", round(imc, 2))
``` 

Saída:
``` python
Seu IMC é: 8.16
``` 
Você também pode combinar texto e variáveis usando o operador de concatenação (+) ou formatar a saída usando f-strings ou a função format(). Aqui está um exemplo usando f-strings:

``` python

nome = "João"
idade = 30

print(f"Meu nome é {nome} e tenho {idade} anos.")
``` 
Saída:
``` python
Meu nome é João e tenho 30 anos.
```

3. Entrada de Dados em Python

Em Python, você pode solicitar a entrada de dados do usuário utilizando a função input(). 
A função input() permite que você exiba uma mensagem ao usuário e aguarde a entrada de dados. A entrada do usuário é retornada como uma string. Aqui está um exemplo de como usar a função input() para obter a entrada de dados em Python:

Exemplo 1: Solicitando um nome e exibindo uma mensagem personalizada:

``` python
nome = input("Digite o seu nome: ")
print("Olá, " + nome + "! Bem-vindo(a)!")
```
Saída:
``` python
Digite o seu nome: Maria
Olá, Maria! Bem-vindo(a)!
```

Exemplo 2: Solicitando um número e realizando um cálculo:
``` python
numero = float(input("Digite um número: "))
dobro = numero * 2
print("O dobro de", numero, "é", dobro)
```

Saída:
``` python

Digite um número: 5
O dobro de 5.0 é 10.0
``` 
Observe que, no segundo exemplo, utilizamos a função float() para converter a entrada do usuário em um número de ponto flutuante (float). Isso permite que o cálculo seja realizado corretamente.

Você também pode armazenar a entrada do usuário em uma variável para uso posterior no seu programa. Por exemplo:

``` python
idade = int(input("Digite a sua idade: "))
ano_nascimento = 2023 - idade
print("Você nasceu em", ano_nascimento)
``` 
Saída:
``` python
Digite a sua idade: 25
Você nasceu em 1998
```

4. Operadores aritméticos

Os operadores aritméticos em Python permitem realizar operações matemáticas em valores numéricos. Aqui estão os principais operadores aritméticos em Python:

Adição (+): Realiza a adição de dois valores.
Exemplo: resultado = 5 + 3 (resultado será 8)

Subtração (-): Realiza a subtração de dois valores.
Exemplo: resultado = 7 - 2 (resultado será 5)

Multiplicação (*): Realiza a multiplicação de dois valores.
Exemplo: resultado = 4 * 6 (resultado será 24)

Divisão (/): Realiza a divisão de dois valores. O resultado é um número de ponto flutuante.
Exemplo: resultado = 10 / 3 (resultado será 3.3333...)

Divisão inteira (//): Realiza a divisão de dois valores e retorna a parte inteira do resultado.
Exemplo: resultado = 10 // 3 (resultado será 3)

Módulo (%): Retorna o resto da divisão entre dois valores.
Exemplo: resultado = 10 % 3 (resultado será 1)

Exponenciação ():** Realiza a exponenciação de um valor pelo outro.
Exemplo: resultado = 2 ** 3 (resultado será 8)

Operador de atribuição (=): Atribui um valor à variável.
Exemplo: x = 5 (a variável x receberá o valor 5)

## Estruturas de condição

Operadores de igualdade 

== 
!=

1. Operadores de relação e condição

Em Python, os operadores de relação são utilizados para comparar valores e retornar um resultado booleano (verdadeiro ou falso) com base na relação entre os valores. A seguir estão os principais operadores de relação em Python:

Igual a: ==

Diferente de: !=

Maior que: >

Menor que: <
              
Maior ou igual a: >=

Menor ou igual a: <=

Exemplos de Uso

``` python
a = 5
b = 10

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True
```

2. O comando If else
    comando if é uma estrutura de controle condicional em Python que permite executar um bloco de código se uma determinada condição for verdadeira. O bloco de código dentro do if é executado apenas se a condição especificada for avaliada como verdadeira. Opcionalmente, você também pode usar o else para executar um bloco de código alternativo quando a condição do if for falsa.

Aqui está a sintaxe básica do comando if com else em Python:

```` python

if condição:
    # Bloco de código a ser executado se a condição for verdadeira
else:
    # Bloco de código a ser executado se a condição for falsa
   ````
Aqui está um exemplo simples para ilustrar o uso do if e else:

```` python

idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
````

Você também pode usar elif para adicionar condições adicionais ao seu comando if. O elif é uma abreviação de "else if" e permite verificar condições adicionais quando a condição anterior é falsa. Aqui está um exemplo:

```` python

idade = 18

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")

````
## Estruturas de controle de fluxo

1.  Laço de repetição While:
 
 O laço "while" executa um bloco de código repetidamente enquanto uma condição específica for verdadeira.
 
```` python
while condição:
    # bloco de código a ser repetido enquanto a condição for verdadeira
````

exemplo simples que usa um laço while para imprimir os números de 1 a 5:
```` python 
contador = 1

while contador <= 5:
    print(contador)
    contador += 1   
````

Neste exemplo, definimos a variável contador com o valor inicial de 1. O bloco de código dentro do while imprime o valor do contador e, em seguida, incrementa o contador em 1. O laço while continua executando enquanto o contador for menor ou igual a 5. Após a execução do bloco de código para o contador igual a 5, a condição se torna falsa e o laço while é interrompido.

A saída deste exemplo será:

```` python
1
2
3
4
5
````

2. Laço de repetição for

 O laço "for" é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou outros objetos iteráveis. 

 ```` python
for item in sequência:
    # bloco de código a ser executado para cada item na sequência
````

exemplo simples de uso da estrutura de controle "for" em Python:

```` python

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
````
Temos uma lista chamada frutas que contém três elementos: "maçã", "banana" e "laranja". Usamos a estrutura "for" para percorrer cada elemento da lista e imprimir seu valor. A cada iteração, a variável fruta recebe um elemento da lista e é impressa na tela.  

A saída do programa será:

```` python
maçã
banana
laranja 

````
3. Laço for range
    O laço "for" em combinação com a função range() é uma estrutura comumente utilizada para executar um bloco de código um número específico de vezes. A função range() retorna uma sequência de números que pode ser utilizada para controlar a iteração do laço.

Aqui está um exemplo de como usar o laço "for" com a função range():

````python

for i in range(5):
    print(i)
   ````
Neste exemplo, o laço "for" irá iterar cinco vezes, pois a função range(5) gera uma sequência de números de 0 a 4 (excluindo o número 5). A cada iteração, a variável i recebe o valor do próximo número da sequência e é impressa na tela.

A saída do programa será:

````python
0
1
2
3
4
````
Você também pode especificar o início, fim e passo da sequência usando a função range() da seguinte forma:

`````python

for i in range(1, 10, 2):
    print(i)
   `````
Neste exemplo, o laço "for" irá iterar começando de 1 e indo até 10 (excluindo o número 10), com um passo de 2. A cada iteração, a variável i recebe o próximo número da sequência e é impressa na tela.

A saída do programa será:

`````python
1
3
5
7
9
`````

3. Instrução break e continue

  As instruções "break" e "continue" são utilizadas dentro de estruturas de controle de fluxo, como os laços "for" e "while", para controlar o comportamento do programa durante a execução. Aqui está uma explicação de como essas instruções funcionam:

Instrução "break":
A instrução "break" é usada para interromper a execução de um laço de repetição imediatamente quando uma condição específica for atendida. Quando o programa encontra a instrução "break", ele sai do laço e continua a execução a partir da próxima linha de código após o laço.
Aqui está um exemplo que utiliza a instrução "break" dentro de um laço "for":

`````python
frutas = ["maçã", "banana", "laranja", "abacaxi", "uva"]

for fruta in frutas:
    if fruta == "laranja":
        break
    print(fruta)
   `````


Instrução "continue":
A instrução "continue" é usada para pular o restante do bloco de código atual em uma iteração de um laço de repetição e continuar para a próxima iteração. Quando o programa encontra a instrução "continue", ele ignora o restante do bloco de código do laço e passa para a próxima iteração.
Aqui está um exemplo que utiliza a instrução "continue" dentro de um laço "for":

`````python

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
   `````

## Strings

 1. Introdução a Strings
    
Uma string pode ser definida utilizando aspas simples (' ') ou aspas duplas (" "). Por exemplo:

`````python

nome = 'João'
mensagem = "Olá, mundo!"
`````

2. Comprimento:

Você pode obter o comprimento de uma string usando a função embutida len(). Ela retorna o número de caracteres na string. Por exemplo:

`````python

mensagem = "Olá, Python!"
comprimento = len(mensagem)  # 13
`````

3. Divisão
   A divisão de strings em Python pode ser realizada utilizando o método split(). Esse método divide uma string em uma lista de substrings com base em um separador especificado.

Aqui está um exemplo de como usar o método split() para dividir uma string em substrings:

`````python

frase = "Python é uma linguagem de programação"
palavras = frase.split()  # dividir a frase em palavras
print(palavras)
`````

4. substituição

    A substituição de partes de uma string em Python pode ser realizada usando o método replace(). Esse método permite substituir uma substring por outra em uma string.

Aqui está um exemplo de como usar o método replace() para substituir uma parte específica de uma string:

`````python

frase = "Python é uma ótima linguagem de programação"
nova_frase = frase.replace("ótima", "excelente")
print(nova_frase)
`````
5. Fatiando Strings
 
   Fatiar strings em Python é uma forma de extrair uma parte específica da string com base em índices. Você pode usar a notação de fatiamento (slicing) para obter uma substring da string original.

Aqui estão alguns exemplos de como fatiar strings em Python:

`````python
frase = "Python é uma ótima linguagem de programação"

# Obtendo os primeiros 6 caracteres
primeiros_caracteres = frase[:6]
print(primeiros_caracteres)  # Saída: "Python"

# Obtendo os caracteres a partir do índice 7 até o final
restante_caracteres = frase[7:]
print(restante_caracteres)  # Saída: "é uma ótima linguagem de programação"

# Obtendo uma substring específica usando índices
substring = frase[7:18]
print(substring)  # Saída: "é uma ótima"

# Obtendo a string invertida
invertida = frase[::-1]
print(invertida)  # Saída: "ãçãrganamargorp ed meganuil amu é nohtyP"
`````

6. Comparando Strings

    Em Python, é possível comparar strings usando operadores de comparação, como ==, !=, <, >, <= e >=. Esses operadores comparam as strings lexicograficamente, ou seja, comparando os caracteres um a um, da esquerda para a direita, com base nos valores ASCII dos caracteres.

Aqui estão alguns exemplos de comparação de strings em Python:

`````python
# Exemplo 1
fruta1 = "maçã"
fruta2 = "banana"

if fruta1 == fruta2:
    print("As frutas são iguais")
else:
    print("As frutas são diferentes")

# Exemplo 2
texto1 = "Python"
texto2 = "python"

if texto1.lower() == texto2.lower():
    print("Os textos são iguais (ignorando maiúsculas e minúsculas)")
else:
    print("Os textos são diferentes")

# Exemplo 3
nome1 = "João"
nome2 = "Maria"

if nome1 < nome2:
    print("O nome", nome1, "vem antes de", nome2, "na ordem alfabética")
else:
    print("O nome", nome1, "vem depois de", nome2, "na ordem alfabética")
   `````

5. Percorrendo Strings
  Ao percorrer uma string em Python, você pode usar um loop for ou um loop while para iterar por cada caractere individualmente. Existem várias abordagens possíveis para percorrer uma string, dependendo do que você deseja realizar.

Aqui estão alguns exemplos de como percorrer uma string em Python:

Usando o loop for:

`````python
string = "Python"

# Percorrendo a string usando um loop for
for caractere in string:
    print(caractere)
  ````` 
Neste exemplo, o loop for itera por cada caractere da string e imprime o caractere na tela. Cada iteração do loop atribui o próximo caractere da string à variável caractere, que pode ser usada dentro do loop para executar alguma ação.

Usando um índice e o loop for:

`````python
string = "Python"

# Percorrendo a string usando um loop for com base em índices
for i in range(len(string)):
    caractere = string[i]
    print(f"O caractere no índice {i} é {caractere}")
   `````
Neste exemplo, usamos o loop for em conjunto com a função range() e len() para percorrer os índices da string. Dentro do loop, obtemos o caractere correspondente ao índice atual e realizamos alguma ação com ele.

Usando um loop while com um índice:

`````python
string = "Python"

# Percorrendo a string usando um loop while com base em índices
indice = 0
while indice < len(string):
    caractere = string[indice]
    print(f"O caractere no índice {indice} é {caractere}")
    indice += 
   `````
## Estrutura de Listas

1.  Introdução a listas
 Em Python, uma lista é uma estrutura de dados que permite armazenar múltiplos valores em uma única variável. As listas são representadas por colchetes [] e 
 podem conter elementos de diferentes tipos, como números, strings, booleanos e até mesmo outras listas.

 Aqui está um exemplo de criação e manipulação básica de listas em Python:

 `````python

 # Criando uma lista vazia
 lista_vazia = []

 # Criando uma lista com elementos
 lista_numeros = [1, 2, 3, 4, 5]
 lista_strings = ["maçã", "banana", "laranja"]
 lista_mista = [10, "python", True]

 # Acessando elementos da lista
 primeiro_elemento = lista_numeros[0]
 segundo_elemento = lista_strings[1]
 ultimo_elemento = lista_mista[-1]

 # Modificando elementos da lista
 lista_numeros[2] = 10
 lista_strings.append("abacaxi")
 del lista_mista[1]

 # Tamanho da lista
 tamanho_lista = len(lista_strings)

 # Iterando sobre uma lista
 for elemento in lista_numeros:
    print(elemento)

 # Verificando a existência de um elemento na lista
 if "banana" in lista_strings:
    print("A lista contém a palavra 'banana'")
`````

2. Percorrendo listas
   Existem várias maneiras de percorrer uma lista em Python. Você pode usar um loop for, um loop while ou até mesmo funções embutidas como enumerate() ou zip(). Vou mostrar alguns exemplos de como percorrer uma lista usando diferentes abordagens:

Percorrendo uma lista com um loop for:

`````python

lista = [1, 2, 3, 4, 5]

# Usando um loop for para percorrer a lista
for elemento in lista:
    print(elemento)
   `````

Neste exemplo, usamos um loop for para percorrer cada elemento da lista. A variável elemento assume o valor de cada elemento da lista em cada iteração.

Percorrendo uma lista com um loop while e um índice:

`````python
lista = [1, 2, 3, 4, 5]

# Usando um loop while com um índice para percorrer a lista
indice = 0
while indice < len(lista):
    elemento = lista[indice]
    print(elemento)
    indice += 1
   `````

Neste exemplo, usamos um loop while em conjunto com um índice para percorrer a lista. Inicializamos o índice como 0 e incrementamos seu valor a cada iteração. Enquanto o índice for menor que o comprimento da lista, obtemos o elemento correspondente ao índice atual e realizamos alguma ação com ele.

Percorrendo uma lista com a função enumerate():

`````python

lista = [1, 2, 3, 4, 5]

# Usando a função enumerate() para percorrer a lista
for indice, elemento in enumerate(lista):
    print(f"Índice: {indice}, Elemento: {elemento}")
   `````
    
3.  Fatiando listas
   
Fatiar uma lista em Python permite que você selecione uma parte específica da lista com base em intervalos de índices. Isso é útil quando você deseja extrair uma subsequência de elementos de uma lista maior. Para fatiar uma lista, você pode usar a notação de fatiamento, que utiliza dois pontos (:).

Aqui estão alguns exemplos de como fatiar listas em Python:

`````python

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Fatiando uma lista para obter uma sublista
sublista = lista[2:6]
print(sublista)  # Saída: [3, 4, 5, 6]

# Fatiando uma lista do início até um determinado índice
sublista_inicio = lista[:4]
print(sublista_inicio)  # Saída: [1, 2, 3, 4]

# Fatiando uma lista de um determinado índice até o final
sublista_fim = lista[6:]
print(sublista_fim)  # Saída: [7, 8, 9, 10]

# Fatiando uma lista com intervalo e passo
sublista_passo = lista[1:9:2]
print(sublista_passo)  # Saída: [2, 4, 6, 8]
`````

3. Incluir, alterar, excluir elemento de listas
 
Para incluir, alterar e excluir elementos de uma lista em Python, você pode usar diversas operações e métodos disponíveis. Vou apresentar alguns exemplos:

Incluir elementos em uma lista:

Usando o método append():

`````python

lista = [1, 2, 3]
lista.append(4)
print(lista)  # Saída: [1, 2, 3, 4]
Nesse exemplo, o método append() é utilizado para adicionar o valor 4 ao final da lista.
`````

Usando a concatenação de listas:

`````python

lista = [1, 2, 3]
lista += [4, 5]
print(lista)  # Saída: [1, 2, 3, 4, 5]
`````

Nesse caso, a lista [4, 5] é concatenada com a lista original usando o operador +=.

Alterar elementos em uma lista:

Para alterar um elemento existente em uma lista, você pode simplesmente atribuir um novo valor a um determinado índice:


`````python

lista = [1, 2, 3, 4, 5]
lista[2] = 10
print(lista)  # Saída: [1, 2, 10, 4, 5]
`````

Nesse exemplo, o valor do elemento no índice 2 é alterado para 10.

Excluir elementos de uma lista:

Usando a instrução del:

`````python

lista = [1, 2, 3, 4, 5]
del lista[2]
print(lista)  # Saída: [1, 2, 4, 5]

`````

Nesse exemplo, o elemento no índice 2 é excluído da lista usando a instrução del.

Usando o método remove():

`````python
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista)  # Saída: [1, 2, 4, 5]
`````

Nesse caso, o método remove() é usado para excluir o valor 3 da lista. Ele busca o primeiro elemento com o valor especificado e o remove.

4.  Ordenar listas

 Para ordenar uma lista em Python, você pode usar o método sort() ou a função sorted(). Ambas as opções permitem ordenar os elementos de uma lista em ordem crescente ou decrescente.

Aqui estão exemplos de como ordenar uma lista de diferentes maneiras:

Usando o método sort() para ordenar a lista em ordem crescente:

`````python

lista = [4, 2, 1, 3, 5]
lista.sort()
print(lista)  # Saída: [1, 2, 3, 4, 5]
`````

Nesse exemplo, o método sort() é chamado na lista, e os elementos são ordenados em ordem crescente.

Usando o método sort() para ordenar a lista em ordem decrescente:

`````python
lista = [4, 2, 1, 3, 5]
lista.sort(reverse=True)
print(lista)  # Saída: [5, 4, 3, 2, 1]
`````

Ao passar o argumento reverse=True para o método sort(), a lista é ordenada em ordem decrescente.

Usando a função sorted() para retornar uma nova lista ordenada em ordem crescente:

`````python

lista = [4, 2, 1, 3, 5]
nova_lista = sorted(lista)
print(nova_lista)  # Saída: [1, 2, 3, 4, 5]
`````

Nesse exemplo, a função sorted() é usada para retornar uma nova lista contendo os elementos da lista original, mas ordenados em ordem crescente.

Usando a função sorted() para retornar uma nova lista ordenada em ordem decrescente:

`````python

lista = [4, 2, 1, 3, 5]
nova_lista = sorted(lista, reverse=True)
print(nova_lista)  # Saída: [5, 4, 3, 2, 1]
`````

Ao passar o argumento reverse=True para a função sorted(), a nova lista é retornada em ordem decrescente.

##  Estrutura de Tuplas

1.  Uma tupla em Python é uma estrutura de dados semelhante a uma lista, mas com a diferença fundamental de que ela é imutável, ou seja, seus elementos não podem ser alterados após a tupla ter sido criada. As tuplas são representadas por parênteses () e podem conter elementos de diferentes tipos.

Aqui estão alguns exemplos de criação e uso de tuplas em Python:

`````python

# Criando uma tupla vazia
tupla_vazia = ()

# Criando uma tupla com elementos
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mista = (10, "python", True)

# Acessando elementos da tupla
primeiro_elemento = tupla_numeros[0]
segundo_elemento = tupla_mista[1]

# Tamanho da tupla
tamanho_tupla = len(tupla_numeros)

# Iterando sobre uma tupla
for elemento in tupla_numeros:
    print(elemento)

# Concatenando tuplas
tupla_concatenada = tupla_numeros + tupla_mista
`````
## Estrutura de Dicionários

 1. Introdução a dicionários
    Os dicionários em Python são estruturas de dados que permitem armazenar pares chave-valor. Cada valor é associado a uma chave única, permitindo um acesso rápido e eficiente aos elementos com base em suas chaves.

Aqui está um exemplo básico de como criar e usar dicionários em Python:

`````python

# Criando um dicionário vazio
dicionario_vazio = {}

# Criando um dicionário com elementos
dicionario_pessoas = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores por chave
print(dicionario_pessoas["nome"])  # Saída: João
print(dicionario_pessoas["idade"])  # Saída: 30
print(dicionario_pessoas["cidade"])  # Saída: São Paulo

# Alterando valores
dicionario_pessoas["idade"] = 31
print(dicionario_pessoas["idade"])  # Saída: 31

# Adicionando novos pares chave-valor
dicionario_pessoas["profissao"] = "Engenheiro"
print(dicionario_pessoas["profissao"])  # Saída: Engenheiro

# Verificando a existência de uma chave
if "cidade" in dicionario_pessoas:
    print("A chave 'cidade' existe no dicionário")

# Removendo um par chave-valor
del dicionario_pessoas["idade"]

# Verificando o tamanho do dicionário
tamanho = len(dicionario_pessoas)
print(tamanho)  # Saída: 3


# Verificando a existência de um elemento na tupla
if "python" in tupla_mista:
    print("A tupla contém a palavra 'python'")
   `````
    
2. Funções com dicionários
   
   As funções em Python podem receber dicionários como argumentos e também retornar dicionários como resultados. Isso permite que você manipule e processe os dados contidos nos dicionários de maneira conveniente. Aqui estão alguns exemplos de como usar funções com dicionários:

Passando dicionários como argumentos:
Você pode definir uma função que recebe um dicionário como argumento e realiza operações com os valores contidos nele. Por exemplo:

`````python
def calcular_media(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media

notas_aluno = {"matematica": 8, "ingles": 7, "historia": 9}
media_aluno = calcular_media(notas_aluno)
print(media_aluno)  # Saída: 8.0
`````
Retornando dicionários como resultado:
Uma função também pode retornar um dicionário como resultado, permitindo que você organize e retorne informações processadas. Por exemplo:

`````python

def calcular_estatisticas(numeros):
    estatisticas = {
        "media": sum(numeros) / len(numeros),
        "minimo": min(numeros),
        "maximo": max(numeros)
    }
    return estatisticas

numeros = [1, 2, 3, 4, 5]
estatisticas = calcular_estatisticas(numeros)
print(estatisticas)  # Saída: {'media': 3.0, 'minimo': 1, 'maximo': 5}

`````
Iterando sobre dicionários em uma função:
É possível iterar sobre as chaves e/ou valores de um dicionário dentro de uma função para realizar operações específicas. Por exemplo:

`````python

def imprimir_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(chave, "=", valor)

pessoa = {"nome": "Maria", "idade": 25, "cidade": "São Paulo"}
imprimir_dicionario(pessoa)
# Saída:
# nome = Maria
# idade = 25
# cidade = São Paulo

`````

Modificar um dicionário dentro de uma função:
Lembre-se de que os dicionários são objetos mutáveis, portanto, é possível modificar seus valores dentro de uma função. Por exemplo:

`````python

def adicionar_elemento(dicionario, chave, valor):
    dicionario[chave] = valor

aluno = {"nome": "João", "idade": 20}
adicionar_elemento(aluno, "nota", 8)
print(aluno)  # Saída: {'nome': 'João', 'idade': 20, 'nota': 8}
`````

As funções em Python são blocos de código reutilizáveis que executam uma tarefa específica. Elas permitem organizar o código em partes menores e modulares, facilitando a compreensão, a manutenção e a reutilização do código.

Aqui está a estrutura básica de uma função em Python:

`````python

def nome_da_funcao(argumentos):
    # Corpo da função
    # Código a ser executado

    # Retorno opcional
    return valor_de_retorno
   `````

A palavra-chave def é usada para definir uma função.

nome_da_funcao é o nome que você escolhe para a função. Siga as convenções de nomenclatura do Python ao dar nome às funções.

argumentos são os parâmetros que a função pode receber. Eles são opcionais e podem ser usados para passar informações para a função.

O corpo da função é o bloco de código indentado que contém as instruções a serem executadas.

Opcionalmente, você pode usar a instrução return para retornar um valor da função. Se não houver uma instrução return, a função retorna None implicitamente.

Aqui está um exemplo de uma função simples que soma dois números e retorna o resultado:

`````python

def somar(a, b):
    resultado = a + b
    return resultado

x = 5
y = 3
soma = somar(x, y)
print(soma)  # Saída: 8
`````

1. Parâmetro de funções
   
Os parâmetros em funções Python são as variáveis que recebem valores quando a função é chamada. Eles permitem que você passe informações para a função, para que ela possa executar suas tarefas com base nesses valores.

Existem três tipos principais de parâmetros em funções Python: parâmetros posicionais, parâmetros com valor padrão e parâmetros de palavra-chave. Aqui está uma descrição de cada um deles:

Parâmetros posicionais:
Os parâmetros posicionais são os parâmetros que você especifica na definição da função, na ordem em que são esperados quando a função é chamada. Quando você chama a função, você precisa fornecer argumentos na mesma ordem dos parâmetros definidos. Exemplo:

`````python
def saudacao(nome, mensagem):
    print(f"Olá, {nome}! {mensagem}")

saudacao("João", "Bom dia")
# Saída: Olá, João! Bom dia
`````

Parâmetros com valor padrão:
Os parâmetros com valor padrão são parâmetros que possuem um valor predefinido. Se nenhum valor é fornecido para esses parâmetros ao chamar a função, eles assumem o valor padrão. Isso permite que você chame a função sem especificar todos os argumentos, tornando-os opcionais. Exemplo:

`````python

def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("Maria")
# Saída: Olá, Maria!

saudacao("Pedro", "Oi")
# Saída: Oi, Pedro!
`````

Parâmetros de palavra-chave:
Os parâmetros de palavra-chave são especificados usando o nome do parâmetro ao chamar a função, seguido por um sinal de igual e o valor correspondente. Dessa forma, você pode fornecer argumentos fora de ordem, desde que você os nomeie corretamente. Exemplo:

`````python

def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")

saudacao(mensagem="Olá", nome="João")
# Saída: Olá, João!
`````

2. Retorno de valores
   
   O retorno de valores em funções Python é feito usando a instrução return. Essa instrução permite que a função retorne um valor calculado ou processado de volta para quem a chamou.

Aqui está um exemplo básico de uma função que retorna um valor:

`````python
def somar(a, b):
    resultado = a + b
    return resultado

x = 5
y = 3
soma = somar(x, y)
print(soma)  # Saída: 8
`````

