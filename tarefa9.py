import asyncio

n = ['5', '3', '7', '4', '6'] 
numeros = list(map(int, n))
numeros.sort()

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

async def terefa(numero):
    print(f'Fatorial de {n} = {fatorial(n)}')
    await asyncio.sleep(2)

async def main():
    await asyncio.gather(terefa(1))

for n in numeros:
    asyncio.run(main())


