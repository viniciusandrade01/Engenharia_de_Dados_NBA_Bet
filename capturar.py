import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import os
import psycopg2
import logging
from datetime import datetime

# Configura o logger
logging.basicConfig(filename=f"Log_{datetime.now().strftime('%Y_%m_%d')}.log", 
                    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d__%H%M%S")

conn = psycopg2.connect(
    host = os.getenv("HOST"),
    database = os.getenv("DATABASE"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    port = os.getenv("PORT")
)
logging.info("BD acessado com sucesso!") if conn.status == 1 else logging.error("Falha ao acessar o BD.")

def usando_banco(df: pd.DataFrame):
    # Criação de um cursor para executar comandos SQL
    cur = conn.cursor()
    
    # Defina a instrução SQL para criar a tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS data_nba (
        Rk INT,
        Player VARCHAR(50),
        Pos VARCHAR(50),
        Age INT,
        Tm VARCHAR(50),
        Gg INT,
        Gs INT,
        Mp INT,
        Fg INT,
        Fga INT,
        Fgp INT,
        P3 INT,
        P3a INT,
        P3p INT,
        P2 INT,
        P2a INT,
        P2p INT,
        Efgp INT,
        Ft INT,
        Fta INT,
        Ftp INT,
        Orb INT,
        Drb INT,
        Trb INT,
        Ast INT,
        Stl INT,
        Blk INT,
        Tov INT,
        Pf INT,
        Pts INT
    );
    """
    # Execute a instrução SQL
    cur.execute(create_table_query)

    # Importação dos dados do DataFrame para a tabela no PostgreSQL
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO data_nba (Rk, Player, Pos, Age, Tm, Gg, Gs, Mp, Fg, Fga, Fgp, P3, P3a, P3p, P2, P2a, P2p, Efgp, Ft, Fta, Ftp, Orb, Drb, Trb, Ast, Stl, Blk, Tov, Pf, Pts) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23],row[24], row[25], row[26], row[27], row[28], row[29])
        )

    # Confirma a transação
    conn.commit()
    logging.info("Dados carregados com sucesso!")
    
    # Execute uma consulta para selecionar todos os valores da tabela
    select_query = "SELECT * FROM data_nba;"
    cur.execute(select_query)

    # Recupere os resultados da consulta
    results = cur.fetchall()

    # Exiba os resultados inseridos no Banco de Dados
    for row in results:
        print(row)

    # Fechando o cursor e a conexão
    cur.close()
    conn.close()

while True:
    year = input("Digite o ano desejado (exemplo: 2018): ")
    if not len(year) != 4:
        break

req = rq.get(f'https://www.basketball-reference.com/leagues/NBA_{year}_totals.html')

if req.status_code == 200:
    logging.info('Requisição bem sucedida!')
    content = req.content
else:
    logging.error("Não foi possível acessar à requisição!")
    raise SystemExit("Programa interrompido devido à falha na requisição.")
    
soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')

df = pd.read_html(str(table))[0].fillna('0')

# Pega os indexes, da coluna Rk (1° coluna), que contém valores diferente do tipo numérico
non_numeric = df[~df['Rk'].str.isnumeric()].index

# Remove as linhas que possuem os indexes com valores não numéricos
df = df.drop(index=non_numeric)

# Troque os pontos ("." por 0) da tabela
df = df.applymap(lambda x: str(x).replace(".", '0'))

# Reseta os indexes da tabela
df.reset_index(drop=True, inplace=True)

# Gera um arquivo csv, que irei inserir no PostgreSQL
df.to_csv("Dataset.csv", sep="\t", index=False, encoding = "utf-8")
logging.info("Arquivo tratado gerado com sucesso!!")

# Acessa função para utilizar o Banco de Dados
usando_banco(df)
logging.info("Banco usado!")
logging.info("-------------------------------")