import random


minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maiuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numero = [str(i) for i in range(10)]
especial = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
            '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '?', '/', '\\',
            '|', '`', '~']

resultado = [
    random.choice(minuscula),
    random.choice(maiuscula),
    random.choice(numero),
    random.choice(especial)

]
total = 12
todos = minuscula + maiuscula + numero + especial 

while len(resultado) < total :
    resultado.append(random.choice(todos))

random.shuffle(resultado)


palavra = ''.join(resultado)

print(f'senha: {palavra}')