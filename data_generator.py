import db_connector as db
from datetime import datetime

# Función para registrar la entrada
def registrar_entrada_db(placa):
    conn = db.get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO parking (placa, hora_entrada, estado) VALUES (%s, NOW(), 0)"
        cursor.execute(sql, (placa,))
        conn.commit()
        print(f"✅ Entrada registrada para la placa: {placa}")
        cursor.close()
        conn.close()

# Función para buscar si la placa está dentro (sin hora_salida)
def buscar_placa_activa(placa):
    conn = db.get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True) # dictionary=True para acceder por nombre de columna
        # Buscamos la última entrada que NO tenga salida aún
        sql = "SELECT * FROM parking WHERE placa = %s AND hora_salida IS NULL ORDER BY hora_entrada DESC LIMIT 1"
        cursor.execute(sql, (placa,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado
    return None

# Función para actualizar a "Pagado" (estado = 1)
def registrar_pago_db(id_registro):
    conn = db.get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE parking SET estado = 1, hora_pago = NOW() WHERE id = %s"
        cursor.execute(sql, (id_registro,))
        conn.commit()
        print("✅ Pago registrado exitosamente.")
        cursor.close()
        conn.close()

# Función para registrar la salida (poner hora_salida)
def registrar_salida_db(id_registro):
    conn = db.get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE parking SET hora_salida = NOW() WHERE id = %s"
        cursor.execute(sql, (id_registro,))
        conn.commit()
        print("👋 Salida registrada. ¡Vuelva pronto!")
        cursor.close()
        conn.close()