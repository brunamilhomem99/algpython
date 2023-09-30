# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    limite = int(input("Informe um valor limite: "))
    incremento = int(input("Informe um valor incremento: "))

    for i in range(0, limite, incremento):
        print(i)

if __name__ == "__main__":
    main()