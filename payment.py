import data_generator as dg
from datetime import datetime


def calcular_pago(tiempo_transcurrido):
    if tiempo_transcurrido < 43000:  
        return 25 
    elif tiempo_transcurrido > 43000:  # 12 horas
        return 50
    elif tiempo_transcurrido > 86400:  # hasta 24 horas
        return 100
    elif tiempo_transcurrido > 172800:  # hasta 48 horas
        return 200

def ejecutar_pago():
    print("\n--- MAQUINA DE PAGO ---")
    plate = input ("Ingrese su numero de placa:").upper()

    registro = dg.buscar_placa_activa(plate)

    if registro:
        hora_entrada = registro['hora_entrada']
        ahora = datetime.now()
        tiempo_transcurrido = (ahora - hora_entrada).total_seconds()

        print(f"Tiempo transcurrido: {int(tiempo_transcurrido / 60)} minutos")
        a_pagar = calcular_pago(tiempo_transcurrido)
        dinero = int(input(f"Por favor ingrese ${a_pagar}: "))


        # validar que pago sea suficiente
        while dinero < a_pagar:
            print(f"por favor ingrese mas dinero. Faltan ${a_pagar - dinero} pesos")
            dinero = int(input(f"Por favor ingrese ${a_pagar}: "))


        #cambio 
        if dinero > a_pagar:
            print(f"Su cambio es ${dinero - a_pagar}")

        # registrar pago solo si se ha pagado el monto correcto
        if dinero == a_pagar:
            deuda_total = dinero

            # registrar pago
            if deuda_total == a_pagar:
                dg.registrar_pago_db(registro['id'])

    else:
        print("Placa no encontrada. Intente nuevamente.")

