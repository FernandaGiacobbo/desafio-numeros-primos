numero = int(input("Digite um número neste campo: "))

def is_prime(numero):
    if numero < 2:
        print("Falso")
        return
    for i in range(2, numero):
        if numero % i == 0:
            print("Falso")
            return
    print("Verdadeiro")

is_prime(numero)