def main():
    ref = int(input("Informe um valor inteiro positivo: "))

    if ref > 0:
        v1 = int(input("Informe o primeiro valor: "))
        v2 = int(input("Informe o segundo valor: "))
        v3 = int(input("Informe o terceiro valor: "))

        soma = v1 + v2 + v3

        if (soma > ref):
            for i in range(1, soma + 1):
                print(i)
        else:
            for i in range(1, ref + 1):
                print(i)

    else:
        print("O valor de referencia deve ser positivo...")

if __name__ == "__main__":
    main()