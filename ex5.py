# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    num = int(input("Informe um valor inteiro: "))

    if (num % 2 == 0):
        print("Divisivel por 2")
    elif (num % 3 == 0):
        print("Divisivel por 3")
    elif (num % 5 == 0):
        print("Divisivel por 5")
    elif (num % 10 == 0):
        print("Divisivel por 10")

    else:
        print("Nao eh divisivel por nenhum valor!")

if __name__ == "__main__":
    main()