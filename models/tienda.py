# models/tienda_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class TiendaModel:
    def crear(self, nombre, direccion):
        sql = "INSERT INTO tienda (nombre, direccion) VALUES (%s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, direccion))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear tienda: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM tienda"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_tienda, nombre, direccion):
        sql = "UPDATE tienda SET nombre = %s, direccion = %s WHERE id_tienda = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, direccion, id_tienda))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar tienda: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_tienda):
        sql = "DELETE FROM tienda WHERE id_tienda = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_tienda,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar tienda: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()