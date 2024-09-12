import random

numero_sorteado = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe um número de 1 a 10: "))
    
    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
        break
    elif palpite > numero_sorteado:
        print("O número é menor.")
    else:
        print("O número é maior.")
    
    tentativas -= 1

if tentativas == 0:
    print(f"Você perdeu! O número era {numero_sorteado}.")