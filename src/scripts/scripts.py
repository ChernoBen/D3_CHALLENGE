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
    data = df[['date','total_cases','total_tests','positive_rate','reproduction_rate']]
    min_date = datetime.datetime.strptime('2020-01-22','%Y-%m-%d').date()
    t2 = data[['date','total_cases','reproduction_rate']]
    dias = days
    dicionario = {}
    for i in range(dias):
        n_date = dateToStr(str(min_date+datetime.timedelta(days=i)))
        dicionario[f'{n_date}'] = t2[t2['date'] == f'{n_date}']
    total = []
    tr = []
    ct = 0
    for chave in dicionario:
        total.append(getTotal(dicionario[chave]))
        if ct>0:
            tr.append(meanTr(dicionario[chave]))
        else:
            tr.append(0)
        ct +=1
    table = list(zip(total,tr))
    table = pd.DataFrame(table, columns = ['total','reproduction_rate'])
    return table

#funcao que retorna uma lista com procentagens de aumento do proximo dia em ralação ao anterior
def txMedia(arr):
    tx = []
    tx.append(0)
    anterior = 0
    for i in range(len(arr)-1):
        anterior = arr[i]
        tx.append(((arr[i+1]-anterior)*100)/anterior)
    return tx

#funcao que retorna uma lista com a taxa de aumento de casos a cada 15 dias
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
    first_cases = table['total'][0]
    days_list = txMedia(table['total'].values)
    perc = prcMedia(days_list)
    d_list = []
    quinzena = 0
    for i in range(day):
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