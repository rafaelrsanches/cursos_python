# Instrução Break

print("Antes do laço")

for item in range(10):
    print(item)

    if item == 6:
        print("A condição 'Break' retornou True")
        break

print("Depois do laço")
