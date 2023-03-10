import random

def jogar():

    inicializacao()     # Mensagem de Inicial.
    nmr_secreto = sorteando_numero()    # Sorteia um numero Random entre 0 a 100.

    total_tentativas = 0
    pontos = 1000

    total_tentativas = dificuldade()        # Altera a dif. entre F - 20 , M - 10 , D - 5

    print(nmr_secreto)
    rodada = 1

    while rodada in range(rodada,total_tentativas + 1):

        chute = chute_jogador(rodada,total_tentativas) # Mensagem de

        validador_chute = validador_chute_entre(chute)  # Verifica se o chute esta entre 0 e 100

        resul_chute = resultado_chute(chute,nmr_secreto)# Retorna do chute

        while validador_chute is False and resul_chute != 'ACERTOU':
            validador_chute = validador_chute_entre(chute)
            if resul_chute == 'ACERTOU':
                break

        pontos = validador_chute_resultado(resul_chute,pontos,nmr_secreto,chute)
        if resul_chute == 'ACERTOU':
            break

        rodada += 1
    print("Fim de jogo !")

def inicializacao():
    print("\n**************************")
    print("*** Jogo de advinhação ***")
    print("**************************\n")

def sorteando_numero():
    nmr_secreto = round(random.randrange(1, 101))  # Random é entre 0.0 e 1.0
    return nmr_secreto

def dificuldade():
    print("Qual nivel de dificuldade ?\n")
    print("(1) Fácil (2) Médio (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    return total_tentativas

def chute_jogador(rodada,total_tentativas):
    print("\n" + "Tentativa:" + str(rodada) + " de " + str(total_tentativas) + "\n")
    chute = int(input("Digite o seu numero entre 1 a 100: "))
    print("Voce digitou :", chute)

    return chute

def resultado_chute(chute, nmr_secreto):

    if chute == nmr_secreto :
        resul = 'ACERTOU'
        return resul

    if chute > nmr_secreto:
        resul = 'MAIOR'
        return resul

    if chute < nmr_secreto:
        resul = 'MENOR'
        return resul

def validador_chute_entre(chute, validador=None):
    if (chute < 1 or chute > 100):
        validador = (chute < 1 or chute > 100)
        print("Voce deve digitar um numero entre 1 a 100")
    return validador
        # CONTINUA COM A PROXIMA INTERAÇÃO ANUNLANDO O CODIGO A BAIXO

def validador_chute_resultado(resul_chute,pontos,nmr_secreto,chute):
    if (resul_chute == 'ACERTOU'):
        print("Voce acertou! e fez {} pontos !".format(pontos))
        # SAI DO LAÇO
    else:
        if (resul_chute == 'MAIOR'):
            print("Voce errou ! O seu chute foi maior que o numero secreto ! ")
        elif (resul_chute == 'MENOR'):
            print("Voce errou ! O seu chute foi menor que o numero secreto ! ")
        pontos_perdidos = abs(nmr_secreto - chute)
        pontos = pontos - pontos_perdidos
    return pontos

if(__name__=='__main__'):
    jogar()

