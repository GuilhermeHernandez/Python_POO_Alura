import random

def jogar():
    mensagem_abertura()
    palavra_secreta = sorteando_palavra()

    print("\n" + "A palavra secreta tem : " + str(len(palavra_secreta)) + " letras")

    letras_acertadas = mostrar_letras(palavra_secreta)

    enforcou = False
    acertou = False
    tentativa = 0

    #ENQUANTO FOR VERDADEIRO
    while (not enforcou and not acertou) :

        chute = chute_jogador()

        if (chute in palavra_secreta) :
            marca_pontos(palavra_secreta,chute,letras_acertadas)
        else:
            tentativa += 1
            desenho_forca(tentativa)

        enforcou = tentativa == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
       mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

def mensagem_abertura():
    print("**************************")
    print("***** Jogo da Forca *****")
    print("**************************")

def sorteando_palavra():
    arq = open("palavras.txt", "r")
    palavras = []

    for linha in arq:
        linha = linha.strip()
        palavras.append(linha)

    arq.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()
    return palavra_secreta

def mostrar_letras(palavra):
    return ["_" for letra in palavra]

def chute_jogador():
    chute = input("\n" + "Qual a letra?")
    chute = chute.strip().upper()
    return chute

def marca_pontos(palavra_secreta,chute,letras_acertadas):
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__=='__main__'):
    jogar()