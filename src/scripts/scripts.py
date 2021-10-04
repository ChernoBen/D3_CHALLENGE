import pandas as pd
import datetime

#funcao que recebe uma string e retorna um formato date 
def dateToStr(date):
    return datetime.datetime.strptime(date,'%Y-%m-%d').date()

#funcao que verifica se um dado é um numero
def isNumber(number):
    try:
        if float(number)>=0:
            return True
    except ValueError:
        return False
    return False

#funcao que retorna a somatoria de uma lista
def sumDay(element):
    total = 0
    for item in element:
        total+=item[1]
    return total

#funcao que retorna a media da taxa de contagio/transmissao
def meanTr(arr):
    tr = 0
    total = 0
    for item in arr.values:
        if isNumber(item[2]):
            tr += item[2]
            total +=1
    if total>0:
        return tr/total
    return 0

#funcao que retorna a somatoria do total de casos em um determinado dia
def getTotal(df):
    total = 0
    cases = [item[1]for item in df.values if isNumber(item[1])]
    for item in cases:
        total += item
    return total

#funcao que retorna um dataframe contendo dados extraidos de uma base csv
def getData(days=0):
    #seleção e adição de dias a data
    df = pd.read_csv('datasets/owid-covid-data.csv')
    #data referente ao registro dos primeiros casos de covid-19
    min_date = datetime.datetime.strptime('2020-01-22','%Y-%m-%d').date()
    data = df[['date','total_cases','reproduction_rate']]
    #dicionario que irá conter tr(taxa de contágio) e total de casos por data
    dictonary = {}
    for i in range(days):
        n_date = dateToStr(str(min_date+datetime.timedelta(days=i)))
        dictonary[f'{n_date}'] = data[data['date'] == f'{n_date}']
    total = []
    #tr é o taxa de contágio e ct o contador
    tr = []
    ct = 0
    for chave in dictonary:
        total.append(getTotal(dictonary[chave]))
        if ct>0:
            tr.append(meanTr(dictonary[chave]))
        else:
            tr.append(0)
        ct +=1
    #gerando um dataframe contendo a taxa de transmissão/contagio e total de casos de cada data
    table = list(zip(total,tr))
    table = pd.DataFrame(table, columns = ['total','reproduction_rate'])
    return table

#funcao que retorna uma lista com porcentagens de aumento do proximo dia em ralação ao anterior
def txMedia(arr):
    tx = []
    tx.append(0)
    previous = 0
    for i in range(len(arr)-1):
        previous = arr[i]
        tx.append(((arr[i+1]-previous)*100)/previous)
    return tx

#funcao que retorna uma lista com a taxa/procentagem média de aumento de casos a cada 15 dias
def prcMedia(arr):
    tx = []
    counter = 0
    total = 0
    for i in range(len(arr)):
        total +=arr[i]
        counter +=1
        if counter>=15:
            tx.append(total/15)
            total = arr[i]
            counter = 0
    return tx

#fazer analize diária e pegar um intervalo
def predict(day=0):
    d = 0
    if day<15:
        d=15 
    else:
        d = day
    table = getData(d)
    counter = 0
    #quantidade de casos registrados na menor data é usado como parâmetro para pedrição 
    first_cases = table['total'][0]
    #days_list recebe uma lista com porcentagens de aumento do proximo dia em ralação ao anterior
    days_list = txMedia(table['total'].values)
    #perc recebe uma lista com a taxa/procentagem média de aumento de casos a cada 15 dias
    perc = prcMedia(days_list)
    #d_lista guardará as predições com base da taxa media quinzenal(perc) e casos do do dia anterior
    d_list = []
    # quinzena é uma flag que serve como marcador de quinzenas
    quinzena = 0
    for i in range(day):
        # first_cases recebe o produto da perc pelos casos anteriores divitido por 100 + casos anteriores
        first_cases = ((perc[quinzena]*first_cases)//100)+first_cases
        d_list.append(first_cases)
        counter +=1
        if counter > 15:
            counter = 0
            quinzena +=1
    for j in range(day):
        if j == 0:
            print(f'{j+1} -> {int(table["total"][0])}')
        else:
            print(f'{j+1} -> {int(d_list[j-1])}')   