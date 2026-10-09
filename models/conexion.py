# models/conexion.py
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class ConexionBD:
    @staticmethod
    def obtener_conexion():
        try:
            conexion = mysql.connector.connect(**DB_CONFIG)
            if conexion.is_connected():
                return conexion
        except Error as err:
            print(f"Error al conectar a MySQL: {err}")
            return None