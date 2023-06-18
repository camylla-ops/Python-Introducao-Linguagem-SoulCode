'''
Como sugestão de prática, indicamos você a criar um novo script python seguindo as orientações a seguir:

Crie uma string contendo o alfabeto com letras maiúsculas separado por espaços.
Percorra e imprima essa string com enumerate.
Substitua os espaços por traço. “-” e imprima para o usuário.
'''

 #criando a string com o alfabeto em letras maiúsculas

alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

# percorrendo e imprimindo a string com enumerate

for indice, letra in enumerate(alfabeto):
    print(indice, letra)
  
# substituindo espaços por traços ("-") e imprimindo para o usuário

print(alfabeto.replace(" ", "-"))
