

def desconto(y):
    def valor(x):
        return x - (x * (y /100))
    return valor


desc = float(input('digite o deconto: '))

calcular_preco_final = desconto(desc)

x = float(input('digite o valor: '))


print(f'preco final com desconto: {calcular_preco_final(x)}')




