# models/producto_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class ProductoModel:
    def crear(self, sku, nombre, descripcion, unidad, precio, costo, id_categoria):
        sql = "INSERT INTO producto (sku, nombre, descripcion, unidad, precio, costo, id_categoria) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (sku, nombre, descripcion, unidad, precio, costo, id_categoria))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear producto: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM producto"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar_precio_costo(self, id_producto, precio, costo):
        sql = "UPDATE producto SET precio = %s, costo = %s WHERE id_producto = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (precio, costo, id_producto))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar producto: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_producto):
        sql = "DELETE FROM producto WHERE id_producto = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_producto,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar producto: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()