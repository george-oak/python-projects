""" Rock Paper Scissors
----------------------------------------
"""
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
welcomeMsg = "¡Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock!"
userChoiceMsg = "Elige tu arma R -> Piedra, P -> Papel, T -> Tijera, L -> Lagarto, S -> Spock: "
userChoiceErrorMsg = "Por favor, no hagas tram: "
reference = {
    'R': 'Piedra',
    'P': 'Papel',
    'T': 'Tijera',
    'L': 'Lagarto',
    'S': 'Spock'
}
userVictories = 0
opponentVictories = 0
while (userVictories + opponentVictories < 5):
    print("\n")
    print (welcomeMsg)
    userChoice = input(userChoiceMsg)
    userChoiceRef = reference.get(userChoice.upper())
    if not re.match("[SsRrPpTtLl]", userChoice):
        print (userChoiceMsg)
        continue
    #Echo the user's choice
    print (f"Elegiste: {userChoiceMsg}")
    choices = ['R', 'P', 'S', 'T', 'L']
    opponenetChoice = random.choice(choices)
    opponenetChoiceRef = reference.get(opponenetChoice)
    print (f"Yo elegí: {opponenetChoiceRef}")

    if opponenetChoice == str.upper(userChoice):
        print ("¡Empate!")
        continue
    elif opponenetChoice == 'R' and userChoice.upper() in ['T', 'L']:
        opponentWins = True
    elif opponenetChoice == 'P' and userChoice.upper() in ['R', 'S']:
        opponentWins = True
    elif opponenetChoice == 'T' and userChoice.upper() in ['L', 'P']:
        opponentWins = True
    elif opponenetChoice == 'L' and userChoice.upper() in ['S', 'P']:
        opponentWins = True
    elif opponenetChoice == 'S' and userChoice.upper() in ['R', 'T']:
        opponentWins = True
    else:       
        opponentWins = False

    opponentWinsMsg = f'¡Yo gano! {opponenetChoiceRef} gana a {userChoiceRef}'
    opponentLoosesMsg = f'¡Tu ganas! {userChoiceRef} gana a {opponenetChoiceRef}'

    if opponentWins:
        opponentVictories += 1
        print (opponentWinsMsg)
        continue
    else:
        userVictories += 1
        print (opponentLoosesMsg)
        continue

print (f"¡Fin! Has logrado ganarme {str(userVictories)} veces.")