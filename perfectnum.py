def isPerfect(num):
    soma = 0
    for i in range(1, n):
        if(n % i == 0):
            soma = soma + i
    if (soma == n):
        print("Perfeito: "+str(n))
    # else:
    #     print("Não perfeito: "+str(n))
    return

#n = int(input("DIGITE O NÚMERO: "))

for n in range(1, 10000):
    isPerfect(n)