import csv

class Pessoa:
    def __init__(self, nome, idade, nif):
        self.nome = nome
        self.idade = idade
        self.nif = nif

    def definir_informacoes_Pessoa(self):
        self.nome = input("Digite o seu nome: ")
        self.idade = input("Digite a sua idade: ")
        self.nif = input("Digite o seu nif: ")

    def exibir_informacoes_Pessoa(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}")

    def definir_idade(self):
        if int(self.idade) >= 18:
            print(f"{self.nome} tem {self.idade} anos e pode ter uma conta no banco.")
        else:
            print(f"{self.nome} tem {self.idade} anos e não pode ter uma conta no banco.")

class AberturaConta(Pessoa):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta):
        super().__init__(nome, idade, nif)
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.ordenado = float(ordenado)
        self.conta = int(conta)

    def autenticar(self):
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        return login, senha

    def exibir_informacoes_conta(self):
        print(f"\nNome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}, Endereço: {self.endereco}, Conta Nº: {self.conta}")

    def definir_limite(self):
        if self.ordenado <= 750:
            print(f"{self.nome}, recebe o ordenado de {self.ordenado} e não tem direito a limite de crédito. \n")
        if self.ordenado > 750:
            print(f"{self.nome}, recebe o ordenado de {self.ordenado} e terá o limite de € 500. \n")

class ContaBancaria(AberturaConta):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta, saldo, historico):
        super().__init__(nome, idade, nif, login, senha, endereco, ordenado, conta)
        self.saldo = float(saldo)
        self.historico = historico

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f'Depósito: +${valor}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f'Saque: -${valor}')
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo

    def atualizar_dados_csv(self):
        dados = ler_dados_csv()
        for linha in dados:
            if linha['conta'] == str(self.conta):
                linha['saldo'] = str(self.saldo)
                linha['limite'] = '500'  # Adicione esta linha se desejar atualizar o limite no CSV
                break
        escrever_dados_csv(dados)

def ler_dados_csv():
    dados = []
    with open('Dados.csv',mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        header = next(leitor)
        for linha in leitor:
            dados.append(dict(zip(header, linha)))
    return dados

def escrever_dados_csv(dados):
    with open('Dados.csv',mode='w', encoding='utf-8', newline='') as arquivo_csv: 
        escritor = csv.writer(arquivo_csv)
        header = dados[0].keys()
        escritor.writerow(header)
        for linha in dados:
            escritor.writerow(linha.values())

def adicionar_nova_conta():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    nif = input("Digite o NIF: ")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    endereco = input("Digite o endereço: ")
    ordenado = float(input("Digite o ordenado: "))
    conta = str(len(ler_dados_csv()) + 1)

    nova_conta = ContaBancaria(nome, idade, nif, login, senha, endereco, ordenado, conta, 0, [])

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
                                    conta['endereco'], conta['ordenado'], conta['conta'], float(conta['saldo']), [])
            break

    if cliente:
        print("Autenticação bem-sucedida!")
        while True:
            print("\nOpções:")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Exibir Histórico")
            print("5. Adicionar Nova Conta")
            print("6. Atualizar Dados de Conta")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print("Saldo atual: $", cliente.consultar_saldo())
            elif escolha == "2":
                valor_deposito = float(input("Digite o valor a depositar: $"))
                cliente.depositar(valor_deposito)
                print("Depósito realizado com sucesso!")
            elif escolha == "3":
                valor_saque = float(input("Digite o valor a sacar: $"))
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
