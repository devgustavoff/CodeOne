lista = [22, 30, 17, 77, 100, 36, 9, 1, 26, 90]
lista.sort()
maior = 0

for item in lista:
    if item > maior:
        maior = item

i = 1
for item in lista:
    if item < lista[i]:
        menor = item

print('Maior item da lista -> ', maior)
print('Menor item da lista -> ',menor)
print(lista)