"""
Arquivo para gerar dados fake para testes


Explicação do Script

- Importações: Bibliotecas pandas e random.
- Número de Linhas: 1000 linhas.
- Lista de Ruas: 40 ruas.
- Lista de Sexos: M e F.
- Geração de Dados: 1000 linhas de dados aleatórios. 
- DataFrame: DataFrame do Pandas com os dados gerados.
- Arquivo CSV: Arquivo CSV com os dados gerados.
- Mensagem de Sucesso: Mensagem indicando que o arquivo CSV foi gerado com sucesso.

Como Executar o Script
- Execute o script no terminal ou no ambiente de desenvolvimento Python.

    python dados_fake.py
"""

import pandas as pd
import random

# Número de linhas
num_linhas = 10000
# Lista de ruas
ruas = [
    "RUA A", "RUA B", "RUA C", "RUA D", "RUA E", "RUA F",
    "RUA G", "RUA H", "RUA I", "RUA J", "RUA K", "RUA L",
    "RUA M", "RUA N", "RUA O", "RUA P", "RUA Q", "RUA R",
    "RUA S", "RUA T", "RUA U", "RUA V", "RUA W", "RUA X"
]
# Lista de sexos
sexos = ["M", "F"]

# Gerar dados
def gerar_dados(ruas, sexos):
    data = []
    for _ in range(num_linhas):
        rua = random.choice(ruas)
        num = random.randint(1, 1000)
        idd = random.randint(0, 100)
        sexo = random.choice(sexos)
        data.append([rua, num, idd, sexo])
    # Criar DataFrame
    df = pd.DataFrame(data, columns=["RUA", "NUM", "IDD", "SEXO"])
    # Salvar em arquivo CSV
    df.to_csv("fake.csv", index=False, encoding='utf-8', sep=',')
    print("Arquivo CSV gerado com sucesso!")
    return df

# Executar a função
if __name__ == "__main__":
    gerar_dados(ruas, sexos)
