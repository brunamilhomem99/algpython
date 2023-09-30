def main():
    ref = int(input("Informe um valor de referencia: "))

    if ref > 0:
        for i in range(1, 11):
            print(ref, "x", i, "=", ref * i)
    else:
        print("O valor de entrada deve ser positivo!")

if __name__ == "__main__":
    main()