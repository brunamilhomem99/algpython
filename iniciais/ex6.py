# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    x = int(input("Informe um valor x: "))
    y = int(input("Informe um valor para y: "))
    z = int(input("Informe um valor para z: "))

    maior = x
    menor = x

    # se y ou z for menor que o "menor" a variavel eh atualizada
    if (y < menor):
        menor = y
        if (z < menor):
            menor = z
    elif (z < menor):
        menor = z

    # mesma logica para achar o maior valor
    if (y > maior):
        maior = y
        if (z > maior):
            maior = z
    if (z > maior):
        maior = z

    print("Maior valor: ", maior)
    print("Menor valor: ", menor)
    
if __name__ == "__main__":
    main()