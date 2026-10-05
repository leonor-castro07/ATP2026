total = 0

print("1-Computador joga primeiro")
print("2-Computador joga em segundo")

opcao = int(input("Escolha um número:"))

if opcao == 1:

    computador = 10
    total = total + computador

    print("Computador jogou:", computador)
    print("Total:", total)

    while total < 100:
        jogador = int(input("Jogador, escolha um número de 1 a 10:"))

        while jogador < 1 or jogador > 10:
            jogador = int(input("Valor inválido. Escolha de 1 a 10:"))

        total = total + jogador
        print("Total:", total)

        if total == 100:
            print("Jogador ganhou.")
        print("Computador jogou:", computador)
        print("Total:", total)

        if total == 100:
            print("Computador ganhou.")
            break

        computador = 11 - jogador
        total = total + computador

        print("Computador jogou:", computador)
        print("Total:", total)

        if total == 100:
            print("Computador ganhou.")

elif opcao == 2:

    while total < 100:

        jogador = int(input("Jogador, escolha um número de 1 a 10:"))

        while jogador < 1 or jogador > 10:
            jogador = int(input("Valor inválido. Escolha de 1 a 10:"))

        total = total + jogador
        print("Total:", total)

        if total == 100:
            print("Jogador ganhou.")
            break 

    computador = 11 - jogador 
    total = total + computador

    print("Computador jogou:", computador)
    print("Total:", total)

    if total == 100:
        print("Computador ganhou.")
