import csv
from datetime import date
import math

TODAY = date.today()
ARQUIVO_CSV = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas_csvs\\AgendadosPopulaçãoGeralD3_21022022.csv'

def printTest(data, num: int = 10):
    for i in range(0, num):
        print(data[i])

def getDate(dateStr):
    date = dateStr.split('/')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    return { 'day': day, 'month': month, 'year': year }

def supressName(data):
    for row in data:
        row[0] = '*'
        

def takeAge(data):
    for row in data:
        birthday = getDate(row[1])
        age = int(TODAY.year) - birthday['year']
        row[1] = age

def groupAge(data):
    maxAge = 0
    minAge = 100
    for row in data:
        age = row[1]
        if age > maxAge:
            maxAge = age
        if age < minAge:
            minAge = age

    i = 10

    intervals = {}
    l = minAge
    while l < maxAge:
        intervals[(l, l + i)] = str(l) + ' a ' + str(l + i)
        l += i + 1
    
    for row in data:
        age = row[1]
        for inferior, superior in intervals.keys():
            if age >= inferior and age <= superior:
                row[1] = intervals[(inferior, superior)]
                break
        

file = open(ARQUIVO_CSV, encoding='UTF8')
csvReader = csv.reader(file)

header = []
header = next(csvReader)

data = []

for row in csvReader:
    if (len(row) > 0):
        data.append(row)

supressName(data)
takeAge(data)
groupAge(data)

printTest(data, 10)
qid = ['data_nascimento', 'data', 'hora']
sup = ['nome']



