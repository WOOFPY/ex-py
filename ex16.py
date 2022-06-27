valor = float(input('Digite o valor do produto: '))
taxaimposto = float(input('Informe quantos porcentos de imposto sobre o produto [EX: 5]: '))
somaimposto = valor + valor * taxaimposto/100
print('Valor bruto: R${:.2f}\nValor final: R${:.2f}'.format(valor, somaimposto))
