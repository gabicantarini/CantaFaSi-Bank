import pandas as pd
from Modelagem1 import Pessoa, ContaBancaria, ler_dados, escrever_dados, adicionar_nova_conta


def main():
    print("Banco CantaFaSi")
    print("1. Criar nova conta.")
    print("2. Entrar.")
    print("9. Sair.")
    escolha1 = int(input("Escolha uma opção: "))

    

    if (escolha1 == 1):
        try:
            adicionar_nova_conta()
            main()
        except ValueError as e: 
            print(e)
            main()
            
    
    elif (escolha1 == 2):
        login_digitado = input("Digite seu login: ")
        senha_digitada = input("Digite sua senha: ")
        dados = ler_dados()
        cliente = []

        for conta in dados:
            if conta['login'] == login_digitado and conta ['senha'] == senha_digitada:
                    cliente = ContaBancaria(conta['nome'], conta['idade'], conta['nif'], conta['login'], 
                                            conta['senha'],conta['endereco'], conta['ordenado'], 
                                            conta['conta'], float(conta['saldo']))
                    break
        if cliente:
            print("Autenticação bem-sucedida!")
            while True:
                print("\nOpções:")
                print("1. Consultar Saldo")
                print("2. Depositar")
                print("3. Levantar")
                print("4. Atualizar Dados de Conta")
                print("9. Sair")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print("\nSaldo atual: €", cliente.consultar_saldo())

                elif escolha == "2":
                    valor_deposito = float(input("Digite o valor a depositar: €"))
                    cliente.depositar(valor_deposito)

                elif escolha == "3":
                    valor_saque = float(input("Digite o valor a levantar: €"))
                    cliente.sacar(valor_saque)
                    
                elif escolha == "4":
                    cliente.atualizar_dados()

                elif escolha == "9":
                    print("Obrigado pela sua preferência.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            
        else:
            print("Autenticação falhou. Verifique seu nome e senha.")
            main()

    elif (escolha1 == 9):
        print("Obrigado pela sua preferência.")
        exit()

    else:
        print("Opção inválida. Tente novamente.")
        main()

main()