'''impar/par'''
x = ""
while x != 0:
    x = int(input("Digite um número que deseja verificar se é ímpar ou par: "))
    if (x % 2) == 0:
        print("{} PAR".format(x))
    else:
        print("{} {{{{impar".format(x))
    x = int(input("Digite qualquer número OU pressione 0 para terminar o programa: "))
print("FIM")