def main():
    
    lista1 = []
    lista2 = []

    for i in range(5):
        lista1.append(int(input("Informe um valor inteiro: ")))

    for i in range(5):
        lista2.append(lista1[i] * 2)

    print(lista1)
    print(lista2)

if __name__== "__main__":
    main()