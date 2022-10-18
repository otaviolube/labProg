import random

numeroAleatorio = random.randint(1, 10)

print("Pensei num número. Tente acertar!")

acertou = False # O jogador não acertou
tentativas = 0  # O jogador tem zero tentativas

while(acertou == False and tentativas < 3):
  palpite = int(input("Digite o seu palpite:"))
  print("Você falou o palpite: " + str(palpite))
  if(palpite == numeroAleatorio):
    print("Você é sinistro! Parabéns!")
    acertou = True
  elif palpite > numeroAleatorio:
    print("Você chutou muito alto. Tente novamente")
    tentativas = tentativas + 1
    print("Numero de tentativas: " + str(tentativas))
  elif palpite < numeroAleatorio:
    print("Você chutou muito baixo. Tente novamente")
    tentativas = tentativas + 1
    print("Numero de tentativas: " + str(tentativas))