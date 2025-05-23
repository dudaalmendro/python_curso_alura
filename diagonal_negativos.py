n = int(input("Qual a ordem da matriz? "))

matriz: [[int]] = [[ 0 for x in range (n)] for x in range(n)]


cont= 0

for i in range (n):
    for j in range (n):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]:"))
        if matriz[i][j] < 0:
            cont = cont +1

print("DIAGONAL PRINCIPAL: ")

for i in range (0 , n):
    print(f"{matriz[i][i]}", end="" " " )
    
print()

print(f"QUANTIDADE DE NEGATIVOS =  {cont}")

