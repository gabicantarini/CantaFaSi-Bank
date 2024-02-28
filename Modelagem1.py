import pandas as pd


def ler_dados():
        return pd.read_csv('Dados.csv', encoding='utf-8').to_dict(orient='records')

def escrever_dados(dados):
        df = pd.DataFrame(dados)
        df.to_csv('Dados.csv', index=False, encoding='utf-8')

class Pessoa:
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta):
        self.nome = nome
        self.idade = idade
        self.nif = nif
        self.login = login
        self.senha = senha
        self.endereco = endereco
        self.ordenado = float(ordenado)
        self.conta = int(conta)

def adicionar_nova_conta():
    dados = ler_dados()

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    nif = input("Digite seu NIF: ")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    endereco = input("Digite seu endereço: ")
    ordenado = float(input("Digite seu ordenado: "))
    conta = str(len(ler_dados()) + 1)
    limite = 500


    nova_conta = Pessoa(nome, idade, nif, login, senha, endereco, ordenado, conta)
    
    
    dados.append({
        'nome': nova_conta.nome,
        'idade': nova_conta.idade,
        'nif': nova_conta.nif,
        'login': nova_conta.login,
        'senha': nova_conta.senha,
        'endereco': nova_conta.endereco,
        'ordenado': nova_conta.ordenado,
        'conta': nova_conta.conta,
        'saldo': 0,
        'limite': limite
    })

    if int(idade) >= 18:
        print(f"Nova conta adicionada para {nome}. Dados de acesso:\nNumero de conta: {conta}\nLogin: {login}\nSenha: {senha}")
    else:
        raise ValueError("Idade abaixo de 18 anos. Não é possível criar uma conta.")
        
    if ordenado <= 750:
        print(f"{nome}, recebe o ordenado de {ordenado} e não tem direito a limite de crédito. \n")
        limite = 0
    else:
        print(f"{nome}, recebe o ordenado de {ordenado} e terá o limite de € 500. \n")
    
    escrever_dados(dados)
    print("Conta criada com sucesso!")

class ContaBancaria(Pessoa):
    
    def __init__(self, nome, idade, nif, login, senha, endereco, ordenado, conta, saldo):
        super().__init__(nome, idade, nif, login, senha, endereco, ordenado, conta)
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.atualizar_saldo()
            print(f"Depósito realizado com sucesso: +€{valor} \nSaldo Atual: € {self.saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor): 
        if valor <= self.saldo:
            self.saldo -= valor
            self.atualizar_saldo()
            print(f"Levantamento realizado com sucesso: +€{valor} \nSaldo Atual: € {self.saldo}")
        else:
            print("Valor de levantamento inválido ou saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo

    def atualizar_dados(self):
        num_conta = int(input("Digite o número da conta que deseja atualizar: "))
        dados = ler_dados()
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

            escrever_dados(dados)
            print(f"Conta {num_conta} atualizada com sucesso!")
        else:
            print(f"Conta {num_conta} não encontrada.")

    def atualizar_saldo(self):
        dados = pd.read_csv('Dados.csv')
        index = dados[dados['login'] == self.login].index[0]
        dados.at[index, 'saldo'] = self.saldo
        dados.to_csv('Dados.csv', index=False)


