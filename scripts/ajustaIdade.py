from datetime import date 
def calcIdade(birthDate):
    y = int(birthDate[0:4])
    m = int(birthDate[5:7])
    d = int(birthDate[8:])
    bd = date(y, m, d)
    days_in_year = 365.2425
    age = int((date.today() - bd).days / days_in_year)
    return str(age)

def verifDatavac(vac):
    y = int(vac[0:4])
    if y >= 2020: return vac
    return ''

ARQUIVO_CSV = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\baseAtaque\\ce-vacina_150122.csv'
ARQUIVO_CSV2 = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\baseAtaque\\ce-vacina_150122_adj.csv'
lines = []

with open(ARQUIVO_CSV,'r', encoding="utf8") as file:
    cont = 0
    IDADE = 2
    DNASC = 3
    DVAC = 27
    for line in file:
        if cont == 0: 
            cont += 1
            lines.append(line)
            continue
        arr = line.split(';')
        dnasc = arr[DNASC].strip('"')
        dvac = arr[DVAC].strip('"')
        
        if len(dvac) == 0: continue 
        if len(dnasc) == 0 or dnasc == 'NULL': continue
        idade = calcIdade(dnasc)
        arr[IDADE] = '"' + idade + '"'

        nline = ''
        for v in arr:
            nline += v + ';'
        nline = nline[0:len(nline)-1]

        lines.append(nline)

with open(ARQUIVO_CSV2,'w', encoding="utf8") as file:
    for line in lines:
        file.write(line)


