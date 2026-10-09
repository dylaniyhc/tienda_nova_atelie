# models/pago_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class PagoModel:
    def crear(self, estado, monto, metodo, fecha_pago, id_pedido):
        sql = "INSERT INTO pago (estado, monto, metodo, fecha_pago, id_pedido) VALUES (%s, %s, %s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (estado, monto, metodo, fecha_pago, id_pedido))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear pago: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM pago"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar_estado(self, id_pago, nuevo_estado):
        sql = "UPDATE pago SET estado = %s WHERE id_pago = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nuevo_estado, id_pago))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar pago: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_pago):
        sql = "DELETE FROM pago WHERE id_pago = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_pago,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar pago: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()