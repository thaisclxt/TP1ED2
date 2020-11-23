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
    
def principalGroup(linf, lsup):
    return [x for x in range(linf, lsup + 1)]

def calculatesMedia(linf, lsup):
    media = (linf + lsup) // 2
    print("A média entre o limite inferior e o limite superior é ", media)
    return media


def group1and2(group, media):
    smallerGroup, largerGroup = [], []
    cont1, cont2 = 0, 0
    for x in group:
        if x <= media and cont1 < 50:
            smallerGroup.append(x)
            cont1 += 1

        elif x >= media and cont2 < 50:
            largerGroup.append(x)
            cont2 += 1
    
    
    print(len(smallerGroup))
    print(smallerGroup)

    print(len(largerGroup))
    print(largerGroup)

    return smallerGroup, largerGroup

def convertToStr(*group):
    # Transforma os números em str
    for g in group:
        data = [str(x) for x in group]

    # Separa os números com um espaço entre eles
    return " ".join(data)

def txt(file, data):
    # Escreve os números no arquivo
    file.write(data)

    # Fecha o arquivo
    file.close

import random
import sys

linf, lsup = setLimits()

print("\nSeu intervalo é [%d, %d]" %(linf, lsup))

# Cria o conjunto de 10 mil números inteiros
group = principalGroup(linf, lsup)

# Embaralha o conjunto
random.shuffle(group)

# Calcula a média do limite inferior e superior
media = calculatesMedia(linf, lsup)

# Cria o conjunto menor e o conjunto maior
smallerGroup, largerGroup = group1and2(group, media)

# Abre o arquivo input.txt e cria se ainda não existir para leitura e ecrita e escreve os dados
txt(open("input.txt", "w+"), convertToStr(group))

# Abre o arquivo search.txt e cria se ainda não existir para leitura e ecrita e escreve os dados
txt(open("search.txt", "w+"), convertToStr(smallerGroup, largerGroup))