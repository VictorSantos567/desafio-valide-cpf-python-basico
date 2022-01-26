cpf = '168995350'
lista = []
soma = 0

print(f'Os 9 primeiros digitos são: {cpf}')

for cont in cpf:
    cont = int(cont)
    lista.append(cont)

for indice, valor in enumerate(range(10, 1, -1)):
    multiplicacao = lista[indice] * valor
    soma += multiplicacao

formula = 11 - (soma % 11)

digito_1 = 0 if formula > 9 else formula
print(f'Digito 1 encontrado é: {digito_1}')
"""----------------------------------------------------"""

lista.append(digito_1)
soma_2 = 0

for indice, valor in enumerate(range(formula, 1, -1)):
    multiplicacao = lista[indice] * valor
    soma_2 += multiplicacao

formula_2 = 11 - (soma_2 % 11)

digito_2 = 0 if formula_2 > 9 else formula_2

lista.append(digito_2)
print(f'Digito 2 encontrado é: {digito_2}')

cpf_digito = []

for indice, valor in enumerate(lista):
    cpf_digito += str(lista[indice])

cpf = "".join(cpf_digito)

novo_cpf = '16899535009'
print(f'O cpf com digitos é: {novo_cpf}')

if cpf == novo_cpf:
    print(f'O cpf: {cpf} é Válido')
else:
    print(f'O cpf: {cpf} é invalido')
