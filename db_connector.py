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