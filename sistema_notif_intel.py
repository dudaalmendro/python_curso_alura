import asyncio

async def notificacao():
    print('Enviando notificações...')
    await asyncio.sleep(2)

async def vip():
    print('Notificação VIP para ana enviada!')
    await asyncio.sleep(2)

async def normal():
    print('Notificação normal para João enviada!')
    await asyncio.sleep(2)
    print('Carla desativou as notificações. Nada foi enviado.')
    await asyncio.sleep(2)
    print('Todas as notificações foram processadas!')


async def main():
    
    tarefa1 = asyncio.create_task(notificacao())
    await tarefa1
    tarefa2 = asyncio.create_task(vip())
    await tarefa2
    tarefa3 = asyncio.create_task(normal())
    await tarefa3

asyncio.run(main())


