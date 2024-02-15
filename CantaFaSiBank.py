from Modelagem import *

# Função principal
def main():
    # Simulação de banco com um cliente
    cliente = ContaBancaria("User1", 25, "25 8369 147", "log", "123", "Ruax", 850, "1258-5", 0, []) 

    # Autenticação
    login_digitado, senha_digitada = cliente.autenticar()
 
    if login_digitado == cliente.login and senha_digitada == cliente.senha:
        print("Autenticação bem-sucedida!")
        while True:
            # Menu de opções
            print("\nOpções:")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Exibir Histórico")
            print("0. Sair")
 
            escolha = input("Escolha uma opção: ")
 
            if escolha == "1":
                print("Saldo atual: $", cliente.consultar_saldo())
            elif escolha == "2":
                valor = float(input("Digite o valor a depositar: $"))
                cliente.depositar(valor) 
                print(f"Depósito no valor de {valor} realizado com sucesso!")
            elif escolha == "3":
                valor = float(input("Digite o valor a levantar: $"))
                cliente.sacar(valor)
            elif escolha == "4":
                print("\nHistórico de Transações:")
                cliente.exibir_historico()
            elif escolha == "0":
                print(f"Adeus, {cliente.nome}! Até a próxima.")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Autenticação falhou. Verifique seu nome e senha.")
 
 
if __name__ == "__main__":
    main()

# Exemplo de cadastro
#pessoa1 = Modelagem.AberturaConta("Gabriela Canta", 21, "222 222 222", "Rua ABC, 123", 1235-9)
#pessoa1.AberturaConta.exibir_informacoes_conta()
# pessoa1.definir_limite(300)
# pessoa1.definir_idade()
# pessoa1.realizar_deposito(1000)
# pessoa1.solicitar_cartao_credito()

"""
# Instância da classe Pai (Pessoa)
pessoa2 = Pessoa.exibir_informacoes_Pessoa("Cecília Canta", 20, "333 333 333")
pessoa2.Pessoa.exibir_informacoes_Pessoa()
# pessoa2.definir_limite(500)

# Instância da classe Filha (AberturaConta)
pessoa2.Pessoa = AberturaConta("Cecília Canta", 20, "333 333 333", "Rua XYZ, 456", 1234)
pessoa2.AberturaConta.exibir_informacoes_conta()

# Instância da classe Filha (AberturaConta)
pessoa3 = AberturaConta("Leandro Canta", 23, "444 444 444", "Rua XYZ, 456", 1456)
pessoa3.AberturaConta.exibir_informacoes_conta()
# pessoa3.realizar_deposito(1500)
# pessoa3.solicitar_cartao_credito()

# Alterando valores dos atributos
pessoa1.Pessoa.nome = "Gabriela I Cantarini"
pessoa2.AberturaConta.endereco = "Avenida Principal, 789"

# Exibindo informações atualizadas
print("\nInformações após alterações:")
pessoa1.Pessoa.exibir_informacoes_Pessoa()
pessoa2.Pessoa.exibir_informacoes_Pessoa()
"""