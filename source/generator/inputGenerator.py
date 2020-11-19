def setOperatorLimits(limit, operator):
    return limit + 9999 if operator == '+' else limit - 9999

def randomLimits():
    return int(str(random.random())[2:6])

def setLimits(option):
    if option == 1 or option == 3:
        linf = int(input("Por favor, insira o limite inferior: ")) if option == 1 else randomLimits()
        lsup = setOperatorLimits(linf, '+')

    else:
        lsup = int(input("Por favor, insira o limite superior: ")) if option == 2 else randomLimits()
        linf = setOperatorLimits(lsup, '-')

    return linf, lsup


import random

print("╔════════════════════════════════════════════════╗")
print("║                      MENU                      ║")
print("║                                                ║")
print("║ Escolha uma opção:                             ║")
print("║ 1- Inserir apenas o limite inferior            ║")
print("║ 2- Inserir apenas o limite superior            ║")
print("║ 3- Deixar o sistema escolher o limite inferior ║")
print("║ 4- Deixar o sistema escolher o limite superior ║")
print("║                                                ║")
print("╚════════════════════════════════════════════════╝\n")

linf, lsup = setLimits(int(input()))

print("\nSeu intervalo é [%d, %d]" %(linf, lsup))