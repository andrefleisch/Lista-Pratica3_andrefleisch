numeros = [2,4,7,2,3,3,1,0,2,6]
n_freq = 0
n_rep = 0
for n in numeros:
    if numeros.count(n) > n_freq:
        n_freq = numeros.count(n)
        n_rep = n
print(f"O número que mais se repetiu é o {n_rep} e ele foi repetido {n_freq} vezes")