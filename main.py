import entrance
import payment
import exit
import sys

def menu():
    while True:
        print("\n==============================")
        print("   SISTEMA DE ESTACIONAMIENTO   ")
        print("==============================")
        print("1. Ingresar Vehículo (Entrance)")
        print("2. Pagar Ticket (Payment)")
        print("3. Salir Vehículo (Exit)")
        print("4. Cerrar Sistema")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            entrance.ejecutar_entrada()
        elif opcion == '2':
            payment.ejecutar_pago()
        elif opcion == '3':
            exit.ejecutar_salida()
        elif opcion == '4':
            print("Apagando sistema...")
            sys.exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()