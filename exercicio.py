# Lista de números de 1 a 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com quatro nomes
nomes = ["Ana", "Bruno", "Carlos", "Daniela"]

# Lista com o ano de nascimento e o ano atual
anos = [2000, 2025]


frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(fruta)


soma_impares = 0

for numero in range(1, 11):
    if numero % 2 != 0:
        soma_impares += numero

print(f"Soma dos ímpares de 1 a 10: {soma_impares}")

for numero in range(10, 0, -1):
    print(numero)


numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


numeros = [1, 2, 3, 4, 5, 'seis', 7]  # Coloquei um erro de propósito para testar o except

soma = 0

for numero in numeros:
    try:
        soma += int(numero)
    except ValueError:
        print(f"Valor inválido encontrado: {numero}")

print(f"Soma dos elementos válidos: {soma}")


valores = [10, 20, 30, 40, 50]

try:
    media = sum(valores) / len(valores)
    print(f"A média é: {media}")
except ZeroDivisionError:
    print("Não é possível calcular a média de uma lista vazia.")
