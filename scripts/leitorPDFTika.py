from logging import warning
from tika import parser
import csv
import os

HEADER = [
    'nome', 
    'data_nascimento', 
    'localvacinacao', 
    'data', 
    'hora', 
    'dose'
]
DIRETORIO_LISTAS = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas'
ARQUIVO_CSV = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas_csvs\\Agendados.csv'
# '010821AGENDADOSD2.pdf'

def lerPdf(url):
    raw = parser.from_file(url)
    content = raw['content']

    content = content.split(chr(10))

    return content

def limpaTexto(content):
    cleanContent = []
    for row in content:
        if row == '':
            continue
        if len(str(row)) <= 5:
            continue
        teste = str(row[0:4]).lower()
        if teste == 'page' or teste == 'dose':
            continue
        letra = str(row[1])
        first = str(row).split(' ')[0]
        if letra.islower() and first != 'nome' or letra.isdigit() or not letra.isalnum():
            continue
        if str(row).upper().find('EM GERAL - IDADE') > -1:
            continue
        letra = str(row[0])
        if letra.isdigit() or not letra.isalnum():
            continue
        if str(row).upper().find('LEMBRE:') > -1:
            continue
        if str(row).upper().find('CPF') > -1:
            continue
        #print(row)
        cleanContent.append(row)

    cleanContent.pop(0)

    for i in range(0, len(cleanContent)):
        row = str(cleanContent[i])
        ref1 = row.find('/')
        inc = (-2, 8)
        if ref1 == -1:
            ref1 = row.find('-')
            inc = (-4, 6)

        nascIdx = (ref1+inc[0], ref1+inc[1])
        nomeIdx = (0, nascIdx[0]-1)

        resto = row[nascIdx[1]+1:]
        ref2 = resto.find(':')

        horaIdx = (ref2-2, ref2+6)
        dataIdx = (horaIdx[0]-11, horaIdx[0]-1)
        doseIdx = -1
        localIdx = (0, dataIdx[0] - 1)

        nome = row[nomeIdx[0]:nomeIdx[1]]
        nasc = row[nascIdx[0]:nascIdx[1]]
        local = resto[localIdx[0]:localIdx[1]]
        data = resto[dataIdx[0]:dataIdx[1]]
        hora = resto[horaIdx[0]:horaIdx[1]]
        #print(row)
        #print(len(row), '-', len(resto))
        dose = resto[doseIdx]

        cleanContent[i] = [
            nome, nasc, local, data, hora, dose
        ]

    return cleanContent

def processaArquivos():
    csv_file = open(ARQUIVO_CSV, 'w', encoding='UTF8')
    #arquivos = os.listdir(DIRETORIO_LISTAS)
    #arquivos = ['010821AGENDADOSD2.pdf']
    #arquivos = [
    #    '080122AGENDADOSGERALD3.pdf', 
    #    '100222AGENDADOSGERALD3.pdf', 
    #    '200122AGENDADOSGERALD3.pdf' 
    #]
    arquivos = [
        '290921POPULACAOGERALD1.pdf', 
        '280921POPULACAOGERALD1.pdf', 
        '180821GESTANTESEPUERPERASD1.pdf',
        '150721POPULACAOGERALD1.pdf',
    ]
    writer = csv.writer(csv_file)

    for arq in arquivos:
        print('----', arq, '----')
        url = DIRETORIO_LISTAS + '//' + arq
        #writer.writerow([arq + '----'])
        content = lerPdf(url)
        #print(content)
        cleanContent = limpaTexto(content)
        #print(cleanContent)
        #writer.writerow(HEADER)
        writer.writerows(cleanContent)

processaArquivos()