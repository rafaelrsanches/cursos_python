# Instrução Continue

print()
print("Antes do laço")

i = 0
while i < 10:
    i += 1

    if i % 2 == 0:
        continue
    if i > 5:
        break

    print(i)
else:
    print("Else")

print("Depois do laço")
print()
