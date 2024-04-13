intervalo = [10,11,12,13,14,15,16,17,18,19,20]
somaIntervalo = 0
somaFora = 0
for i in range(0,10):
    n = float(input("Digite um número: "))
    if n in intervalo:
        somaIntervalo += 1
    else:
        somaFora += 1
print(f"Quantidade de números dentro do intervalo: {somaIntervalo}\nQuantidade de números fora do intervalo: {somaFora}")