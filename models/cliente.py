# models/cliente_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class ClienteModel:
    def crear(self, nombre, email, telefono):
        sql = "INSERT INTO cliente (nombre, email, telefono) VALUES (%s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, email, telefono))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear cliente: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM cliente"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_cliente, nombre, email, telefono):
        sql = "UPDATE cliente SET nombre = %s, email = %s, telefono = %s WHERE id_cliente = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, email, telefono, id_cliente))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar cliente: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_cliente):
        sql = "DELETE FROM cliente WHERE id_cliente = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_cliente,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar cliente: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()