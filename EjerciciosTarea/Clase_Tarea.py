import os
os.system('cls' if os.name == 'nt' else 'clear')

# Clase para agrupar los ejercicios de la tarea de avanzada y luego llamarla desde el main

class EjerciciosTarea:
    def __init__(self):
        pass

    # Ejercicio 1: Imprimir "Hola mundo"
    def ejercicio1_tarea(self):
        print("Hola mundo")

    # Ejercicio 2: suma de dos numeros
    def ejercicio2_tarea(self):
        # Definicion de variables
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))

        # Sumar los dos numeros
        suma = n1 + n2

        # print para mostrar la suma de los numeros
        print(f"La suma de {n1} + {n2} es = {suma}") 

    # Ejercicio 3: calculo del area de un rectangulo
    def ejercicio3_tarea(self):
        # Definicion de variables
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))

        # Calcular el area del rectangulo
        area = base * altura

        # print para mostrar el area del rectangulo
        print(f"El area del rectangulo es = {area}")

    # Ejercicio 4: numero positivo, negativo o cero
    def ejercicio4_tarea(self):
        numero = int(input("Ingrese un numero: "))

        # Condicionales para determinar si el numero es positivo, negativo o cero
        if numero > 0:
            print(f"El numero {numero} es positivo")
        else:
            if numero < 0:
                print(f"El numero {numero} es negativo")
            else:
                print(f"El numero {numero} es cero")

    # Ejercicio 5: numero par o impar
    def ejercicio5_tarea(self):
        numero = int(input("Ingrese un numero: "))

        # Condicionales para determinar si el numero es par o impar
        if numero % 2 == 0:
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} es impar")

    # Ejercicio 6: mayor de 3 numeros
    def ejercicio6_tarea(self):
        # Definicion de variables
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        n3 = int(input("Ingrese el tercer numero: "))

        # Condicionales para determinar cual es el mayor de los 3 numeros
        if n1 > n2 and n1 > n3:
            print(f"El numero mayor es {n1}")
        elif n2 > n1 and n2 > n3:
            print(f"El numero mayor es {n2}")   
        else:
            print(f"El numero mayor es {n3}")

    # Ejercicio 7: ciclo for del 1 al 10
    def ejercicio7_tarea(self):
        # Ciclo for para mostrar la cuenta del 1 al 10
        for i in range(1, 11):
            print(i)

    # Ejercicio 8: tabla de multiplicar
    def ejercicio8_tarea(self):
        # Definicion de variable 
        t = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

        # Ciclo for para mostrar la tabla de multiplicar
        for i in range(1, 11):
            print(f"{t} x {i} = {t * i}")

    # Ejercicio 9: suma del 1 a un numero ingresado por el usuario con un ciclo for
    def ejercicio9_tarea(self):
        # Definicion de variable
        n = int(input("Ingrese un numero para ver la suma del 1 a ese numero: "))

        # Inicializar la variable suma
        suma = 0
        # Ciclo for para sumar del 1 a n
        for i in range(1, n + 1):
            suma += i 

        # Mostrar el resultado
        print(f"La suma del 1 al {n} es: {suma}")

    # Ejercicio 10: dibujar con asteriscos
    def ejercicio10_tarea(self):
        # Solicita al usuario un número
        n = int(input("Ingrese un número: "))

        # Usa un ciclo for para dibujar una línea de N asteriscos
        for i in range(n):
            print("*", end="")

        print()  # Para agregar una nueva línea al final