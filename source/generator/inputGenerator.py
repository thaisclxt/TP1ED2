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

# Cria o conjunto de 10 mil números
group = [str(x) for x in range(linf, lsup + 1)]

# Embaralha o conjunto
random.shuffle(group)

# Converte o conjunto para ser dado de entrada para o arquivo input.txt
data = " ".join(group)
print(data)

# Abre o arquivo input.txt e cria se ainda não existir para leitura e ecrita
file = open("input.txt", "w+")

# Escreve os números no arquivo
file.write(data)

# Fecha o arquivo
file.close