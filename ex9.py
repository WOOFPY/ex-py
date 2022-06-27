lista = []

for c in input("Digite seu nome: "): #colocando em uma lista ele ficara em forma de escada
    lista.append(c)
    var1 = "".join(map(str,lista))
    "".join(map(str, lista)) # retirando os [, ], ', e ,
    print(var1.upper()) #.upper para letra maiuscula