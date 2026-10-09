# models/categoria_model.py
from models.conexion import ConexionBD
from mysql.connector import Error

class CategoriaModel:
    def crear(self, nombre, slug):
        sql = "INSERT INTO categoria (nombre, slug) VALUES (%s, %s)"
        conn = ConexionBD.obtener_conexion()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, slug))
            conn.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al crear categoría: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def obtener_todos(self):
        sql = "SELECT * FROM categoria"
        conn = ConexionBD.obtener_conexion()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def actualizar(self, id_categoria, nombre, slug):
        sql = "UPDATE categoria SET nombre = %s, slug = %s WHERE id_categoria = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (nombre, slug, id_categoria))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar categoría: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()

    def borrar(self, id_categoria):
        sql = "DELETE FROM categoria WHERE id_categoria = %s"
        conn = ConexionBD.obtener_conexion()
        if not conn: return False
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_categoria,))
            conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al borrar categoría: {e}")
            conn.rollback()
        finally:
            if conn and conn.is_connected(): cursor.close(); conn.close()