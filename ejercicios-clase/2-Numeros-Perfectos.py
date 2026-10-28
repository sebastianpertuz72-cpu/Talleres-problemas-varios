while True:
    num = int(input("Introduzca su numero: "))
    sum = 0
    if num < 0:
        break
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print("Numero perfecto. ")
    else:
        print("Numero imperfecto")