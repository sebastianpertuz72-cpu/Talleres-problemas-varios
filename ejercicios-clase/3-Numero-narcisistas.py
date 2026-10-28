def cant_digito(num):
    cont = 1
    while num // 10 != 0:
        cont += 1
        num = num // 10
    return cont

while True:
    num = int(input("Digite un numero para saber si es narcisista: "))

    num3 = num % 10
    casinum2 = num // 10
    num2 = casinum2 % 10
    casinum1 = casinum2 // 10
    num1 = casinum1 % 10

    elevacion = cant_digito(num)

    suma1 = num1 ** elevacion
    suma2 = num2 ** elevacion
    suma3 = num3 ** elevacion

    sum_tot = suma1 + suma2 + suma3

    if sum_tot == num:
        print("Es un numero narcisista")
    else:
        print("No es un numero narcisista")
    break

