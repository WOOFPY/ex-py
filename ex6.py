lista1 = []
lista2 = []

lista1.append(input('Digite uma frase: '))
lista2.append(input('Digite outra frase: '))

#ler o tamanho das strings
l1 = len(lista1[0])
l2 = len(lista2[0])

print('=================================')
print(f'Tamanho de "{lista1[0]}": contem {len(lista1[0].replace(" ", ""))} caracteres.') #.replace(" ", "") remove os espaços entre as frazes.
print(f'Tamanho de "{lista2[0]}": contem {len(lista2[0].replace(" ", ""))} caracteres.')

if l1 == l2:
    print('As duas strings trem tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')

if lista1 == lista2:
    print('As duas strings possuem conteúdos iguais.')
else:
    print('As duas strings possuem conteúdos diferente.')