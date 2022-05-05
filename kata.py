def solution(string):
    newList = []
    i = -1
    while len(newList) < len(string):
        newList.append(string[i])
        i = i - 1
    return newList

def solutionMain(string):
    lista = []
    i = -1
    while len(lista) < len(string):
        lista.append(string[i])
        i = i - 1
    return lista

print(solutionMain('drlow'))