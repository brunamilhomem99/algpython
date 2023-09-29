# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    num = int(input("Informe um valor inteiro: "))

    if (num < 0):
        print("Branco")
    elif (0 <= num <= 100):
        print("Verde")
    elif (101 <= num <= 1000):
        print("Azul")
    else:
        print("Vermelho")

if __name__ == "__main__":
    main()