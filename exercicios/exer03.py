chamada = ['Gustavo', 'Ricardo', 'Rafael', 'Emanuel', 'Filipe', 
           'Alice', 'Laryssa', 'Jão Miguel', 'Bolsonaro', 'Lula']

def chamada_alunos(chamada):
    alunos_presentes = []
    alunos_faltantes = []
    i = 0
    while i < len(chamada):
        esta_presente = input(chamada[i] + ' Esta presente? [S/N]')
        if esta_presente == 'S' or esta_presente == 's':
            alunos_presentes.append(chamada[i])
        elif esta_presente == 'N' or esta_presente == 'n':
            alunos_faltantes.append(chamada[i])
        i = i + 1
    encerrar = False
    while encerrar == False:
        print('Mostra lista: ')
        print('[1]Presentes')
        print('[2]Faltantes')
        opcao = int(input('Informe a opção: '))
        if opcao == 1:
            print(alunos_presentes)
        elif opcao == 2:
            print(alunos_faltantes)
        else:
            print('Opção não Disponivel!')
        opcao_2 = input('Deseja encerrar o programa: ')
        if opcao_2 == 'S' or opcao_2 == 's':
            encerrar = True
        else:
            encerrar = False
    return None
chamada_alunos(chamada)