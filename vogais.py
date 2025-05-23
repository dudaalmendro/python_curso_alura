vog = ['a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú']
cont = 0
frase = input('Escreva uma frase: ').lower()

letras = [char for char in frase if char.isalpha()]
for letra in letras:
    if letra in vog:
        cont += 1

print(f'O texto contém {cont} vogais.')
