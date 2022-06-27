#listas
lista1 = []
lista2 = []
lista3 = []

#perguntas
for c in range(5):
    lista1.append(str(input(f'Informe o nome N°{c+1}: ')))
    lista2.append(input('Idade: '))
    lista3.append(input('Altura: '))

#listas de resposta
# [::-1] significa começar do primeiro caractere e indo em um passo negativo de -1 ( de trás para frente )
print('==============')
print('Nome: {}\nIdade: {}\nAltura: {}'.format(lista1[0], lista2[0][::-1], lista3[0][::-1]))
print('==============')
print('Nome: {}\nIdade: {}\nAltura: {}'.format(lista1[1], lista2[1][::-1], lista3[1][::-1]))
print('==============')
print('Nome: {}\nIdade: {}\nAltura: {}'.format(lista1[2], lista2[2][::-1], lista3[2][::-1]))
print('==============')
print('Nome: {}\nIdade: {}\nAltura: {}'.format(lista1[3], lista2[3][::-1], lista3[3][::-1]))
print('==============')
print('Nome: {}\nIdade: {}\nAltura: {}'.format(lista1[4], lista2[4][::-1], lista3[4][::-1]))
print('==============')

