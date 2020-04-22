# -*- coding: utf-8 -*-
# Comentários
print("Olá mundo")

# Outro comentário
print("nova linha")

"""
Comentários 
de muitas 
linhas
"""
print("mensagem")
print(2 + 2)

# variáveis
var1 = 1
var2 = 1.1
var3 = "String"
var4 = True # Verdadeiro
var5 = False # Falso

# Operadores lógicos
"""
=   -> atribuição
and -> Duas condições sejam verdadeiras
or  -> Pelo menos uma condição seja verdadeira
not -> Inverte o valor
"""

# Operadores relacionais
"""
== -> Igual
!= -> Diferente
>  -> Maior
<  -> Menor
>= -> Maior ou igual
<= -> Menor ou igual
"""

# Comandos condicional - if
"""
Realiza testes condicionais
Executa um bloco SE uma determinada condição for atendida
Avalia se condição é verdadeira ou não
"""
x = 1
y = 2
if x > y:
	print("x é maior que y")
if y > x:
	print("y é maior que x")

# Comandos condicional - else
"""
É executado caso a condição do comando if não seja atendida
"""
a = 1
b = 2

if x > y:
	print("X é maior que Y")
else:
	print("X não é menor que y")

# Comandos condicional - elif
"""
Caso haja necessidade de mais condições entre o if e o else
"""
if x == y:
	print("Números iguais")
elif y > x:
	print("y maior que x")
else:
	print("Números diferentes")

# Laços de repetição - while(Enquanto)
c = 1
while c < 10:
	print(c)
	c += 3

# Laços de repetição - for
lista1 = [1,2,3,4,5]
lista2 = ["olá", "mundo", "!"]
lista3 = [0, "olá", "biscoito", "bolacha", 9.99, True]

for i in lista1:
	print(i)

# Laços de repetição - range
for i in range(10,20,2):
	print(i)