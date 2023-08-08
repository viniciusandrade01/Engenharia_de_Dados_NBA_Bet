# Engenharia_de_Dados_NBA_Bet
É notório que processos ETL sempre são vistos no escopo da Engenharia de Dados. 
Dessa forma, visando fixar, exercitar e entender o conteúdo relacionado:
1°) fiz uma extração de dados da fonte https://www.sports-reference.com/ - que por sinal, é uma fonte rica em informação, abordando dados de diversos esportes e ligas -, usando web scraping;
2°) tratei os dados obtidos - limpando os dados e gerando uma padronização;
3°) armazenei em um arquivo do formato csv e inseri no Banco de Dados PostgreSQL.

Etapas:

1) Importação das bibliotecas a serem utilizadas, tais como: Pandas - para manipular os dados em forma de tabela -, Requests - para execução de requisições HTTP -, BeautifulSoup - para extração de dados em arquivos HTML e XML -, Os - para 'puxar'/acessar às variáveis de ambiente, oriundas do arquivo .env - e Psycopg2 - para manipular e usar o Banco de Dados, nesse caso, PostgreSQL -.

2) Coleta do ano para ser utilizado como referência para obtenção dos dados da temporada da NBA - que é o objeto de estudo.
    .Ano contendo 4 dígitos e com validação

3) Requisição, já inserindo o ano desejado.
    .Validando se o status da requisição é 200 - que indica que foi bem sucedida

4) Usando a Biblioteca BeautifulSoup, extraí a tabela e atribuí à variável,
posterior a isso, acessei o elemento da página desejado via método find

5) Tendo o código html da tabela, usei a Biblioteca Pandas para facilitar o manuseio e tratamento dos dados - pois o pandas carrega os dados em dataframe -, via método read_html.
    .A tabela já vem previamente ajustada, ajustes pontuais foram realizados, sendo um deles a configuração para que os valores 'NaN' retornem ''

6) Depois dos tratamentos necessários, gerei um arquivo .csv

7) Com todos os tratamentos de dados já finalizados, agora inserirei o conteúdo do csv no Banco de Dados configurado, executando os scripts necessários
    .Os acessos a ele, ao banco, foram configurados usando variáveis de ambiente, arquivo .env (um conteúdo exemplo estará no final desse arquivo)
    .Além das configurações de acesso, fiz duas execuções de scripts sql
        1°) A partir da leitura do conteúdo do arquivo datanba.sql, para criação da tabela
        2°) Dentro do próprio código python (capturar.py), fazendo uso de um loop para inserir no banco.

8) Prontinho, os dados foram inseridos com sucesso ao Banco de Dados configurado, para facilitar a visualização dos dados inseridos, criei um loop for para 'imprimir' todo o conteúdo inserido no banco.

RESUMO:
Nesse desenvolvimento em Linguagem de Programação Python, fiz uso da biblioteca Pandas, Requests, BeautifulSoup, Os e Psycopg2. Além dessas tecnologias, fiz uso do Banco de Dados PostgreSQL.

------------------------------------------------------------------------------------------------
Obs.: Usei variáveis de ambiente para acessar o banco, então, para garantir a funcionalidade do código, será necessário informá-las, segue a estrutura que utilizei para armazenar os dados:

Nome do arquivo: .env

DATABASE="XXXXXXXXX"
HOST="XXXXXXXXXXXXX"
USER="XXXXXXXXXXXXX"
PASSWORD="XXXXXXXXX"
PORT="XXXXXXXXXXXXX"