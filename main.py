def cria_conta(nmr,nome,saldo,limite):
    conta = {'numero' : nmr,
             'titular' : nome,
             'saldo' : saldo ,
             'limite' : limite}

    return conta

def deposita(conta,valor):
    conta['saldo'] += valor

def sacar(conta,valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'O saldo é R${conta["saldo"]} ')