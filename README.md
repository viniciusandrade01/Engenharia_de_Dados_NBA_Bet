# Web-Scraping-Datasets-Esportivo
É notório que processos ETL sempre são vistos no escopo da Engenharia de Dados. 
Dessa forma, visando fixar, e exercitar, o conteúdo relacionado, farei uma extração de dados da fonte https://www.sports-reference.com/ - que por sinal, é uma fonte rica em informação, abordando dados de diversos esportes e ligas -, usando web scraping, tratarei os dados obtidos - removendo dados 'sujos' e gerando uma 'padronização' - e armazenarei em um arquivo do formato csv, para posteriormente inserir no Banco de Dados PostgreSQL. Abaixo, os passos:

Etapas:

1) Importação das bibliotecas a serem utilizadas, tais como:
    .Biblioteca Pandas: para manipular os dados em forma de tabela.
              Requests: para execução de requisições HTTP;
         BeautifulSoup: para extração de dados em arquivos HTML e XML;
                    Os: para 'puxar'/acessar às variáveis de ambiente, oriundas do arquivo .env
              Psycopg2: para manipular e usar o Banco de Dados, nesse caso, PostgreSQL.

2) Coleta do ano para ser utilizado como referência para obtenção dos dados da temporada da NBA - que é o objeto de estudo.
    .Ano contendo 4 dígitos

3) Requisição, já inserindo o ano desejado.
    .Validando se o status da requisição é 200 - que indica que foi bem sucedida

4) Usando a Biblioteca BeautifulSoup, extraímos a tabela e atribuímos em uma variável,
posterior a isso, acessei o elemento da página desejado via método find

5) Tendo o código html da tabela, usei a Biblioteca Pandas para facilitar no manuseio e tratamento dos dados - pois o pandas carrega os dados em dataframe -, via método read_html.
    .A tabela já vem previamente ajustada, ajustes pontuais foram realizados, sendo um deles a configuração para que os valores 'NaN' retornem ''

6) Depois dos tratamentos necessários, gerei um arquivo .csv

7) Com todos os tratamentos de dados já finalizados, agora inserirei o conteúdo do csv no Banco de Dados configurado, executando os scripts necessários
    .Os acessos a ele, ao banco, foram configurados usando variáveis de ambiente, arquivo .env (um conteúdo exemplo estará no final desse arquivo)
    .Além das configurações de acesso, faremos duas execuções de scripts no sql
        1°) A partir da leitura do conteúdo do arquivo datanba.sql, para criação da tabela
        2°) Dentro do próprio código python (capturar.py), fazendo uso de um loop.

8) Prontinho, os dados foram inseridos com sucesso ao Banco de Dados configurado, para facilitar a visualização dos dados inseridos, criei um loop for para 'imprimir' todo o conteúdo inserido no banco.

RESUMO:
Nesse desenvolvimento em Python, fiz uso da biblioteca Pandas - para lidar com dados em formato tabular -, biblioteca Requests - para realizar solicitações HTTP e obter dados online -, biblioteca BeautifulSoup - que me auxiliou na extração de informações de HTML/XML -, biblioteca os - para acessar variáveis de ambiente de forma segura -, e a biblioteca Psycopg2 - para tratar com banco de dados PostgreSQL, que é bem amigável e facilita todas as interações, desde a conexão até operações como consultas e inserções -.

Obs.: Usei variáveis de ambiente para acessar o banco, então, para garantir a funcionalidade do código, será necessário informá-las, segue a estrutura que utilizei para armazenar os dados:

Nome do arquivo: .env

DATABASE="XXXXXXXXX"
HOST="XXXXXXXXXXXXX"
USER="XXXXXXXXXXXXX"
PASSWORD="XXXXXXXXX"
PORT="XXXXXXXXXXXXX"