def setOperatorLimits(limit, operator):
    return limit + 9999 if operator == '+' else limit - 9999

def randomLimits():
    return int(str(random.random())[2:6])

def setLimits():
    size = len(sys.argv)

    if size == 3:
        args = sys.argv[1]
        limit = int(sys.argv[2])

        if args == "li":
            linf = limit
            lsup = setOperatorLimits(linf, '+')
        else:
            lsup = limit
            linf = setOperatorLimits(lsup, '-')

    elif size == 1:
        linf = randomLimits()
        lsup = setOperatorLimits(linf, '+')
        
    else:
        print("╔═══════════════════════════════════════════════════════════════╗")
        print("║                           ATENÇÃO                             ║")
        print("║                                                               ║")
        print("║ Para executar este arquivo de forma correta é necessário que  ║")
        print("║ você escreva no terminal:                                     ║")
        print("║                                                               ║")
        print("║    py inputGenerator.py args1 args2                           ║")
        print("║                                                               ║")
        print("║ Tal que, args1 deve ser \"li\" para limite inferior ou \"ls\"     ║")
        print("║ para limite superior e args2 deve ser o número em inteiro que ║")
        print("║ você deseja definir para o limite escolhido. Por exemplo:     ║")
        print("║                                                               ║")
        print("║    py inputGenerator.py ls 501                                ║")
        print("║    py inputGenerator.py li 8888                               ║")
        print("║                                                               ║")
        print("║ Caso queira que o sistema defina os limites, basta:           ║")
        print("║                                                               ║")
        print("║    py inputGenerator.py                                       ║")
        print("║                                                               ║")
        print("╚═══════════════════════════════════════════════════════════════╝\n")
        exit()
    return linf, lsup

import random
import sys

linf, lsup = setLimits()

print("\nSeu intervalo é [%d, %d]" %(linf, lsup))

# Cria o conjunto de 10 mil números
group = [str(x) for x in range(linf, lsup + 1)]

# Embaralha o conjunto
random.shuffle(group)

# Converte o conjunto para ser dado de entrada para o arquivo input.txt
data = " ".join(group)

# Abre o arquivo input.txt e cria se ainda não existir para leitura e ecrita
file = open("input.txt", "w+")

# Escreve os números no arquivo
file.write(data)

# Fecha o arquivo
file.close