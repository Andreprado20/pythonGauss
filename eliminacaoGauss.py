
# Função para pegar a matriz e aplicar a eliminação gaussiana
def eliminacao(A,b):
    n = len(b)
    x = [0]*n
    for k in list(range(1,n,1)):
        for i in list(range(k+1,n+1,1)):
            m = float("{:.2f}".format(A[i-1][k-1]/A[k-1][k-1]))
            A[i-1][k-1] = 0
            b[i-1] = b[i-1] - m*b[k-1]
            

            for j in list(range(k+1,n+1,1)):
                A[i-1][j-1] = float("{:.2f}".format(A[i-1][j-1] - m*A[k-1][j-1]))
                

    return A,b

# Função para pegar a matriz já triangulada e resolver o sistema:
def solveUpperTriangular(matrizTriangular, matrizResultados):
    n = len(matrizResultados)
    x = [0]*n
    x[n-1] = matrizResultados[n-1]/matrizTriangular[n-1][n-1]

    for i in list(range(n-1,0,-1)):
        s = 0
        for j in list(range(i+1,n+1,1)):
            s = s + matrizTriangular[i-1][j-1] * x[j-1]
        
        x[i-1] = float("{:.2f}".format((matrizResultados[i-1]-s)/(matrizTriangular[i-1][i-1])))

    return x

# Função que vai ler a matriz do usuário e realizar a operação chamando as funções anteriores:
def Gauss():
    # equations = input("Digite o número de equações no sistema: ");
    # variables = input("Digite o número de variáveis no sistema: ");
    print("Digite os elementos da matriz A44: ")
    a11 = int(input("Digite o elemento A[1,1]: "));
    a12 = int(input("Digite o elemento A[1,2]: "));
    a13 = int(input("Digite o elemento A[1,3]: "));
    # a14 = int(input("Digite o elemento A[1,4]: "));
    a21 = int(input("Digite o elemento A[2,1]: "));
    a22 = int(input("Digite o elemento A[2,2]: "));
    a23 = int(input("Digite o elemento A[2,3]: "));
    # a24 = int(input("Digite o elemento A[2,4]: "));
    a31 = int(input("Digite o elemento A[3,1]: "));
    a32 = int(input("Digite o elemento A[3,2]: "));
    a33 = int(input("Digite o elemento A[3,3]: "));
    # a34 = int(input("Digite o elemento A[3,4]: "));
    # a41 = int(input("Digite o elemento A[4,1]: "));
    # a42 = int(input("Digite o elemento A[4,2]: "));
    # a43 = int(input("Digite o elemento A[4,3]: "));
    # a44 = int(input("Digite o elemento A[4,4]: "));
    b1 = int(input("Digite o elemento B[1]: "));
    b2 = int(input("Digite o elemento B[2]: "));
    b3 = int(input("Digite o elemento B[3]: "));
    # b4 = int(input("Digite o elemento B[4]: "));

    # matrizA = [
    #     [a11,a12,a13,a14],
    #     [a21,a22,a23,a24],
    #     [a31,a32,a33,a34],
    #     [a41,a42,a43,a44]
    # ]
    # matrizB = [b1,b2,b3,b4]

    matrizA = [
        [a11,a12,a13],
        [a21,a22,a23],
        [a31,a32,a33]
    ]
    matrizB = [b1,b2,b3]
 
    print("Matriz A: ")
    matrix = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrizA])
    print(matrix)

    print("Matriz B: ", matrizB)

    matrizAi,matrizBi = eliminacao(matrizA, matrizB)
    resultado = solveUpperTriangular(matrizAi, matrizBi)

    array = ["x1","x2","x3","x4"]
      
    print("\nSoluções: ")
    for l in range(len(resultado)):
        print('%s = %.2f' % (array[l],resultado[l]))

# Função "main" que seleciona entre fazer a função ou sair do sistema:
def mainFunction(selecionado):
    match selecionado:
        case 1: Gauss()
        case 2: print("Goodbye...")

 
# Implementação do loop:
selecionado = 1

while(selecionado < 2):
    print("-------------------------------------------------------------------------")
    print("Olá! O que deseja fazer?")
    selecionado = int(input("Digite 1 para usar a função em um sistema ou 2 para sair: "))
    print("-------------------------------------------------------------------------")
    mainFunction(selecionado)
