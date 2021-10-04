# D3 Challenge


## Metodologia

O primeiro passo foi obter o número total de casos do primeiro registro de covid-19.
Esse primeiro registro serve de base para predição dos próximos casos que discutiremos a seguir.
O próximo passo, é, a partir do primeiro registro, obter a somatória dos casos por dia até o valor de entrada do usuário, sendo D o número de dias informado.
O algoritmo calcula a diferença entre o próximo dia e seu dia anterior ao longo de 15 dias, obtendo uma porcentagem do aumento de casos nesse período quinzenal, considerando o período de incubação de acordo com a Organização Mundial da Saúde (OMS), tendo a Covid-19 um intervalo que varia de 1 a 14 dias.
Após o processo de obtenção da taxa de aumento de casos, é utilizada a informação do número de dias informado pelo usuário para prever a partir do valor do primeiro registro, quantos casos poderão ser registrados para o seguinte dia até o dia D, sendo D o parâmetro de dias informado pelo usuário.


## Fontes

| Fontes | links |
| ------ | ------ |
| Período de incubação do virus | [https://portal.fiocruz.br/pergunta/qual-e-o-tempo-de-incubacao-do-novo-coronavirus] |
| Our World in Data GitHub Repo |[https://github.com/owid/covid-19-data] |
| Our World in Data | [https://ourworldindata.org/explorers/coronavirus-data-explorer?zoomToSelection=true&time=2020-03-01..latest&country=USA~GBR~CAN~DEU~ITA~IND&region=World&pickerMetric=location&pickerSort=asc&Interval=7-day+rolling+average&Align+outbreaks=false&Relative+to+Population=true&Metric=Confirmed+cases]|

## Tech's e Libs

Um pouco sobre tudo oque foi utilizado para o desenvolvimento:

- [Docker] - Para conteinerização da aplicação!
- [Python] - Uma linguagem de sintaxe simples mas poderosa.
- [Datetime] - É uma biblioteca nativa do python para manipulação de datas.
- [Pandas] - Essa é uma das mais famosas libs do python e foi criada para manipulação e análise de dados. "Se o python fosse o Manchester United, a lib Pandas seria o Cristiano Ronaldo" - Benjamim Francisco.

## Instalação e Inicialização

Como utilizar a aplicação se você utiliza docker?

```sh
Clone este repositório e siga para a raiz do projeto

No seu terminal execute o comando:
docker build -t pypredict .

Após o building execute:
docker run -it pypredict ./init.sh
```

Caso não utilize docker faça:

```sh
No seu terminal na raiz do projeto execute o seguinte comando para instalar as bibliotecas:
pip install -r requirements.txt

Verifique se o arquivo 'init.sh' possui as permissões necessárias
Caso não tenha execute:
chmod +x init.sh

Agora inicie a aplicação executando o comando:
./init.sh

```

## Extras

Acredito que este tipo de aplicação poderia ser melhor aproveitada como um microserviço conteinerizado em nuvem que possua conexão com um banco de dados não relacional também em nuvem como mongo atlas ou firebird, atuando como uma espécie de pipeline de dados, sendo a entrada, registros da pandemia da covid-19 e sua sáida, os dados processados e limpos que serão armazenados em seu respectivo banco de dados em nuvem. Sobre as características e 'modus operandi' da aplicação, uma melhor abordagem poderia ser o emprego de um modelo baseado em IA como regressão logística e clusterização levando em consideração a vasta quantidade de variáveis disponíveis nas bases de dados referenciadas neste documento, para obter um maior grau de acurácia das predições. E finalmente, sobre o foco da informação gerada, acredito que alimentar dashboards e demais aplicações que dependam dos efeitos de uma pandemia viral seriam as principais metas para esse tipo de projeto.