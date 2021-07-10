import random

lista = ["pedra", "papel", "tesoura"]

while True:
    pc = lista[random.randint(0, 2)]
    print("-" * 25)
    print("Digite sair para encerrar o programa")
    jogador = input("Pedra, Papel, Tesoura? : ")

    jogador = jogador.lower()

    if jogador == pc:
        print('empate')
    elif jogador == "pedra":
        if pc == "papel":
            print('Perdeu! O papel cobriu a pedra!')
        else:
            print("Venceu! A pedra esmagou a tesoura!")
    elif jogador == "papel":
        if pc == "tesoura":
            print("Perdeu! A tesoura cortou o papel!")
        else:
            print("Venceu! O papel cobriu a pedra!")
    elif jogador == "tesoura":
        if pc == "pedra":
            print("Perdeu! A pedra esmagou a tesoura")
        else:
            print("Venceu! A tesoura cortou o papel")
    elif jogador == "sair":
        break
    else:
        print("Escolha uma palavra valida!")
