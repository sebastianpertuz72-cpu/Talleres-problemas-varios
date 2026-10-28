temperatura = int(input("Cual es la temperatura en grados celcius? "))
while True:
    if temperatura < 26:
        print("Temperatura baja, suba la temperatura hasta minimo 23 C°")
        break
    elif temperatura > 34:
        print("Temperatura alta, baje la temperatura hasta minimo 34 C°")
        break  
    else:
        print("La temperatura es la adecuada mantenlo en", temperatura, "C°")
        break