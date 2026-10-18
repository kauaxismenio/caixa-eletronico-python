
saldo = 1000
dep = list()
sac = list()
historico = list()


def linha():
    print('-=' * 20)


while True:
    print('====== CAIXA ELETRÔNICO ======')
    print('[1] Consultar Saldo')
    print('[2] Depositar Saldo')
    print('[3] Sacar Dinheiro')
    print('[4] Histórico de operações')
    print('[5] Sair')

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        linha()
        print(f'Seu saldo é: R$ {saldo:.2f}')
        linha()
        
    elif escolha == 2:
        deposito = float(input('Digite o valor que deseja depositar: '))

        if deposito > 0:
            saldo = saldo + deposito
            dep.append(deposito)
            historico.append(f'Depósito: R$ {deposito:.2f}')

            linha()
            print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
            linha()

        else:
            linha()
            print('Permitido apenas depósitos acima de zero!')
            linha()

    elif escolha == 3:
        saque = float(input('Digite o valor que deseja sacar: '))

        if saque <= 0:
            linha()
            print('Valor inválido! Digite um valor maior que zero.')
            linha()

        elif saque > saldo:
            linha()
            print(f'Seu saldo é de R$ {saldo:.2f}! Não pode fazer um saque maior que o saldo.')
            linha()

        else:
            saldo = saldo - saque
            sac.append(saque)
            historico.append(f'Saque: R$ {saque:.2f}')

            linha()
            print(f'Parabéns pelo saque! Seu novo saldo é de: R$ {saldo:.2f}')
            linha()

    elif escolha == 4:
        if len(historico) == 0:
            print('Nenhuma operação realizada até o momento!')

        else:
            cont = 1
            print('====== HISTÓRICO DE OPERAÇÕES ======')

            for c in historico:
                print(f'{cont} - {c}')
                cont += 1

            print(f'Total de operações: {len(historico)}')
            print('====================================')

    elif escolha == 5:
        linha()
        print('Programa Encerrado!')
        linha()
        break

    else:
        linha()
        print('Opção inválida!')
        linha()


totdep = sum(dep)
totsac = sum(sac)

linha()
print('RELATÓRIO FINAL')
linha()
print(f'Total depositado: R$ {totdep:.2f}')
print(f'Total sacado: R$ {totsac:.2f}')
print(f'Quantidade de operações realizadas: {len(dep) + len(sac)}')
linha()
