cardapio = ['chees burguer', 'pizza calabresa', 'smash burguer']
bebida = ['coca cola', 'pepis',  'cerveja']
i = 1
for item in cardapio:
    print(i, item)
    i = i + 1
opcao = int(input("Qual seu pedido: "))

if opcao == 1:
    print("Seu pedido foi um " + cardapio[0])
elif opcao == 2:
    print("Seu pedido foi um " + cardapio[1])
elif opcao == 3:
    print("Seu pedido foi um " + cardapio[2])

opcao2 = input("Gostaria de beber algo: ")
if opcao2 == 'S' or opcao2 == 's':
    i = 1
    for item in bebida:
        print(i, item)
        i = i + 1
    opcao2 = int(input("Qual a bebida? "))
    if opcao2 == 1:
        print("Sua bebida é " + bebida[0])
    elif opcao2 == 2:
        print("Sua bebida é " + bebida[1])
    elif opcao2 == 3:
        print("Sua bebida é " + bebida[2])
else:
    print("Não pediu bebida")