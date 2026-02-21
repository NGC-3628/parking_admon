import mysql.connector

def get_db_connection():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="isaac4ever",
            database="parking_lot_DB"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error conectando a la BD: {err}")
        return None
    

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Conexión exitosa a la base de datos")
        conn.close()
    else:
        print("No se pudo conectar")