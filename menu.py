def menu():
    print("Menu de operação")
    print("[a] Mostrar saldo")
    print("[b] Efetuar deposito")
    print("[c] Efetuar saque]")
    print("[d] Finalizar")
    opcao = input("Informe a opção: ")
    return opcao

encerrar_programa = False
saldo = 0
valor = 0

while encerrar_programa == False:
    
    opcao_menu = menu()
    
    if opcao_menu == 'a':
        print("Seu saldo é:", saldo)
    elif opcao_menu == 'b':
        valor = float(input("Informe o valor para depositado: "))
        saldo = saldo + valor
    elif opcao_menu == 'c':
        valor = float(input('Informe o valor a retirar: '))
        if valor > saldo:
            print("Saque não permitido, saldo insuficiente")
        else:
            saldo = saldo - valor
        print("Saque efetuado")
    elif opcao_menu == 'd':
        encerrar_programa = True
        print("PROGRAMA FINALIZADO!")
    else:
        print("Opção invalida, tente novamente.")

