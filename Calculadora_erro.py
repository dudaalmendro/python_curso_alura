
try:
    y = int(input('Digite o primeiro número: '))
    operacao = input('Escolha a operação (+, -, *, /): ')
    x = int(input('Digite o segundo número: '))

    if operacao == '+':
        ope = y + x
        print(ope)
    elif operacao == '-':
        ope = y - x
        print(ope)
    elif operacao == '*':
        ope = y * x
        print(ope)
    else: 
        ope = y / x
        print(ope)
except ValueError:
  print('Erro: Entrada inválida. Digite apenas números.') 
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')

    