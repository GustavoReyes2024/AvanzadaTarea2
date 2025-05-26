import os
os.system('cls' if os.name == 'nt' else 'clear')

# creacion del main donde llamaremos a todos los ejercicios de la clase y de la tarea
from Clase_EjerciciosClase import EjerciciosClase
from Clase_Tarea import EjerciciosTarea

ejercicios_clase = EjerciciosClase()
ejercicios_tarea = EjerciciosTarea()

def limpia_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

menu = ""

while menu != "0":
    print("Menu de ejercicios de Opciones")
    print("1. Ejercicios de la clase")
    print("2. Ejercicios de la tarea")
    print("0. Salir")
    menu = input("Seleccione una opcion: ")

    match menu:
        case "1":
            print("Ejercicios de la clase")
            print("1. Ejercicio 1 Descuento y ISV")
            print("2. Ejercicio 2 Calculo de edad")
            print("3. Ejercicio 3 Tabla de multiplicar del 5")
            print("4. Ejercicio 4 Tabla de multiplicar personalizada")
            print("5. Ejercicio 5 Tabla de multiplicar con ciclo while")
            print("6. Ejericio 6  operaciones aritmeticas")
            print("7. Ejercicio 7 Descuento y ISV con funciones")
            print("8. Ejercicio 8 numero par, impar o cero")
            print("9. Ejercicio 9 calculo diametro de un circulo y suma")
            print("10. Ejercicio 10 imprimir un hola mundo")
            print("11. Ejercicio 11 Clase Animal")
            print("12  Ejercicio 12 Clase Operaciones")
            opcion = input("Seleccione una opcion: ")
            limpia_consola()

            match opcion:
                case "1":
                    ejercicios_clase.ejercicio1_clase()
                    input("\nPresione Enter para continuar...")


                case "2":
                    ejercicios_clase.ejercicio2_clase()
                    input("\nPresione Enter para continuar...")


                case "3":
                    ejercicios_clase.ejercicio3_clase()
                    input("\nPresione Enter para continuar...")


                case "4":
                    ejercicios_clase.ejercicio4_clase()
                    input("\nPresione Enter para continuar...")


                case "5":
                    ejercicios_clase.ejercicio5_clase()
                    input("\nPresione Enter para continuar...")

                case "6":
                    ejercicios_clase.ejercicio6_clase()
                    input("\nPresione Enter para continuar...")

                case "7":
                    ejercicios_clase.ejercicio7_clase()
                    input("\nPresione Enter para continuar...")

                case "8":
                    ejercicios_clase.ejercicio8_condicionales()
                    input("\nPresione Enter para continuar...")

                case "9":
                    ejercicios_clase.ejercicio9_funciones()
                    input("\nPresione Enter para continuar...")

                case "10":
                    ejercicios_clase.ejercicio10_holamundo()
                    input("\nPresione Enter para continuar...")

                case "11":  
                    ejercicios_clase.ejercicio11_claseAnimal()
                    input("\nPresione Enter para continuar...")

                case "12":
                    ejercicios_clase.ejercicio12_claseOperaciones()
                    input("\nPresione Enter para continuar...")

                case _:
                    print("Opcion no valida")

        case "2":
            print("Ejercicios de la tarea")
            print("1. Ejercicio 1 hola mundo")
            print("2. Ejercicio 2 suma de dos numeros")
            print("3. Ejercicio 3 calculo del area de un rectangulo")
            print("4. Ejercicio 4 numero positivo, negativo o cero")
            print("5. Ejercicio 5 numero par o impar")
            print("6. Ejercicio 6 mayor de 3 numeros")
            print("7. Ejercicio 7 ciclo for del 1 al 10")
            print("8. Ejercicio 8 tabla de multiplicar")
            print("9. Ejercicio 9 suma del 1 a un numero ingresado por el usuario con un ciclo for")
            print("10. Ejercicio  10 dibujar con asteriscos")
            opcion = input("Seleccione una opcion: ")
            limpia_consola()

            match opcion:
                case "1":
                    ejercicios_tarea.ejercicio1_tarea()
                    input("\nPresione Enter para continuar...")

                case "2":
                    ejercicios_tarea.ejercicio2_tarea()
                    input("\nPresione Enter para continuar...")

                case "3":
                    ejercicios_tarea.ejercicio3_tarea()
                    input("\nPresione Enter para continuar...")

                case "4":
                    ejercicios_tarea.ejercicio4_tarea()
                    input("\nPresione Enter para continuar...")

                case "5":
                    ejercicios_tarea.ejercicio5_tarea()
                    input("\nPresione Enter para continuar...")

                case "6":
                    ejercicios_tarea.ejercicio6_tarea()
                    input("\nPresione Enter para continuar...")


                case "7":
                    ejercicios_tarea.ejercicio7_tarea()
                    input("\nPresione Enter para continuar...")

                    
                case "8":
                    ejercicios_tarea.ejercicio8_tarea()
                    input("\nPresione Enter para continuar...")


                case "9":
                    ejercicios_tarea.ejercicio9_tarea()
                    input("\nPresione Enter para continuar...")


                case "10":
                    ejercicios_tarea.ejercicio10_tarea()
                    input("\nPresione Enter para continuar...")

                case _:
                    print("Opcion no valida")

        case "0":
            print("Saliendo del programa...")
        case _:
            print("Opcion no valida, intente nuevamente")