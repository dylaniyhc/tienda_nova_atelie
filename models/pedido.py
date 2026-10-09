# models/pedido_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class PedidoModel:
    def crear(self, estado, fecha_pedido, id_tienda, id_cliente):
        sql = "INSERT INTO pedido (estado, fecha_pedido, id_tienda, id_cliente) VALUES (%s, %s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (estado, fecha_pedido, id_tienda, id_cliente))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear pedido: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM pedido"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar_estado(self, id_pedido, nuevo_estado):
        sql = "UPDATE pedido SET estado = %s WHERE id_pedido = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nuevo_estado, id_pedido))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar pedido: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_pedido):
        sql = "DELETE FROM pedido WHERE id_pedido = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_pedido,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar pedido: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()