# models/tienda_model.py
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class TiendaModel:
    
    # -------------------------------------------------------------------
    # CONEXIÓN
    # Función dedicada exclusivamente a conectar con MySQL
    # -------------------------------------------------------------------
    def conectar(self):
        try:
            conexion = mysql.connector.connect(**DB_CONFIG)
            return conexion
        except Error as err:
            print(f"Error al conectar a MySQL: {err}")
            return None

    # -------------------------------------------------------------------
    # 1. CREACIÓN (Create)
    # -------------------------------------------------------------------
    def crear_cliente(self, nombre, email, telefono):
        sql = "INSERT INTO cliente (nombre, email, telefono) VALUES (%s, %s, %s)"
        conexion = self.conectar()
        if not conexion:
            return None
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (nombre, email, telefono))
            conexion.commit()
            id_creado = cursor.lastrowid
            return id_creado
        except Error as err:
            print(f"Error en CREAR cliente: {err}")
            conexion.rollback()
            return None
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    def crear_producto(self, sku, nombre, descripcion, unidad, precio, costo, id_categoria):
        sql = """
            INSERT INTO producto (sku, nombre, descripcion, unidad, precio, costo, id_categoria)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        conexion = self.conectar()
        if not conexion:
            return None
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (sku, nombre, descripcion, unidad, precio, costo, id_categoria))
            conexion.commit()
            return cursor.lastrowid
        except Error as err:
            print(f"Error en CREAR producto: {err}")
            conexion.rollback()
            return None
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    # -------------------------------------------------------------------
    # 2. LECTURA (Read)
    # -------------------------------------------------------------------
    def leer_clientes(self):
        sql = "SELECT id_cliente, nombre, email, telefono FROM cliente"
        conexion = self.conectar()
        if not conexion:
            return []
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f"Error en LEER clientes: {err}")
            return []
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    def leer_cliente_por_id(self, id_cliente):
        sql = "SELECT id_cliente, nombre, email, telefono FROM cliente WHERE id_cliente = %s"
        conexion = self.conectar()
        if not conexion:
            return None
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(sql, (id_cliente,))
            resultado = cursor.fetchone()
            return resultado
        except Error as err:
            print(f"Error en LEER cliente por ID: {err}")
            return None
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    # -------------------------------------------------------------------
    # 3. ACTUALIZACIÓN (Update)
    # -------------------------------------------------------------------
    def actualizar_cliente(self, id_cliente, nombre, email, telefono):
        sql = "UPDATE cliente SET nombre = %s, email = %s, telefono = %s WHERE id_cliente = %s"
        conexion = self.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (nombre, email, telefono, id_cliente))
            conexion.commit()
            return cursor.rowcount > 0
        except Error as err:
            print(f"Error en ACTUALIZAR cliente: {err}")
            conexion.rollback()
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    # -------------------------------------------------------------------
    # 4. BORRADO (Delete)
    # -------------------------------------------------------------------
    def borrar_cliente(self, id_cliente):
        sql = "DELETE FROM cliente WHERE id_cliente = %s"
        conexion = self.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(sql, (id_cliente,))
            conexion.commit()
            return cursor.rowcount > 0
        except Error as err:
            print(f"Error en BORRAR cliente: {err}")
            conexion.rollback()
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()