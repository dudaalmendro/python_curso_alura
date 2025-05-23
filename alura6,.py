def calcular(x):
    soma = 0
    for i in range(0, x+1):
        soma = soma + i 
    return soma

numero = int(input('escreva o numero: '))

print(f'soma dos numeros: {calcular(numero)}')
    