lista = int(input('digite os numeros da lista de numeros: '))

lista_nume = []
lista_nume.append(lista)

def eh_par(x): 
    return x % 2 == 0

pares = filter(eh_par(lista_nume))

print(pares)

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 
