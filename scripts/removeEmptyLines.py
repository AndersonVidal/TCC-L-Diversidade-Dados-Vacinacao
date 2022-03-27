ARQUIVO_CSV = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas_csvs\\Agendados.csv'
ARQUIVO_CSV2 = 'C:\\Users\\Anderson\\Documents\\Estudos\\tcc\\listasDeAgendamento\\listas_csvs\\Agendados2.csv'
lines = []
with open(ARQUIVO_CSV,'r', encoding="utf8") as file:
    for line in file:
        if not line.isspace():
            lines.append(line)

with open(ARQUIVO_CSV2,'w', encoding="utf8") as file:
    for line in lines:
        file.write(line)
