# models/empleado_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class EmpleadoModel:
    def crear(self, nombre, rol, id_tienda):
        sql = "INSERT INTO empleado (nombre, rol, id_tienda) VALUES (%s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, rol, id_tienda))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear empleado: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM empleado"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_empleado, nombre, rol):
        sql = "UPDATE empleado SET nombre = %s, rol = %s WHERE id_empleado = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, rol, id_empleado))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar empleado: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_empleado):
        sql = "DELETE FROM empleado WHERE id_empleado = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_empleado,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar empleado: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()