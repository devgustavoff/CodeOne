lista = ['Dia', 'Mes', 'Ano']
data_nascimento = []

for item in lista:
    resposta_usr = int(input(item + ' que você nasceu: '))
    data_nascimento.append(resposta_usr)

idade = 2022 - data_nascimento[2]
print('Sua idade é: {}'.format(idade))