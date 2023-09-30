def main():
    vet1 = []
    vet2 = []

    for i in range(5):
        vet1.append(int(input("Informe um valor inteiro: ")))

    for i in range(5):
        vet2.append(vet1[i])

    vet2.reverse()

    print(vet1)
    print(vet2)

if __name__ == "__main__":
    main()