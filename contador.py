

saq = int(input('digite o valor do sauqe: '))
valor_cem = 0
valor_cinquenta = 0
valor_vinte = 0 
valor_dez = 0 
valor_cinco = 0
valor_dois = 0

while saq > 0:
    if saq % 2 == 0:
        saq = saq - 100
        if saq  <= 0: 
            valor_cem = valor_cem + 1
            print(f'{valor_cem} de R$ 100')


            if saq <= 0 == False:  
                cinquenta = saq - 50 
                if cinquenta <= 0:
                    valor_cinquenta = valor_cinquenta + 1
                    print(f'{valor_cinquenta} de R$ 50')


                    if cinquenta <= 0 == False:
                        vinte = cinquenta - 20 
                        if vinte <= 0: 
                            valor_vinte = valor_vinte + 1
                            print(f'{valor_vinte} de R$ 20')


                            if vinte <= 0 == False:
                                dez = vinte - 10
                                if dez <= 0:
                                    valor_dez = valor_dez + 1
                                    print(f'{valor_dez} de R$ 10')


                                    if dez <= 0 == False:
                                        cinco = dez - 5
                                        if cinco <= 0:
                                            valor_cinco = valor_cinco + 1
                                            print(f'{valor_cinco} de R$ 5')

                                            
                                            if cinco <= 0 == False:
                                                dois = cinco - 2
                                                if dois <= 0:
                                                    valor_dois = valor_dois + 1
                                                    print(f'{valor_dois} de R$ 2')
    else: 
       print('Erro: O valor deve ser múltiplo de 2.') 
       break                
      