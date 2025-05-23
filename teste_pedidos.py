import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def inicio(pedido):
    print(f'Processando pedido #{pedido["id"]}')

    if pedido['pagamento_aprovado']:
        print(f'Pagamento aprovado para pedido #{pedido["id"]}')
    else: 
        print(f'Pagamento recusado para pedido #{pedido["id"]}. Pedido cancelado.')
        return
     
    if pedido["estoque_disponivel"]:
        print(f'Estoque disponível para pedido #{pedido["id"]}')
        await processamento(pedido)
    else:
        print(f'Estoque indisponível para pedido #{pedido["id"]}. Pedido cancelado.')

async def processamento(pedido):
    print(f'Pedido #{pedido["id"]} confirmado! Enviado para entrega.\n')
    await asyncio.sleep(1)  # Simula tempo de processamento

async def main():
    tarefas = []
    for pedido in pedidos[:3]:
        tarefas.append(asyncio.create_task(inicio(pedido)))
    await asyncio.gather(*tarefas)

asyncio.run(main())
