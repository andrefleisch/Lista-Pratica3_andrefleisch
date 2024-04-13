n = int(input("Digite um número de 1 a 10: "))
while n <= 0 or n > 10:
    print("Número inválido")
    n = int(input("Digite um número de 1 a 10: "))
    continue
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")