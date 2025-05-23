

a = int(input('escreva numero 1: '))
b = int(input('escreva numero 2: '))
operacao = input('escreva a operacao: ')

if operacao == '+': 
    soma = lambda a, b: a + b    
    print(soma(a , b))
elif operacao == '-':
    sub = lambda a, b: a - b 
    print(sub(a, b))
elif operacao == '*':
    vezes = lambda a, b: a * b 
    print(vezes)
else:
    divi = lambda a, b: a / b 
    print(divi)



