"""
Para validar o CPF utilizando o digitos
CPF = 168.995.350-09

- PARA ENCONTRAR O PRIMEIRO DIGITO

multiplicar os 9 primeiro numeros do CPF por contagem regressiva de 10 a 2,
e a cada multiplicação salvar em uma variavel
somar todas a variaveis da multiplicação = resultado
formula

1 * 10 = 10         #   1 * 11 = 11 <-
6 * 9 = 54          #   6 * 10 = 60
8 * 8 = 64          #   8 * 9 = 72
9 * 7 = 63          #   9 * 8 = 72
9 * 6 = 54          #   9 * 7 = 63
5 * 5 = 25          #   5 * 6 = 30
3 * 4 = 12          #   3 * 5 = 15
5 * 3 = 15          #   5 * 4 = 20
0 * 2 = 0           #   0 * 3 = 0
                    #-> 0 * 2 = 0
        297         #           343
11 - (297 % 11)= 11 #   11 - (343 % 11) = 9
11 > 9 = 0          #   Digito 2 = 9
Digito 1 = 0

11 - (resultado % 11) = 11
SE 11 > 9 então o resultado é = 0
digito 1 = 0

- PARA ENCONTRA O SEGUNDO DIGITO

guarda a validação no novo_cpf
"""
cpf = '168995350'
lista = []
soma = 0


for cont in cpf:
    cont = int(cont)
    lista.append(cont)

for indice, valor in enumerate(range(10, 1, -1)):
    multiplicacao = lista[indice] * valor
    soma += multiplicacao

# print(f'{soma}')

formula = 11 - (soma % 11)
# print(digito_1)
# print(formula)

digito_1 = 0 if formula > 9 else formula

print(digito_1)

print('----------------------------------')

lista.append(digito_1)
soma_2 = 0

for indice, valor in enumerate(range(formula, 1, -1)):
    multiplicacao = lista[indice] * valor
    soma_2 += multiplicacao

# print(soma_2)

formula_2 = 11 - (soma_2 % 11)
# print(digito_1)
# print(formula_2)

digito_2 = 0 if formula_2 > 9 else formula_2
print(digito_2)

lista.append(digito_2)
print(lista)

cpf_digito = []

for indice, valor in enumerate(lista):
    cpf_digito += str(lista[indice])

cpf = "".join(cpf_digito)

# print(type(cpf))


novo_cpf = '16899535009'

if cpf == novo_cpf:
    print('Válido')
else:
    print("invalido")
