import os
os.system('cls' if os.name == 'nt' else 'clear')

# Clase EjerciciosClase que encapsula los ejercicios de la clase 

class EjerciciosClase:
    def __init__(self):
        pass

    def ejercicio1_clase(self):
        venta = float(input("Ingrese el precio del producto: "))

        if venta >= 10000: 
            descuento = 0.25

        else:
            descuento = 0

        isv = 0.15
        TotalCompra= venta - (venta * descuento)
        TotalCompra= TotalCompra + (TotalCompra * isv)
        print("El descuento es igual a: ", TotalCompra * descuento)
        print("El isv es igual a: ", venta * isv)
        print(f"El total de la compra por un producto es igual a: {TotalCompra}")

    def ejercicio2_clase(self):
        # programa que calcula la edad de una persona
        anio_nacimiento = int(input("ingrese su anio de nacimiento: "))

        anio = 2025 

        edad = anio - anio_nacimiento

        print("su edad es: ",edad)

        if edad >= 21:
            print(f"Tienes {edad} años, eres mayor de edad")
        else:
            if edad == 18:
                print(f"Tienes {edad} anios, eres ciudadano")
            print(f"Tienes {edad} anios, eres menor de edad")
    
    def ejercicio3_clase(self):
        for i in range(1,11):
            print(f"{5} x {i} = {5*i}")

    def ejercicio4_clase(self):
        # programa que muestra la tabla de multiplicar de un numero que elija el usuario
        t = int(input("ingrese una tabla de multiplicar: "))

        # ciclo for para imprimir la tabla de multiplicar que ingreso el usuario
        for i in range(1,11):
            print(f"{t} x {i} = {t*i}")

    def ejercicio5_clase(self):
        # Ciclo While con las tablas de multiplicar

        t = int(input("Ingrese una tabla de multiplicar: "))

        i = 1

        while i <= 10:
            print(f"{t} x {i} = {t * i}")
            i += 1

    def ejercicio6_clase(self):
        # operaciones arithmeticas con funciones

        # funcion suma
        def suma(a, b):
            return a + b

        # funcion resta
        def resta(a, b):
            return a - b

        # funcion multiplicacion
        def multiplicacion(a, b):
            return a * b

        # funcion division
        def division(a, b):
            return a / b

        # funcion potencia
        def potencia(a, b):
            return a ** b

        # funcion raiz
        def raiz(a):
            return a ** (1/2)


        # llamada a la funcion suma
        print(f"La suma es: {suma(1, 2)}")

        # llamada a la funcion resta
        print(f"La resta es: {resta(2, 1)}")

        # llamada a la funcion multiplicacion
        print(f"La multiplicacion es: {multiplicacion(2, 3)}")

        # llamada a la funcion division 
        print(f"La division es: {division(6, 3)}")

        # llamada a la funcion potencia
        print(f"La potencia es: {potencia(2, 3)}")

        # llamada a la funcion raiz
        print(f"La raiz es: {raiz(4)}")

    def ejercicio7_clase(self):
        # Funcion para calcular el isv y el descuento

        def obtener_descuento(venta):
            if venta >= 10000:
                return 0.25
            else:
                return 0

        def calcular_total(venta):
            isv = 0.15
            descuento = obtener_descuento(venta)
            total_sin_isv = venta - (venta * descuento)
            total_con_isv = total_sin_isv + (total_sin_isv * isv)

            print("El descuento es igual a:", venta * descuento)
            print("El ISV es igual a:", venta * isv)
            print("El total de la compra es:", total_con_isv)

        # Ejecución directa del programa
        venta = float(input("Ingrese el precio del producto: "))
        calcular_total(venta)

    def ejercicio8_condicionales(self):
        #condicionales en python 
        a = int(input("ingrese un numero: ")) 

        if a % 2 == 0:
            if a==0:
                print("es cero, no se puede clasificar como impar o par")
            else:
                print(f"{a} es par")

        else:
            print(f"{a} es impar")

    def ejercicio9_funciones(self):
        # funciones 

        # definicion de la funcion
        def mensaje(nombre):
            print(f"Hola {nombre}")

        def _PI():
            return 3.1416

        def suma(a, b):
            return a + b

        # llamada a la funcion
        mensaje("Gustavo")

        # calcular el diametro de un circulo
        r = 10 
        diametro = 2 * _PI() * r
        print(f"Diametro: {diametro}")

        # funcion suma
        print(f"funcion suma: {suma(1, 1)}")

    def ejercicio10_holamundo(self):
        # Holamundo en python
        print("Hola Mundo")  

    def ejercicio11_claseAnimal(self):
        class Animal:
            def __init__(self, nombre):
                self.nombre = nombre

            def comer(self):
                print(f"{self.nombre} Esta comiendo")


            def correr(self):
                print(f"{self.nombre} Esta corriendo")

        class Perro(Animal):
            def ladrar(self):
                print(f"{self.nombre} Esta ladrando")

        class Gato(Animal):
            def maullar(self):
                print(f"{self.nombre} Esta maullando")

        miPerrox = Perro("Canelito")

        miPerrox.ladrar()

        miPerrox.correr()

        migatox = Gato("Michi")
        migatox.maullar()
        migatox.correr()
        migatox.comer()

    def ejercicio12_claseOperaciones(self):
        class OperacionesAritmeticas:
            def __init__(self, a, b):
                self.a = a 
                self.b = b

            def suma(self):
                return self.a + self.b
            
            def resta(self):
                return self.a - self.b 
            
            def multiplicacion(self):
                return self.a * self.b 
            
            def division(self):
                return self.a / self.b

        MainOperaciones = OperacionesAritmeticas(10, 5)
        print(f"La suma es igual a: {MainOperaciones.suma()}")
        print(f"La resta es igual a: {MainOperaciones.resta()}")
        print(f"La multiplicacion es igual a: {MainOperaciones.multiplicacion()}")
        print(f"La division es igual a: {MainOperaciones.division()}")