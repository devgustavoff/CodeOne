lista_chamada = ['Gustavo', 'Ricardo', 'Felipe', 'Emanuel'
                 'Laryssa', 'Gaby', 'Ruan', 'Ramom', 'João Miguel'
                 'Rafael']
presenca = []
lista_presenca = []
lista_falta = []
i = 0

while i < len(lista_chamada):
    presenca_aluno = input(lista_chamada[i] + " Esta presente? [S/N]") 
    if presenca_aluno == 'S' or presenca_aluno == 's':
        presenca.append(True)
    elif presenca_aluno == 'N' or presenca_aluno == 'n':
        presenca.append(False)
    i = i +1

j = 0
while j < len(presenca):
    if presenca[j] == True:
        lista_presenca.append(lista_chamada[j])
    elif presenca[j] == False:
        lista_falta.append(lista_chamada[j])
    
    j = j + 1 

# MOSTRA LISTA DE PRESENÇA E LISTA DE FALTAS
# FAZER FUNÇÕES PARA CHAMADA E PARA AS LISTAS
def presencas():
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

def listas(presensa):
    lista_presenca = []
    lista_falta = []
    i = 0 
    while i < len(presenca):
        if presenca[i] == True:
            lista_presenca.append(lista_chamada[i])
        elif presenca[i] == False:
            lista_falta.append(lista_chamada[i])
        i = i + 1 