def abundantes (num):
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum > num

inicial = int(input("Digite un numero inicial: "))
final = int(input("Digite un numero final: "))

for i in range(inicial, final + 1):
    if abundantes(i):
        print(i)