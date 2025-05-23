def desconto(valor, porcentagem):
    gorje = (valor * porcentagem) / 100
    return print(f'Valor da gorjeta: {gorje}')

def total(valor, porcentagem):
    gorje = (valor * porcentagem) / 100
    total_pagar = gorje + valor 
    return print(f'Total a pagar: {total_pagar}')

val = float(input('Digite o valor da conta: '))
porc = int(input('Digite a porcentagem de gorjeta: '))

def main():
    desconto(val, porc)
    total(val, porc)
    
main()