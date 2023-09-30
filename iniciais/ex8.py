# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    num = int(input("Informe um valor inteiro: "))


    for i in range(num, -1, -1):
        print(i)

    print("\n")

    for i in range(0, num + 1):
        print(i)

if __name__ == "__main__":
    main()