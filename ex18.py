dat = input('Informe a data em formato [DD/MM/AAAA]: ')
dia = dat[:-8]
mes = dat[:-5][3:]
ano = dat[6:]
print(f'Dia: {dia}\nMês: {mes}\nAno: {ano}')