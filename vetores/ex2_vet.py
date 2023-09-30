# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():

    lista = []

    for i in range(5):
        lista.append(int(input("Informe um valor inteiro: ")))

    for i in range(5):
        lista[i] = lista[i] * 2

    for i in range(5):
        print(lista[i])


if __name__ == "__main__":
    main()