# main.py
from grupo_uribe import clasificar_rotacion
from metro_medellin import clasificar_servicio
from epm_consumo import clasificar_consumo
from plaza_minorista import clasificar_temperatura

def menu():
    print("\n--- SISTEMA DE MONITOREO ---")
    print("1. Grupo Uribe - Inventario")
    print("2. Metro Medellín - Tiempos de espera")
    print("3. EPM - Consumo de agua")
    print("4. Plaza Minorista - Cadena de frío")
    print("0. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        datos = [30, 45, 60, 10, 25] * 20
        promedio = sum(datos) / len(datos)
        print("Promedio:", promedio)
        print("Resultado:", clasificar_rotacion(promedio))
    elif opcion == "2":
        datos = [80, 90, 100, 70, 60] * 10
        promedio = sum(datos) / len(datos)
        print("Promedio:", promedio)
        print("Resultado:", clasificar_servicio(promedio))
    elif opcion == "3":
        datos = [20, 40, 60, 80, 100] * 4
        promedio = sum(datos) / len(datos)
        print("Promedio:", promedio)
        print("Resultado:", clasificar_consumo(promedio))
    elif opcion == "4":
        datos = [2, 3, 5, 7, 9] * 20
        datos.pop()
        datos.pop(datos.index(5))
        promedio = sum(datos) / len(datos)
        print("Promedio:", promedio)
        print("Resultado:", clasificar_temperatura(promedio))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Saliendo del sistema...")
            break
        ejecutar_opcion(opcion)
