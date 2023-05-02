for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

        # en un bucle con funcion for in y range que establece donde parar se tiene que poner un numero mas para que este incluido el 100 con if es una condicion, con el elif verifico las demas condiciones por que if solo verifica una vez, utilizo and para cuando ambos condicionales son ciertos. en resumen es un bucle fon in con operadores.