# models/direccion_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class DireccionModel:
    def crear(self, etiqueta, calle, ciudad, id_cliente):
        sql = "INSERT INTO dirección (etiqueta, calle, ciudad, id_cliente) VALUES (%s, %s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (etiqueta, calle, ciudad, id_cliente))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear dirección: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM dirección"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_direccion, etiqueta, calle, ciudad):
        sql = "UPDATE dirección SET etiqueta = %s, calle = %s, ciudad = %s WHERE id_direccion = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (etiqueta, calle, ciudad, id_direccion))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar dirección: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_direccion):
        sql = "DELETE FROM dirección WHERE id_direccion = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_direccion,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar dirección: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()