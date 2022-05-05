lista_chamada = ['Gustavo', 'Ricardo', 'Felipe', 'Emanuel',
                 'Laryssa', 'Gaby', 'Ruan', 'Ramom', 'João Miguel',
                 'Rafael']

def presencas(lista_chamada):
    i = 0
    while i < len(lista_chamada):
        presenca = []
        presenca_aluno = input(lista_chamada[i] + " Esta presente? [S/N]")
        if presenca_aluno == 'S' or presenca_aluno == 's':
            presenca.append(True)
        elif presenca_aluno == 'N' or presenca_aluno == 'n':
            presenca.append(False)
        i = i + 1 
    return presenca

def mostra_listas(presenca):
    lista_faltas = []
    lista_presente = []
    i = 0
    print("VER LISTA:")
    print("[1] Lista de Alunos presentes")
    print("[2] Listas de Alunos que faltaram")
    opcao = int(input("Informe a opção: "))
    if opcao == 1:
        while i < len(presenca):
            if presenca == True:
                lista_presente.append(lista_chamada[i])
            i = i + 1
        return lista_presente
    elif opcao == 2:
        while i < len(presenca):
            if presenca == False:
                lista_faltas.append(lista_chamada[i])
            i = i + 1
        return lista_faltas

presencas = presencas(lista_chamada)
print(mostra_listas(presencas))