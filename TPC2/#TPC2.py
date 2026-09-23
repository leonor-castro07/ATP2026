# TPC2
## Modalidade 1
from random import radint 
computador = randint(0, 100)
jogador = int(input("Qual o número em que pensei?"))
tentativas = 0

while jogador != computador:
  if jogador < computador:
    print("O número em que pensei é maior.")
    jogador = int(input("Qual o número em que pensei?"))
    tentativas = tentativas + 1
  
  elif jogador > computador:
    print("O número que pensei é menor.")
    jogador = int(input("Qual o número em que pensei?"))
    tentativas = tentativas + 1

tentativas = tentativas + 1
print(f"Acertou em {tentativas} tentativas"}

## Modalidade 2
print("Pense num número entre 0 e 100, se eu não acertar, diga-me se o número que escolheu é maior ou menor".)
min = 0
max = 100
tentativas = 0
palpite = int((min + max)/2)
resposta = input("Avalia o meu palpite")

while resposta != "acertou":
  if resposta == "maior":
    min = palpite + 1
    palpite = int((min + max)/2)
    print(palpite)
    resposta = input("Avalia o meu palpite")
    tentativas = tentativas + 1
  elif resposta == "menor":
    max = palpite - 1
    palpite = int((min + max)/2)
    print(palpite)
    resposta = input("Avalia o meu palpite")
    tentativas = tentativas + 1
tentativas = tentativas + 1
print(f"Acertei em {tentativas} tentativas.")
    

