# Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. Os endereços no intervalo de
# 0 à 127 são classe A, de 128 a 191 são classe B, de 192 a 223 são classe C, de 224 à 239 são classe D
# e a partir de 240 são classe E. Faça um algoritmo que leia o primeiro octeto, no formato decimal de um
# endereço IP, e informe a sua classe.

ipv4 = input("Digite o endereço IP versão 4: ")

octet = int(ipv4[:3])

if (octet > 0) and (octet <= 127):
    print("Classe A")
elif (octet >= 128) and (octet <= 191):
    print("Classe B")
elif (octet >= 192) and (octet <= 223):
    print("Classe C")
elif (octet >= 224) and (octet <= 239):
    print("Classe D")
elif (octet >= 240) and (octet <= 255):
    print("Classe E")
else:
    print("O número não é um IPV4!")
