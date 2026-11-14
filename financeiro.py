import pandas as pd

def soma_despesas(financias):
        total_despesas = sum(item['valor'] for item in financias if item['tipo'] == 'despesa')
        return total_despesas

def soma_receitas(financias):
    total_receitas = sum(item['valor'] for item in financias if item['tipo'] == 'receita')
    return total_receitas

try:
    financias = pd.read_excel('financas.xlsx').to_dict(orient='records')
except FileNotFoundError:
    financias = []
while True:    
    print('1 - Adicionar despesa')
    print('2 - Adicionar receita')
    print('3 - Total de despesas')
    print('4 - Total de receitas')
    print('5 - Saldo final')
    print('6 - mostrar todas as despesas/receitas')
    print('7 - Sair')
    opcao = input('escolha uma opção: ')

    if opcao == '1':
        despesa = float(input('Digite o valor da despesa: '))
        financias.append({'tipo': 'despesa', 'valor': despesa})
    
    elif opcao == '2':
        receita = float(input('Digite o valor da receita: '))
        financias.append({'tipo': 'receita', 'valor': receita})
    
    elif opcao == '3':
        total_despesas = soma_despesas(financias)
        print(f'Total de despesas: {total_despesas}')
    
    elif opcao == '4':
        total_receitas = soma_receitas(financias)
        print(f'Total de receitas: {total_receitas}')
    
    elif opcao == '5':
        total_despesas = soma_despesas(financias)
        total_receitas = soma_receitas(financias)
        saldo = total_receitas - total_despesas
        print(f'Saldo final: {saldo}')
    
    elif opcao == '6':
        print('Despesas e Receitas:')
        for item in financias:
            print(f"{item['tipo'].capitalize()}: {item['valor']}")
        print(f'Total: {sum(item["valor"] for item in financias)}')
    
    elif opcao == '7':
        print('Saindo do programa...')
        df = pd.DataFrame(financias)
        df.to_excel('financas.xlsx', index=False)    
        quit()
    else:
        print('Opção inválida. Tente novamente.')
df = pd.DataFrame(financias)