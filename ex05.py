somaImpar = 0
somaPar = 0
for i in range(0,10):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        somaPar += 1
    else:
        somaImpar += 1
print(f"A quantidade de números ímpares é: {somaImpar}\nA quantidade de números pares é: {somaPar}")
