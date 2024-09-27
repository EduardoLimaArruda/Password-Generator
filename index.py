import random

letras = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao Criador de Senhas!")
nr_letras = int(input("Quantas letras você quer na sua senha?\n"))
nr_numeros = int(input(f"Quantos números você quer?\n"))
nr_simbolos = int(input(f"Quantos simbolos você quer?\n"))

Password = []

for Char in range(0, nr_letras):
    Password += random.choice(letras)

for Char in range(0, nr_numeros):
    Password += random.choice(numeros)

for Char in range(0, nr_simbolos):
    Password += random.choice(simbolos)

random.shuffle(Password)

PL = ""
for Char in Password:
    PL += Char

print(f"\nSua nova senha é {PL}\n")

Exit = input("Aperte Enter para fechar!")