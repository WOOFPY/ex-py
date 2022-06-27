print('=x='*7)
print('  CALCULANDO NOTAS')
print('=x='*7)
print('Obs: valor maximo = 100')

#listas
temp = []
princ = []
princ2 = []
alunos = []

#área das perguntas
for c in range(10):
    print('==================')
    princ2.append(str(input(f'Digite o nome do aluno N{c+1}: ')))
    temp.append(float(input('Digite a primeira nota: ')))
    temp.append(float(input('Digite a segunda nota: ')))
    temp.append(float(input('Digite a terceira nota: ')))
    temp.append(float(input('Digite a quarta nota: ')))
    princ.append(temp[:]) #copiando a lista temp
    temp.clear() #lipar a lista temp para que n haja bugs

#calculando as notas
som1 = sum(princ[0]) / len(princ[0])
som2 = sum(princ[1]) / len(princ[1])
som3 = sum(princ[2]) / len(princ[2])
som4 = sum(princ[3]) / len(princ[3])
som5 = sum(princ[4]) / len(princ[4])
som6 = sum(princ[5]) / len(princ[5])
som7 = sum(princ[6]) / len(princ[6])
som8 = sum(princ[7]) / len(princ[7])
som9 = sum(princ[8]) / len(princ[8])
som10 = sum(princ[9]) / len(princ[9])

#soma das notas acima de 70
if som1 > 70:
    alunos.append(princ[0][0])
if som2 > 70:
    alunos.append(princ[0][0])
if som3 > 70:
    alunos.append(princ[0][0])
if som4 > 70:
    alunos.append(princ[0][0])
if som5 > 70:
    alunos.append(princ[0][0])
if som6 > 70:
    alunos.append(princ[0][0])
if som7 > 70:
    alunos.append(princ[0][0])
if som8 > 70:
    alunos.append(princ[0][0])
if som9 > 70:
    alunos.append(princ[0][0])
if som10 > 70:
    alunos.append(princ[0][0])

#resultado de todos os alunos, somas e status
print('-----------')
if som1 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[0], som1, 'Aprovado'))
elif som1 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[0], som1, 'Reprovado'))
print('-----------')
if som2 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[1], som2, 'Aprovado'))
elif som2 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[1], som2, 'Reprovado'))
print('-----------')
if som3 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[2], som3, 'Aprovado'))
elif som3 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[2], som3, 'Reprovado'))
print('-----------')
if som4 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[3], som4, 'Aprovado'))
elif som4 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[3], som4, 'Reprovado'))
print('-----------')
if som5 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[4], som5, 'Aprovado'))
elif som5 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[4], som5, 'Reprovado'))
print('-----------')
if som6 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[5], som6, 'Aprovado'))
elif som6 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[5], som6, 'Reprovado'))
print('-----------')
if som7 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[6], som7, 'Aprovado'))
elif som7 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[6], som7, 'Reprovado'))
print('-----------')
if som8 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[7], som8, 'Aprovado'))
elif som8 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[7], som8, 'Reprovado'))
print('-----------')
if som9 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[8], som9, 'Aprovado'))
elif som9 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[8], som9, 'Reprovado'))
print('-----------')
if som10 >= 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[9], som10, 'Aprovado'))
elif som10 < 70:
    print('Aluno: {}\nNota: {:.2f}\nStatus: {}'.format(princ2[9], som10, 'Reprovado'))
print('===============')
print('{} alunos foram aprovados!'.format(len(alunos)))