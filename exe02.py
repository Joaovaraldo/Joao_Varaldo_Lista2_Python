jogador1 = int(input("Jogador 1, escolha 0 para Pedra, 1 para Papel ou 2 para Tesoura: "))
jogador2 = int(input("Jogador 2, escolha 0 para Pedra, 1 para Papel ou 2 para Tesoura: "))


if jogador1 not in [0, 1, 2] or jogador2 not in [0, 1, 2]:
    print("Opção inválida! Por favor, escolha 0 para Pedra, 1 para Papel ou 2 para Tesoura.")
else:

    opcoes = {0: "Pedra", 1: "Papel", 2: "Tesoura"}
    jogador1_escolha = opcoes[jogador1]
    jogador2_escolha = opcoes[jogador2]
 
    print(f"\nJogador 1 escolheu: {jogador1_escolha}")
    print(f"Jogador 2 escolheu: {jogador2_escolha}")

    if jogador1 == jogador2:
        print("Empate!")
    
    if jogador1 == 0 and jogador2 == 2:
        print("Jogador 1 venceu!")
    
    if jogador1 == 1 and jogador2 == 0:
        print("Jogador 1 venceu!")
    
    if jogador1 == 2 and jogador2 == 1:
        print("Jogador 1 venceu!")

    if jogador2 == 0 and jogador1 == 2:
        print("Jogador 2 venceu!")
    
    if jogador2 == 1 and jogador1 == 0:
        print("Jogador 2 venceu!")
    
    if jogador2 == 2 and jogador1 == 1:
        print("Jogador 2 venceu!")