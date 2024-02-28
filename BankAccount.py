from Modelagem import ContaBancaria, ler_dados_csv, escrever_dados_csv
 
def adicionar_nova_conta():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    nif = input("Digite o NIF: ")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    endereco = input("Digite o endereço: ")
    ordenado = float(input("Digite o ordenado: "))
    conta = str(len(ler_dados_csv()) + 1)
 
    nova_conta = ContaBancaria(nome, idade, nif, login, senha, endereco, ordenado, conta, 0)
 
    dados = ler_dados_csv()
    dados.append({
        'nome': nova_conta.nome,
        'idade': nova_conta.idade,
        'nif': nova_conta.nif,
        'login': nova_conta.login,
        'senha': nova_conta.senha,
        'endereco': nova_conta.endereco,
        'ordenado': str(nova_conta.ordenado),
        'conta': nova_conta.conta,
        'saldo': '0',
        'limite': '500'
    })
    escrever_dados_csv(dados)
    print(f"Nova conta para {nome} foi adicionada com sucesso!")
 
def atualizar_dados_conta():
    num_conta = input("Digite o número da conta que deseja atualizar: ")
    dados = ler_dados_csv()
    conta_existente = next((conta for conta in dados if conta['conta'] == num_conta), None)
 
    if conta_existente:
        print("\nInformações atuais da conta:")
        for chave, valor in conta_existente.items():
            print(f"{chave.capitalize()}: {valor}")
 
        opcoes_atualizacao = ['nome', 'idade', 'nif', 'login', 'senha', 'endereco', 'ordenado']
        for opcao in opcoes_atualizacao:
            novo_valor = input(f"Digite o novo valor para {opcao.capitalize()} (deixe em branco para manter o valor atual): ")
            if novo_valor:
                conta_existente[opcao] = novo_valor
 
        escrever_dados_csv(dados)
        print(f"Conta {num_conta} atualizada com sucesso!")
    else:
        print(f"Conta {num_conta} não encontrada.")
 
def autenticar():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    return login, senha
 
def main():
    dados = ler_dados_csv()
    login_digitado, senha_digitada = autenticar()
 
    cliente = None
    for conta in dados:
        if conta['login'] == login_digitado and conta['senha'] == senha_digitada:
            cliente = ContaBancaria(conta['nome'], conta['idade'], conta['nif'], conta['login'], conta['senha'],
                                    conta['endereco'], conta['ordenado'], conta['conta'], float(conta['saldo']))
            break
 
    if cliente:
        print("Autenticação bem-sucedida!")
        while True:
            print("\nOpções:")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Adicionar Nova Conta")
            print("5. Atualizar Dados de Conta")
            print("9. Sair")
 
            escolha = input("Escolha uma opção: ")
 
            if escolha == "1":
                print("Saldo atual: €", cliente.consultar_saldo())
            elif escolha == "2":
                valor_deposito = float(input("Digite o valor a depositar: €"))
                cliente.depositar(valor_deposito)
                print("Depósito realizado com sucesso!")
            elif escolha == "3":
                valor_saque = float(input("Digite o valor a sacar: €"))
                cliente.sacar(valor_saque)
            elif escolha == "4":
                adicionar_nova_conta()
            elif escolha == "5":
                atualizar_dados_conta()
            elif escolha == "9":
                cliente.atualizar_dados_csv()
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
 
    else:
        print("Autenticação falhou. Verifique seu nome e senha.")
 
if __name__ == "__main__":
    main()