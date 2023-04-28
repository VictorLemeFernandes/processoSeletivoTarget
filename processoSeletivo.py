def exercicio01():
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k = k + 1
        soma = soma + k
    
    print("O valor da variável soma é: ", end="")
    print(soma)

exercicio01()

def exercicio02(num):
    ultimo = 1
    penultimo = 0
    cont = 0
    if num == 0 or num == 1:
        print("O numero pertence a sequencia")
    else:
        cont = 2
        print(penultimo, end=" ")
        print(ultimo, end=" ")
        while cont < num:
            atual = penultimo + ultimo
            print(atual, end=" ")
            if num == atual:
                print("\nO numero pertence a sequencia")
                break
            penultimo = ultimo
            ultimo = atual
            cont += 1


exercicio02(8)


"""
Exercicio 3:

a) 9
b) 128
c) 49
d) 100
e) 13
f) 200



Exercicio 4:

Nenhum estará mais próximo de Ribeirão Preto, os dois estarão à mesma distância.

Se o carro percorreu 80 km saindo de Ribeirão e ele cruza com o caminhão nesse momento, isso significa que faltam 80 km para o caminhão chegar até Ribeirão preto.
"""

def exercicio05(str):
    strFinal = ""
    for i in range(len(str) -1, -1, -1):
        strFinal += str[i]
    
    print(strFinal)

exercicio05('victor')
