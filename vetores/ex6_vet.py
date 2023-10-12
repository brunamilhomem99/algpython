# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1
def main():
    N = 10
    soma_vet = [0] * N # aloca 10 (N) espacos no vetor

    soma_vet[0] = int(input("Informe o primeiro valor do vetor: "))
    soma_vet[1] = int(input("Informe o segundo valor do vetor: "))

    for i in range(2, N):
        soma_vet[i] = soma_vet[i - 2] + soma_vet[i - 1]

    print(soma_vet)

if __name__ == "__main__":
    main()