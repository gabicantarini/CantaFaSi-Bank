import pandas as pd
class Pessoa:
    def __init__(self, nome, idade, nif):
        self.nome = nome
        self.idade = idade
        self.nif = nif
 
    def exibir_informacoes_Pessoa(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}")
 
class AberturaConta(Pessoa):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta):
        super().__init__(nome, idade, nif)
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.ordenado = float(ordenado)
        self.conta = int(conta)
 
    #def exibir_informacoes_conta(self):
        #print(f"\nNome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}, Endereço: {self.endereco}, Conta Nº: {self.conta}")
 
class ContaBancaria(AberturaConta):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta, saldo):
        super().__init__(nome, idade, nif, login, senha, endereco, ordenado, conta)
        self.saldo = float(saldo)
 
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito: +€{valor}')
 
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Levantamento: -€{valor}')
        else:
            print("Saldo insuficiente.")
 
    def consultar_saldo(self):
        return self.saldo
 
    def atualizar_dados_csv(self):
        dados = ler_dados_csv()
        for i, linha in enumerate(dados):
            if linha['conta'] == str(self.conta):
                dados[i]['saldo'] = str(self.saldo)
                dados[i]['limite'] = '500'
                break
        escrever_dados_csv(dados)
 
def ler_dados_csv():
    return pd.read_csv('Dados.csv', encoding='utf-8').to_dict(orient='records')
 
def escrever_dados_csv(dados):
    df = pd.DataFrame(dados)
    df.to_csv('Dados.csv', index=False, encoding='utf-8')
 
def adicionar_nova_conta():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    nif = input("Digite o NIF: ")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    endereco = input("Digite o endereço: ")
    ordenado = float(input("Digite o ordenado: "))
    conta = str(len(ler_dados_csv()) + 1)
    limite = 500
 
    nova_conta = {
        'nome': nome,
        'idade': idade,
        'nif': nif,
        'login': login,
        'senha': senha,
        'endereco': endereco,
        'ordenado': ordenado,
        'conta': conta,
        'saldo': 0,
        'limite': limite
    }
 
    if int(idade) >= 18:
        print(f"Nova conta adicionada para {nome}. Dados de acesso:\n Numero de conta: {conta}\nLogin: {login}\nSenha: {senha}")
    else:
        print(f"{nome} tem {idade} anos e não pode ter uma conta no banco.\n")
        return main()
       
    if ordenado <= 750:
        print(f"{nome}, recebe o ordenado de {ordenado} e não tem direito a limite de crédito. \n")
        limite = 0
    else:
        print(f"{nome}, recebe o ordenado de {ordenado} e terá o limite de € 500. \n")
 
 
    dados = ler_dados_csv()
    dados.append(nova_conta)
    escrever_dados_csv(dados)
 
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
            print("3. Levantar")
            print("4. Adicionar Nova Conta")
            print("5. Atualizar Dados de Conta")
            print("9. Sair")
 
            escolha = input("Escolha uma opção: ")
 
            for conta in dados:
                if conta['login'] == login_digitado and conta['senha'] == senha_digitada:
                    cliente = ContaBancaria(conta['nome'], conta['idade'], conta['nif'], conta['login'], conta['senha'],
                                    conta['endereco'], conta['ordenado'], conta['conta'], float(conta['saldo']))
                break
 
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