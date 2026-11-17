import pandas as pd
from datetime import datetime

def soma_despesas(financias):
        total_despesas = sum(item['despesa'] for item in financias )
        return total_despesas

def soma_receitas(financias):
    try:
        total_receitas = sum(item['receita'] for item in financias if item['tipo'] == 'receita')
        return total_receitas
    except:
        return("ERRO: sem valor adicionado")

def mostrar_receitas_despesas(financias):
    for item in financias:
        if 'despesa' in item:
            print(f'Despesa: {item["despesa"]}')
        elif 'receita' in item:
            print(f'Receita: {item["receita"]}')

def saida_do_sistema(financias):
    df = pd.DataFrame(financias)
    df.to_excel('financas.xlsx', index=False)    
    quit()

try:
    financias = pd.read_excel('financas.xlsx').to_dict(orient='records')
except FileNotFoundError:
    financias = []
while True:    
    print('1 - Adicionar despesa')
    print('2 - Adicionar receita')
    print('3 - Retirar despesa/receita')
    print('4 - Total de despesas')
    print('5 - Total de receitas')
    print('6 - Saldo final')
    print('7 - mostrar todas as despesas/receitas')
    print('8 - Sair')
    opcao = input('escolha uma opção: ')

    if opcao == '1':
        despesa = float(input('Digite o valor da despesa: '))
        data = datetime.strptime(
            input('Digite a Data (DD-MM-AAAA)'),
            '%d/%m/%Y'
        ).date          ()
        financias.append({'despesa': despesa, 'data': data})
    
    elif opcao == '2':
        receita = float(input('Digite o valor da receita: '))
        financias.append({'receita': receita})
    
    elif opcao == '3':
        print(financias)
        opcao = float(input('digite qual o valor a retirar?'))
        financias.remove(opcao)        
    
    elif opcao == '4':
        total_despesas = soma_despesas(financias)
        print(f'Total de despesas: {total_despesas}')
    
    elif opcao == '5':
        total_receitas = soma_receitas(financias)
        print(f'Total de receitas: {total_receitas}')
    
    elif opcao == '6':
        total_despesas = soma_despesas(financias)
        total_receitas = soma_receitas(financias)
        saldo = total_receitas - total_despesas
        print(f'Saldo final: {saldo}')
    
    elif opcao == '7':
        print('Despesas e Receitas:')
        mostrar_receitas_despesas(financias)
    
    elif opcao == '8':
        print('Saindo do sistema...')
        saida_do_sistema(financias)
    else:
        print('Opção inválida. Tente novamente.')
