# models/proveedor_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class ProveedorModel:
    def crear(self, nombre, info_contacto):
        sql = "INSERT INTO proveedor (nombre, info_contacto) VALUES (%s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, info_contacto))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear proveedor: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM proveedor"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_proveedor, nombre, info_contacto):
        sql = "UPDATE proveedor SET nombre = %s, info_contacto = %s WHERE id_proveedor = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, info_contacto, id_proveedor))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar proveedor: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_proveedor):
        sql = "DELETE FROM proveedor WHERE id_proveedor = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_proveedor,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar proveedor: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()