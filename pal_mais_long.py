texto = input('Digite um texto: ').split()
palavras_grand = []
cont = 0

for palavra in texto:
    letras = [char for char in palavra if char.isalpha()]
    if len(letras) > 10:
        palavras_grand.append(palavra)
        cont += 1


if cont == 0:
    print('Nenhuma palavra longa foi encontrada no texto. ')
else:
    print(f'{palavras_grand}')
    
