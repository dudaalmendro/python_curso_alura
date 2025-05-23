n = int(input("Quantos numeros voce vai digitar? "))

vet = [0 for x in range(n)]

neg = 0 

for i in range (0 , n):
    vet[i] = int(input("Digite um numero: "))

print("NUMEROS NEGATIVOS: ")

for i in range (0, n):
    if vet[i] < 0:
        print(f"negativo {vet[i]}")
    
