class Group:
    def __init__(self, args):
        self.setLimits(args)
        self.generateNumbers()
        self.calculateMedia()

    def setOperatorLimits(self, limit, operator):
        return limit + 9999 if operator == '+' else limit - 9999

    def randomLimits(self):
        return int(str(random.random())[2:6])

    def setLimits(self, args):
        size = len(args)

        if size == 3:
            limit = int(args[2])

            if args[1] == "li":
                self.linf = limit
                self.lsup = self.setOperatorLimits(self.linf, '+')
            else:
                self.lsup = limit
                self.linf = self.setOperatorLimits(self.lsup, '-')

        elif size == 1:
            self.linf = self.randomLimits()
            self.lsup = self.setOperatorLimits(self.linf, '+')
            
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

    def generateNumbers(self):
        self.generatedNumbers = [x for x in range(self.linf, self.lsup + 1)]
    
    def calculateMedia(self):
        self.media = (self.linf + self.lsup) // 2

    def shuffleNumber(self):
        random.shuffle(self.generatedNumbers)

import random