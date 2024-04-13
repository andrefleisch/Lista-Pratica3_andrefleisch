divisores = []
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    divisores.append(i)
    if n % i != 0:
        divisores.remove(i)
print(divisores)