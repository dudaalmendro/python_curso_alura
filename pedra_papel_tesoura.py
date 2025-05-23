import asyncio
import random  

escolhas_comp = ['pedra' , 'papel', 'tesoura']


escolha_agr = random.choice(escolhas_comp)


async def empate(x):
    if escolha_agr == x:
        print('empate')
        

async def pedra1(x):
    if (x == 'pedra') and (escolha_agr == 'tesoura') :
        print('Voce ganhou!')
        

async def pedra2(x):
    if (escolha_agr == 'pedra') and (x == 'tesoura') :
        print('Voce perdeu!')
        
async def tesoura1(x):
    if (x == 'tesoura') and (escolha_agr == 'papel'): 
        print('Voce ganhou!')
        

async def tesoura2(x):
    if (escolha_agr == 'tesoura') and (x == 'papel'): 
        print('Voce ganhou!')
        

async def papel1(x):
    if (x == 'papel') and (escolha_agr == 'pedra'):
        print('voce ganhou!')
        

async def papel2(x):
    if (escolha_agr == 'papel') and (x == 'pedra'):
        print('voce perdeu!')
        

sua_escolha = input('Escolha: pedra, papel ou tesoura? ').lower

async def main():
    await empate(sua_escolha) 
    await pedra1(sua_escolha)
    await pedra2(sua_escolha)        
    await tesoura1(sua_escolha)
    await tesoura2(sua_escolha)
    await papel1(sua_escolha)
    await papel2(sua_escolha)

asyncio.run(main())