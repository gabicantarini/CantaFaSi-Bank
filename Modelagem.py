import BancoDados
#Cria a classe pai Pessoa 
class Pessoa:
    def __init__(self, nome, idade, nif):
        self.nome = nome
        self.idade = idade
        self.nif = nif

    def definir_informacoes_Pessoa(self):
        self.nome = input("Digite o seu nome: ")
        self.idade = input("Digite a sua idade: ")
        self.nif = input("Digite o seu nif: ")
        #return nome, idade, nif


        
        
    def exibir_informacoes_Pessoa(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}")

    def definir_idade(self):
        if self.idade >= 18:
            print(f"{self.nome} tem {self.idade} anos e pode ter uma conta no banco.")
        else:
            print(f"{self.nome} tem {self.idade} anos e não pode ter uma conta no banco.")
 
 
#Cria a classe filha AberturaConta, que herda as informações da classe pai
class AberturaConta(Pessoa):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta):
        super().__init__(nome, idade, nif)
        self.login = login #login é igual ao primeiro caracter do nome + nº de conta
        self.senha = senha #Definida pelo utilizador
        self.endereco = endereco 
        self.ordenado = ordenado
        self.conta = conta # nº de conta é incrementado

    # Função para autenticação de usuários
    def autenticar(self):
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        return login, senha
    
    #metodo para exibir informações basicas da conta
    def exibir_informacoes_conta(self):
        print(f"\nNome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}, Endereço: {self.endereco}, Conta Nº: {self.conta}")
        
    def definir_limite(self):        
        if self.ordenado <= 750:
            print(f"{self.nome}, recebe o ordenado de {self.ordenado} e não tem direito a limite de crédito. \n")
        if self.ordenado > 750:
            print(f"{self.nome}, recebe o ordenado de {self.ordenado} e terá o limite de € 500. \n")


# Módulo para gerenciar contas bancárias
class ContaBancaria(AberturaConta):
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta, saldo, historico):#Eliminar o histórico login pré definido
        super().__init__(nome, idade, nif, login, senha, endereco, ordenado, conta)
        self.saldo = 0
        self.historico = []
 
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
 
    def exibir_historico(self):
        for transacao in self.historico:
            print(transacao)


           