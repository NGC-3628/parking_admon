import data_generator as dg

def ejecutar_entrada():
    print("\n--- PLAZA LOS MOLINOS: ENTRADA ---")
    plate = input("Ingrese su número de placa: ").upper() # .upper() para que siempre sea mayúscula
    
    if plate:
        dg.registrar_entrada_db(plate)
    else:
        print("Error: La placa no puede estar vacía.")