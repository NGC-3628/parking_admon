import data_generator as dg
from datetime import datetime
#import payment 
import main

def ejecutar_salida():
    print("\n--- SALIDA ---")
    plate = input("Ingrese su placa para salir: ").upper()
    
    registro = dg.buscar_placa_activa(plate)
    
    if registro:
        hora_entrada = registro['hora_entrada']
        ahora = datetime.now()
        tiempo_transcurrido = (ahora - hora_entrada).total_seconds()
        
       
        if registro['estado'] == 1 or tiempo_transcurrido < 40:
            if tiempo_transcurrido < 40 and registro['estado'] == 0:
                print("Puede salir. ¡Gracias!")
                dg.registrar_pago_db(registro['id']) 
            
            dg.registrar_salida_db(registro['id'])
            
        else:
            print(f"ALTO. Han pasado {int(tiempo_transcurrido)} segundos y no ha pagado.")
            print("Pase a pagar")
            main.menu() 
            
    else:
        print("Placa no encontrada. Intente nuevamente.")