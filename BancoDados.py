import csv
import pandas as pd


# Função para adicionar novas linhas ao arquivo CSV
def adicionar_linhas(caminho_arquivo_csv, novas_linhas):
    with open(caminho_arquivo_csv, mode='a', encoding='utf-8', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(novas_linhas)

# Função para ler e exibir dados do arquivo CSV usando pandas
def ler_e_exibir_dados(caminho_arquivo_csv):
    dados_df = pd.read_csv(caminho_arquivo_csv, encoding='utf-8')
    print(dados_df)

# Caminho do arquivo CSV
caminho_arquivo_csv = "Dados.csv"

# Dados das novas linhas
novas_linhas = [
    ["Maria Oliveira", 35, 123456789, "M0004", "moliveira", "Porto", 2500, 4, 700, 500],
    ["João Pereira", 30, 987654321, "J0005", "jpereira", "Lisboa", 1800, 5, 400, 500]
]

# Adicionando novas linhas ao arquivo CSV
adicionar_linhas(caminho_arquivo_csv, novas_linhas)

# Lendo e exibindo os dados do arquivo CSV
ler_e_exibir_dados(caminho_arquivo_csv)
