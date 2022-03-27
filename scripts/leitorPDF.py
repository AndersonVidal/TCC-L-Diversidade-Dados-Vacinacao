# importa as bibliotecas necessárias
from logging import warning
import PyPDF2
import csv
import os
import warnings
from tika import parser

DIRETORIO_LISTAS = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas'
ARQUIVO_CSV = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas_csvs\\Agendados.csv'
comProblema = []

def getParsed(file, pageNum):
    page = file.getPage(pageNum)
    page_content = page.extractText()
    #print(page_content.encode('utf-8'))
    if ord(page_content[0]) == 10 and ord(page_content[1]) == 10:
        return 'COMPROBLEMA'
    parsed = ''.join(page_content)

    parsed = parsed.split('\n')
    return parsed

def incrementHeader(parsed, writercsv):
    header = parsed[0:6]

    writercsv.writerow(header)

def removeText(parsed):
    last = 0
    for i in range(10, len(parsed), 5):
        try:
            last = int(parsed[i])
        except:
            break
    if last > 0:
        parsed = parsed[0:last+1]

def incrementRow(file, pageNum, writercsv):
    parsed = getParsed(file, pageNum)
    if parsed == 'COMPROBLEMA':
        return parsed

    if pageNum == 0:
        incrementHeader(parsed, writercsv)
        removeText(parsed)

    i = 6

    for j in range(6, len(parsed) + 1, 6):
        row = parsed[i:j]
        if len(row) > 0:
            writercsv.writerow(row)
        i = j

def genCSV(file, writercsv):
    numPages = file.getNumPages()
    for i in range(0, numPages):
        s = incrementRow(file, i, writercsv)
        if s == 'COMPROBLEMA':
            return 1
    return 0

def lerArquivo(arquivo_pdf, writer):
    pdf_file = open(arquivo_pdf, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    res = genCSV(read_pdf, writer)
    if res == 1:
        comProblema.append(arquivo_pdf)
    

def processaArquivos():
    csv_file = open(ARQUIVO_CSV, 'w', encoding='UTF8')
    arquivos = os.listdir(DIRETORIO_LISTAS)
    #arquivos = ['011121AGENDADOSIDOSOSD3.pdf']
    #arquivos = ['010821AGENDADOSD2.pdf']
    writer = csv.writer(csv_file)

    for arq in arquivos:
        print('----', arq, '----')
        url = DIRETORIO_LISTAS + '//' + arq
        writer.writerow(['----' + arq + '----'])
        lerArquivo(url, writer)

processaArquivos()
print(comProblema)