cpf = input('Digite seu CPF: ').replace('.', '').replace('-', '')  # Remove pontos e traços, se existirem
quant = len(cpf)

def numeros(quant, cpf):
    if quant == 11:
        print('CPF válido.')
    else:
        print('Erro: O CPF deve ter exatamente 11 dígitos.')

    if cpf.isdigit(): 
        print("Todos os elementos são números.")
    else:
        print("Erro: O CPF contém caracteres não numéricos.")
        return

def main():
    numeros(quant, cpf)

main()
