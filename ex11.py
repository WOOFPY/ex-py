lista1 = [11, 12, 11, 12]
lista2 = [21, 22, 21, 22]

soma1 = (lista1[0] * lista2[1])
soma2 = (lista1[1] * lista2[2])
soma3 = (lista1[2] * lista2[3])
soma4 = (soma3 * soma2) * soma1
print(f'| A{lista1[0]} A{lista1[1]} B{lista1[2]} B{lista1[3]} |\n| A{lista2[0]} A{lista2[1]} B{lista2[2]} B{lista2[3]} |\n')
print(f'DetA = {lista1[0]}.{lista2[1]} {lista1[1]}.{lista2[2]} {lista1[2]}.{lista2[3]}')
print(f'DetA = {soma1}.{soma2}.{soma3}')
print(f'DetA = {soma4}')