import random
import asyncio 


async def tempe():
    while True:
        await asyncio.sleep(2)
        senso_temp = random.choice([ '22C', '23C' , '23C', '25C'])
        print(f'[{2}s] Temperatura: {senso_temp}')
        

async def umi():
    while True: 
        await asyncio.sleep(3)
        senso_umi = random.choice(['60%', '50%', '60%' , '70%'])
        print(f'[{3}s] Temperatura: {senso_umi}')
        

async def quali():
    while True:
        await asyncio.sleep(5)
        senso_quali = random.choice([ 'ruim' , 'regular', 'boa', 'otima'])
        print(f'[{5}s] Qualidade do ar: {senso_quali}')
       

async def main(): 
    await asyncio.gather(tempe(), umi(), quali())

asyncio.run(main())



    
