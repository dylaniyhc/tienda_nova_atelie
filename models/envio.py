# models/envio_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class EnvioModel:
    def crear(self, transporte, codigo_seguimiento, estado, id_pedido):
        sql = "INSERT INTO envio (transporte, codigo_seguimiento, estado, id_pedido) VALUES (%s, %s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (transporte, codigo_seguimiento, estado, id_pedido))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear envío: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM envio"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar_estado(self, id_envio, nuevo_estado):
        sql = "UPDATE envio SET estado = %s WHERE id_envio = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nuevo_estado, id_envio))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar envío: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_envio):
        sql = "DELETE FROM envio WHERE id_envio = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_envio,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar envío: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()