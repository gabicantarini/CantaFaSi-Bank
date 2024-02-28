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
 
class ContaBancaria(Pessoa):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta, saldo=0):
        super().__init__(nome, idade, nif)
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.ordenado = float(ordenado)
        self.conta = int(conta)
        self.saldo = float(saldo)
 
    def autenticar(self):
        login_digitado, senha_digitada = super().autenticar()
        return login_digitado == self.login and senha_digitada == self.senha
 
    def exibir_informacoes_conta(self):
        print(f"\nNome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}, Endereço: {self.endereco}, Conta Nº: {self.conta}")
 
    def definir_limite(self):
        if self.ordenado <= 750:
            print(f"{self.nome}, recebe o ordenado de {self.ordenado} e não tem direito a limite de crédito.\n")
        elif self.ordenado > 750:
            print(f"{self.nome}, recebe o ordenado de {self.ordenado} e terá o limite de € 500.\n")
 
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito: +€{valor}')
 
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque: -€{valor}')
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