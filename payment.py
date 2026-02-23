import data_generator as dg
from datetime import datetime

exit_message = "\nGracias por su pago"

####### MENU DE CAJA AUTOMATICA ######
def maquinaPago():
    print("\n --- MAQUINA DE PAGO ---")
    plate = input("Ingrese su placa por favor ").upper()
    registro = validar_placa(plate)

    if registro:
        ejecutar_pago(registro)
    else:
        print("Placa no encontrada. Intente nuevamente.")
        maquinaPago()
    

####### VALIDACION DE PLACA ######
def validar_placa (plate):
    registro = dg.buscar_placa_activa(plate)
    if registro:
        return registro
    else:
        return False

####### calculo de cobro ######
def calcular_pago(tiempo_transcurrido):
    if tiempo_transcurrido > 172800:  # > 48 horas
        return 200
    elif tiempo_transcurrido > 86400:  # > 24 horas
        return 100
    elif tiempo_transcurrido >= 43000: # > 12 horas
        return 50
    else:                              #<= 12 horas
        return 25

####### EJECUCION DE PAGO ######
def ejecutar_pago(registro):

    if registro["estado"] == 1:
        print("Este boleto ya esta pagado")
        return

    hora_entrada = registro['hora_entrada']
    ahora = datetime.now()
    tiempo_transcurrido = (ahora - hora_entrada).total_seconds()

    print(f"Tiempo transcurrido: {int(tiempo_transcurrido / 60)} minutos")

    a_pagar = calcular_pago(tiempo_transcurrido)
    ingreso = int(input(f"Por favor ingrese ${a_pagar} "))

    
    if ingreso == a_pagar:
        pass
    
    elif ingreso > a_pagar:
        print(f"Entregando cambio. \nSu cambio es ${ingreso - a_pagar}")
    
    else:
        falta = a_pagar - ingreso
        while falta > 0:
            print(f"Saldo insuficiente. Le falta ${falta}")
            nuevo_ingreso = int(input("Ingrese el dinero restante: "))
            falta = falta - nuevo_ingreso

            if falta < 0:
                print(f"Entregando cambio. \nSu cambio es ${abs(falta)}")
            
    dg.registrar_pago_db(registro['id'])
    
    print(exit_message)



