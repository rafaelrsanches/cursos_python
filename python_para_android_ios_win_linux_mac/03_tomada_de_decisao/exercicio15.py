# Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.

char = str(input("Digite um caractere: ")).strip()

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if char in vowel:
    print("O caractere '%s' é uma vogal!" % char)
else:
    print("O caractere '%s' não é uma vogal!" % char)
