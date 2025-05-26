'''Evaluación práctica estructura de datos lineales
Ejercicio: Separación de elementos usando Pila y Cola

Objetivo:
Dado una cola con elementos y una pila vacía, desarrollar un programa que procese la cola de forma que:
	Los elementos que se encuentran en posiciones pares (0, 2, 4, ...) permanezcan en la cola.
	Los elementos que se encuentran en posiciones impares (1, 3, 5, ...) se transfieran a la pila.

Consideraciones:
	La posición de los elementos se cuenta a partir de cero (la primera posición es la 0, la segunda es la 1, etc.).
	La operación debe realizarse recorriendo la cola una sola vez.
	Al finalizar, la pila contendrá los elementos impares en orden LIFO y la cola solo los elementos pares en su orden original.
'''
import os
from cola import Cola
from pila import Pila


def clear(): 
    os.system('cls')

def separar_elementos(cola_original):
    pila = Pila()
    nueva_cola = Cola()
    posicion = 0
    temp = []

    while not cola_original.esta_vacia():
        dato = cola_original.desencolar()
        temp.append(dato)

    for dato in temp:
        if posicion % 2 == 0:
            nueva_cola.encolar(dato)
        else:
            pila.apilar(dato)
        posicion += 1

    return nueva_cola, pila

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar elemento a la cola")
    print("2. Procesar separación")
    print("3. Mostrar cola procesada (pares)")
    print("4. Mostrar pila procesada (impares)")
    print("5. Mostrar cola original")
    print("6. Salir")

def mostrar_cola(cola):
    if cola.esta_vacia():
        print("Cola vacía.")
    else:
        actual = cola.frente
        print("Cola:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def mostrar_pila(pila):
    if pila.esta_vacia():
        print("Pila vacía.")
    else:
        actual = pila.cima()
        print("Pila (cima -> base):", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

if __name__ == "__main__":
    cola = Cola()
    cola_procesada = None
    pila_resultante = None
    valores_originales = []

    while True:
        
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        

        if opcion == '1':
            valor = input("Ingrese un valor para agregar a la cola: ")
            cola.encolar(valor)
            valores_originales.append(valor)
            print(f"{valor} agregado a la cola.")

        elif opcion == '2':
            temp_cola = Cola()
            for val in valores_originales:
                temp_cola.encolar(val)
            cola_procesada, pila_resultante = separar_elementos(temp_cola)
            print("Separación realizada correctamente.")

        elif opcion == '3':
            print("Cola procesada (posiciones pares):")
            if cola_procesada:
                mostrar_cola(cola_procesada)
            else:
                print("Debe procesar la separación primero (opción 2).")

        elif opcion == '4':
            print("Pila procesada (posiciones impares):")
            if pila_resultante:
                mostrar_pila(pila_resultante)
            else:
                print("Debe procesar la separación primero (opción 2).")

        elif opcion == '5':
            print("Cola original:")
            if valores_originales:
                temp_cola = Cola()
                for val in valores_originales:
                    temp_cola.encolar(val)
                mostrar_cola(temp_cola)
            else:
                print("La cola original está vacía.")

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
