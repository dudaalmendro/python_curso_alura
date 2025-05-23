saque = int(input("Digite o valor do saque: "))

if saque % 2 != 0:
    print("Erro: O valor deve ser múltiplo de 2.")
else:
    valor_cem = saque // 100
    saque %= 100

    valor_cinquenta = saque // 50
    saque %= 50

    valor_vinte = saque // 20
    saque %= 20

    valor_dez = saque // 10
    saque %= 10

    valor_cinco = saque // 5
    saque %= 5

    valor_dois = saque // 2
    saque %= 2

    if valor_cem > 0:
        print(f"{valor_cem} nota(s) de R$ 100")
    if valor_cinquenta > 0:
        print(f"{valor_cinquenta} nota(s) de R$ 50")
    if valor_vinte > 0:
        print(f"{valor_vinte} nota(s) de R$ 20")
    if valor_dez > 0:
        print(f"{valor_dez} nota(s) de R$ 10")
    if valor_cinco > 0:
        print(f"{valor_cinco} nota(s) de R$ 5")
    if valor_dois > 0:
        print(f"{valor_dois} nota(s) de R$ 2")
