import random

lista = []
opcao = -1

while opcao != 0:

    print("\n===== MENU =====")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

    opcao = int(input("Escolha uma opção: "))

    # 1 - Criar lista aleatória
    if opcao == 1:
        n = int(input("Quantos números quer na lista? "))

        lista = []

        for i in range(n):
            numero = random.randint(1, 100)
            lista.append(numero)

        print("Lista criada:", lista)

    # 2 - Ler lista introduzida pelo utilizador
    elif opcao == 2:
        n = int(input("Quantos números quer introduzir? "))

        lista = []

        for i in range(n):
            numero = int(input("Introduza um número: "))
            lista.append(numero)

        print("Lista criada:", lista)

    # 3 - Soma
    elif opcao == 3:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            soma = sum(lista)
            print("Soma:", soma)

    # 4 - Média
    elif opcao == 4:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            media = sum(lista) / len(lista)
            print("Média:", media)

    # 5 - Maior elemento
    elif opcao == 5:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            maior = max(lista)
            print("Maior elemento:", maior)

    # 6 - Menor elemento
    elif opcao == 6:
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            menor = min(lista)
            print("Menor elemento:", menor)

    # 7 - Verificar ordem crescente
    elif opcao == 7:
        crescente = True

        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                crescente = False

        if crescente:
            print("Sim, a lista está ordenada por ordem crescente.")
        else:
            print("Não, a lista não está ordenada por ordem crescente.")

    # 8 - Verificar ordem decrescente
    elif opcao == 8:
        decrescente = True

        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                decrescente = False

        if decrescente:
            print("Sim, a lista está ordenada por ordem decrescente.")
        else:
            print("Não, a lista não está ordenada por ordem decrescente.")

    # 9 - Procurar elemento
    elif opcao == 9:
        elemento = int(input("Que elemento pretende procurar? "))

        posicao = -1

        for i in range(len(lista)):
            if lista[i] == elemento:
                posicao = i

        print("Posição:", posicao)

    # 0 - Sair
    elif opcao == 0:
        print("Lista final:", lista)
        print("Programa terminado.")

    else:
        print("Opção inválida.")
