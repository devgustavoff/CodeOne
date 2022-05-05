
def obter_numeros(lista = []):
    while len(lista) < 10:
        num = int(input())
        lista.append(num)
    return lista

lista = []
print(obter_numeros(lista))
