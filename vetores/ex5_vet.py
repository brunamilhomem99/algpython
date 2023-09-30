def main():
    N = 7
    valores = []

    for i in range(N):
        valores.append( int( input("Oi Bruna!:") ) )

    menor = valores[0]
    maior = valores[0]

    for i in range(N):
        if (valores[i] < menor):
            menor = valores[i]
        if (valores[i] > maior):
            maior = valores[i]

    print("Menor valor: ", menor)
    print("Maior valor: ", maior)

if __name__ == "__main__":
    main()