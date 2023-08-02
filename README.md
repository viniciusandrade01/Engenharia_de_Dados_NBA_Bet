# Web-Scraping-Datasets-Esportivo
É notório que ETL é sempre visto na Engenharia de Dados. 
Dessa forma, visando fixar, e exercitar, o conteúdo relacionado, farei uma extração de dados da fonte https://www.sports-reference.com/  - que por sinal, é uma fonte rica em informação, abordando dados de diversos esportes e ligas -, usando web scraping, tratarei os dados obtidos e armazenarei em um arquivo do formato csv.

Etapas:

1) Importação das bibliotecas a serem utilizadas, tais como:
    .Biblioteca Pandas: para manipular os dados em forma de tabela.
              Requests: para execução de requisições HTTP;
         BeautifulSoup: para extração de dados em arquivos HTML e XML;

2) Coleta do ano para ser utilizado como referência para obtenção dos dados da temporada da NBA - que é o objeto de estudo.
    .Ano contendo 4 dígitos

3) Requisição, já inserindo o ano desejado.
    .Validando se o status da requisição é 200 - que indica que foi bem sucedida

4) Usando a Biblioteca BeautifulSoup, extraímos a tabela e atribuímos em uma variável,
posterior a isso, acessei o elemento da página desejado via método find

5) Tendo o código html da tabela, usei a Biblioteca Pandas para facilitar no manuseio e tratamento dos dados - pois o pandas carrega os dados em dataframe -, via método read_html.
    .A tabela já vem previamente ajustada, ajustes pontuais foram realizados, sendo um deles a configuração para que os valores 'NaN' retornem ''

6) Depois dos tratamentos necessários, gerei um arquivo .csv

7) Com tudo já praticamente finalizado, agora inserirei o conteúdo do csv no Banco de Dados configurado.

RESUMO:
Foi utilizada a biblioteca requests - para executar requisições GET e obter o código HTML das páginas que queremos -, depois a BeautifulSoup - para extrair os dados que queremos destas páginas - e a Pandas - salvaremos esses dados em um Data Frame.