# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    N = 10
    Z = 5

    entrada = []
    media = []

    for i in range(N):
        entrada.append(int(input("Informe um valor inteiro: ")))

    for i in range( int(Z) ):
        media.append( (entrada[i] + entrada[i+5]/2) )

    print(entrada)
    print(media)

if __name__ == "__main__":
    main()