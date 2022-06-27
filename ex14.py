lista = []

for c in range(3):
    lista.append(int(input(f'Digite o {c+1}° argumento: ')))

print(f'A soma dos 3 argumentos foram {sum(lista)}')