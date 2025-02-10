n = int(input("Digite a quantidade de números: "))
resultado = "Não"
for _ in range(n):
    numero = input("Digite um número: ")
    if any(numero[i] == numero[i+1] for i in range(len(numero)-1)):
        resultado = "Sim"
print(resultado)