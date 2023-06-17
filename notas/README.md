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

1. Operadores de relação e condição

