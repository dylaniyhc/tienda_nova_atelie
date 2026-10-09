# models/tipo_producto_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class TipoProductoModel:
    def crear(self, nombre, descripcion):
        sql = "INSERT INTO tipo_producto (nombre, descripcion) VALUES (%s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, descripcion))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear tipo de producto: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM tipo_producto"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_tipo, nombre, descripcion):
        sql = "UPDATE tipo_producto SET nombre = %s, descripcion = %s WHERE id_tipo = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, descripcion, id_tipo))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar tipo de producto: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_tipo):
        sql = "DELETE FROM tipo_producto WHERE id_tipo = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_tipo,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar tipo de producto: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()