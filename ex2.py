import math #biblioteca de somas

print('=x='*7)
print(' CALCULANDO VETORES')
print('=x='*7)

lista = []

for c in range(5):
    lista.append(int(input(f'Digite o {c+1}° número: ')))
soma = sum(lista)
mult = math.prod(lista) #faz a multiplicação
print('=========')
print('SOMA: {}\nMULTIPLICAÇÃO: {}\nLISTA: {}'.format(soma, mult, lista))