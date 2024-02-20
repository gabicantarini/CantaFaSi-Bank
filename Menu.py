menu = """

[1] Depositar
[2] Levantar
[3] Extrato #transferência
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_RETIRADA = 2

while True:
    opcao = input(menu)

    if opcao == "1":
        # Solicita o valor do depósito ao usuário
        valor = float(input("Informe o valor do depósito: "))
        
        # Verifica se o valor do depósito é válido
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}\n'
        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")

    elif opcao == '2':
        # Solicita o valor do saque ao usuário
        valor = float(input("Informe o valor do saque: "))

        # Verifica as condições para realizar o saque
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_RETIRADA

        if excedeu_saldo:
            print("Operação falhou! Não há saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite permitido.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques foi excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor: .2f}\n'
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        # Exibe o extrato e o saldo
        print("\n=============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===============================")

    elif opcao =="4":
        # Encerra o programa
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")
