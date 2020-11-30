# Relatório

## Linguagem utilizada

> Utilizamos duas linguagens diferentes no código, uma para o experimento em si, que é a implementação das árvores binária de busca e AVL e também o programa que realiza as comparações do experimento. E outra linguagem para implementação do gerador do conjunto dos 10 mil números, e dos conjuntos menor, maior e interno.

### Experimento

- Dart

>Eu, Heitor, decidi implementar o experimento utilizando Dart porque anteriormente entrei em contato com a língua e gostei muito dela, tem as capacidades de uma linguagem orientada à objetos sem complicações desnecessárias e ainda mantendo a organização do código. Vi neste trabalho a primeira oportunidade de usar minha linguagem favorita na UFT.

### Gerador

- Python

> Eu, Thaís, escolhi utilizar Python neste trabalho pois me adaptei bem com a linguagem e encontrei uma ótima forma de praticar e aprimorar mais os meus conhecimentos com esta. 

## Fonte dos algoritmos

### Experimento

- A implementação foi feita por mim, tomando como base a demonstração teórica nas aulas.

### Gerador

- O gerador foi elaborado por mim, com auxílio da documentação de Python.

## Dados

### Intervalo dos dados

> Na execução de exemplo, enviada neste trabalho, estão anexos os arquivos que contém os dados utilizados. Para os 10 mil números, temos o seguinte intervalo:

- **Limite inferior:** 1
- **Limite superior:** 10000

### Conjuntos de dados testados

|      | Conjunto Menor | Conjunto Maior | Conjunto Interno |
| ---- | -------------- | -------------- | ---------------- |
| 1    | 4845           | 7477           | 1                |
| 2    | 4126           | 6796           | 2                |
| 3    | 2998           | 6823           | 3                |
| 4    | 2962           | 7173           | 4                |
| 5    | 1846           | 6736           | 5                |
| 6    | 4807           | 6168           | 6                |
| 7    | 4678           | 9760           | 7                |
| 8    | 3884           | 7851           | 8                |
| 9    | 9444           | 9128           | 9                |
| 10   | 105            | 5776           | 10               |
| 11   | 4379           | 5402           | 11               |
| 12   | 426            | 9771           | 12               |
| 13   | 1115           | 9611           | 13               |
| 14   | 2580           | 6962           | 14               |
| 15   | 439            | 8116           | 15               |
| 16   | 3500           | 9542           | 16               |
| 17   | 4824           | 9852           | 17               |
| 18   | 24             | 9422           | 18               |
| 19   | 3442           | 5664           | 19               |
| 20   | 2026           | 8515           | 20               |
| 21   | 3728           | 6500           | 21               |
| 22   | 4407           | 9400           | 22               |
| 23   | 4119           | 5454           | 23               |
| 24   | 2525           | 7052           | 24               |
| 25   | 1799           | 5408           | 25               |
| 26   | 4506           | 9107           | 9976             |
| 27   | 3349           | 5535           | 9977             |
| 28   | 320            | 9396           | 9978             |
| 29   | 1207           | 7322           | 9979             |
| 30   | 460            | 6658           | 9980             |
| 31   | 1911           | 6911           | 9981             |
| 32   | 3350           | 5210           | 9982             |
| 33   | 3331           | 5222           | 9983             |
| 34   | 1853           | 8098           | 9984             |
| 35   | 3361           | 9620           | 9985             |
| 36   | 209            | 6140           | 9986             |
| 37   | 2118           | 6350           | 9987             |
| 38   | 4129           | 8667           | 9988             |
| 39   | 3764           | 6490           | 9989             |
| 40   | 732            | 8302           | 9990             |
| 41   | 3934           | 7053           | 9991             |
| 42   | 1580           | 8442           | 9992             |
| 43   | 2067           | 9684           | 9993             |
| 44   | 921            | 8989           | 9994             |
| 45   | 4940           | 6617           | 9995             |
| 46   | 1265           | 8082           | 9996             |
| 47   | 4186           | 5938           | 9997             |
| 48   | 3382           | 8059           | 9998             |
| 49   | 3984           | 7434           | 9999             |
| 50   | 768            | 6080           | 10000            |

## Gráfico Comparativo

![Comparação de médias entre ABB e AVL](C:\Users\thais\Downloads\Comparação de médias entre ABB e AVL.png)

## Utilização

### Experimento

>Para utilizar o programa do experimento, você necessita executar o comando `dart science.dart INPUT SEARCH`, sendo **INPUT** o caminho para o arquivo input.txt e **SEARCH** o caminho para o arquivo search.txt.
>
>Lembre-se de utilizar o comando acima dentro da pasta onde se encontra o arquivo *science.dart*, do contrário o programa não irá executar.

### Gerador

> Para o programa do gerador ser executado corretamente, é necessário inserir o comando `py inputGenerator.py args1 args2`, tal que, **args1** deve ser **li**, para o limite inferior, ou **ls** para o limite superior, e **args2** deve ser o número em inteiro que você deseja definir para o limite escolhido.
>
> Caso queira que o sistema defina os limites, basta não informar **ags1** e **args2**.
>
> Não esqueça de utilizar o comando acima dentro da pasta onde se encontra o arquivo inputGenerator.py, se não o programa não será executado.