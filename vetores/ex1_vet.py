# UFMT - Ciencia da computacao
# Programacao de computadores
# Prof. Ivairton
# 
# Exercicio de programacao 1

def main():
    lista = [] # cria uma lista vazia

    valor = 1 # Primeiro valor da contagem a ser armazenado na lista
    for i in range(5):
        lista.append(valor) # add o valor na lista
        valor += 1

    # imprime os valores armazenados na lista
    for i in lista:
        print(i)

if __name__ == "__main__":
    main()