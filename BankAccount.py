# Módulo para gerenciar contas bancárias
class ContaBancaria:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
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
 
 
# Função para autenticação de usuários
def autenticar():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    return nome, senha
 
 
# Função principal
def main():
    # Simulação de banco com um cliente
    cliente = ContaBancaria("Usuario1", "senha123")
 
    # Autenticação
    nome_digitado, senha_digitada = autenticar()
 
    if nome_digitado == cliente.nome and senha_digitada == cliente.senha:
        print("Autenticação bem-sucedida!")
        while True:
            # Menu de opções
            print("\nOpções:")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Exibir Histórico") #Talvez seja melhor ter função de transferir dinheiro em vez de exibir histórico
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
                print("\nHistórico de Transações:")
                cliente.exibir_historico()
            elif escolha == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Autenticação falhou. Verifique seu nome e senha.")
 
 
if __name__ == "__main__":
    main()