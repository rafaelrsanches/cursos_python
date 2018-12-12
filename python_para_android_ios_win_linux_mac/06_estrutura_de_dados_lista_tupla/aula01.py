# Iterando Listas

list_numbers = [100, 200, 300, 400, 500]

# Iterando a Lista

for item in list_numbers:
    print(item)

# Função Range/Length

for item in range(len(list_numbers)):
    list_numbers[item] += 1000

print(list_numbers)

# Função Enumerate

for idx, item in enumerate(list_numbers):
    list_numbers[idx] += 1000

print(list_numbers)
