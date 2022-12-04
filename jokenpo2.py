import random
fimDeJogo = False
placarPC = 0
placarJogador = 0
while True:
    nomeJogador = input("Qual o nome do jogador: ")
    if (nomeJogador != ""):
        break
while (fimDeJogo == False):
    escolhaDoPC = random.randint(1,3)
#1 = pedra 2 =  papel 3 = tesoura
    escolhaDoJogador = input("Ecolha:\n1 - pedra \n2 - papel \n3 - tesoura\n")
    match escolhaDoJogador:
        case "1":
            match escolhaDoPC:
                case 1:
                    print("Empate\n")
                case 2:
                    print("Perdeu\n")
                    placarPC += 1
                case 3:
                    print("Ganhou\n")
                    placarJogador += 1
        case "2":
            match escolhaDoPC:
                case 1:
                    print("Ganhou\n")
                    placarJogador += 1
                case 2:
                    print("Empate\n")
                case 3:            
                    print("Perdeu\n")
                    placarPC += 1
        case "3":
            match escolhaDoPC:
                case 1:
                    print("Perdeu\n")
                    placarPC += 1
                case 2:
                    print("Ganhou\n")
                    placarJogador += 1
                case 3:
                    print("Empate\n")
        case _:
            print("Opção inválida escolha um número de 1-3")

    print(f"Placar PC: {placarPC}  \nPlacar {nomeJogador}: {placarJogador}\n")
    if placarPC == 3:
        print("\n O PC ganhou")
        fimDeJogo = True
    elif placarJogador ==3:
        print("\nVocê Ganhou")
        fimDeJogo = True