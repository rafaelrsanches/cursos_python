# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma
# letra. Caso a letra seja o "q" finalize a aplicação. Do contrário, imprima novamente a mesma frase até
# que o caractere "q" seja enviado:

char = None
while char != 'q':
    print("estou em looping")
    char = str(input("Digite uma letra: ")).strip()
