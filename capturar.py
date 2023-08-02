import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import psycopg2

# Carrega as variáveis de ambiente do arquivo .env
#load_dotenv()

conn = psycopg2.connect(
    host = os.getenv("HOST"),
    database = os.getenv("DATABASE"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD")
)
print("BD acessado com sucesso!") if conn.status == 1 else print("Falha ao acessar o BD.")
#port = os.getenv("PORT")

def usando_banco(df: pd.DataFrame):
    # Criação de um cursor para executar comandos SQL
    cur = conn.cursor()

    # Importação dos dados do DataFrame para a tabela no PostgreSQL
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO Dataset (Rk, Player, Pos, Age, Tm, Gg, Gs, Mp, Fg, Fga, Fgp, P3, P3a, P3p, P2, P2a, P2p, Efgp, Ft, Fta, Ftp, Orb, Drb, Trb, Ast, Stl, Blk, Tov, Pf, Pts) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23],row[24], row[25], row[26], row[27], row[28], row[29])
        )

    # Confirma a transação
    conn.commit()
    print("Dados carregados com sucesso!")

    # Fechando o cursor e a conexão
    cur.close()
    conn.close()

while True:
    year = input("Digite o ano desejado (exemplo: 2018): ")
    if not len(year) != 4:
        break

req = rq.get(f'https://www.basketball-reference.com/leagues/NBA_{year}_totals.html')

if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content
    
soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')

df = pd.read_html(str(table))[0].fillna('')

# Pega os indexes, da coluna Rk (1° coluna), que contém valores diferente do tipo numérico
non_numeric = df[~df['Rk'].str.isnumeric()].index

# Remove as linhas que possuem os indexes com valores não numéricos
df = df.drop(index=non_numeric)

# Reseta os indexes da tabela
df.reset_index(drop=True, inplace=True)
df.to_csv("Dataset.csv", sep="\t", index=False, encoding = "utf-8")
usando_banco(df)
print("Banco usado!")
