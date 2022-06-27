import random #biblioteca para gerar números aleatorios

#listas
v1 = []
v2 = []

#gerando números aleatorios
n1 = random.sample(range(100), k=10) # gerar números de 0 a 100 em apenas 10 casas.
v1.append(n1)
n2 = random.sample(range(100), k=10)
v2.append(n2)

#montando os vetores
print('VETOR 1')
print(f'{v1[0][0]}  {v1[0][1]}  {v1[0][2]}  {v1[0][3]}  {v1[0][4]}  {v1[0][5]}  {v1[0][6]}  {v1[0][7]}  {v1[0][8]}  {v1[0][9]}')
print('---------------------------------------- >')
print('=x=x=x=x=x=x=x=x=x=x=x=')
print('VETOR 2')
print(f'{v2[0][0]}  {v2[0][1]}  {v2[0][2]}  {v2[0][3]}  {v2[0][4]}  {v2[0][5]}  {v2[0][6]}  {v2[0][7]}  {v2[0][8]}  {v2[0][9]}')
print('---------------------------------------- >')
print('=x=x=x=x=x=x=x=x=x=x=x=')
print('VETOR 3')
print(f'{v1[0][0]}  {v1[0][1]}  {v1[0][2]}  {v1[0][3]}  {v1[0][4]}  {v1[0][5]}  {v1[0][6]}  {v1[0][7]}  {v1[0][8]}  {v1[0][9]}  {v2[0][0]}  {v2[0][1]}  {v2[0][2]}  {v2[0][3]}  {v2[0][4]}  {v2[0][5]}  {v2[0][6]}  {v2[0][7]}  {v2[0][8]}  {v2[0][9]}')
print('-------------------------------------------------------------------------------- >')
