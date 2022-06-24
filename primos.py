'''ímpar'''

x = ""

while x != 0:
    x = int(input("Digite um número que deseja verificar se é primo: "))
    for i in range(x):
        print('-'*50)
        i += 1
        print("{} é divisivel por {}?".format(x, (i)))
        if (x % i) == 0:
            print("SIM!, {} é divisivel por {}".format(x, (i)))
        else:
            print("NÃO, {} não é divisivel por {}".format(x, (i)))
        if (i % 2) == 0:
            print("-{} não é primo".format(i))
        else:
            print("-{} é primo".format(i))
        print("Resultado da divisão {} / {} = {:.1f}".format(x, i, x/i))
    x = int(input("Digite qualquer número OU pressione 0 para terminar o programa: "))
print("FIM")