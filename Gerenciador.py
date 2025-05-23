tarefas = []

def ad_tarefas():
    adicionar = input('item para adicionar: ')
    tarefas.append(adicionar)
    print('tarefa adicionada')

def visu_tarefas():
   return print(tarefas)

def remov_tarefas():
    remover = input('item a ser removido: ')
    if remover in tarefas:
        tarefas.remove(remover)
        print('tarefa removida')
    else: 
        print('tarefa nao encontrada')

def sair():
   return print('fim do programa')


def opcoes_tare(op):
    if op == '1':
        ad_tarefas()
    elif op == '2':
        visu_tarefas()
    elif op == '3':
        remov_tarefas()
    elif op == '4':
        sair()
    else:
        print('opcao invalida')

print('\nMenu:')
print('1 - Adicionar tarefa')
print('2 - Ver tarefas')
print('3 - Remover tarefa')
print('4 - Sair')     

op = ''
while op != '4':
    op = input('escolha uma opcao: ')
    opcoes_tare(op)



