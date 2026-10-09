# main.py
from models.tienda_model import TiendaModel

# Instanciar el modelo dedicado a MySQL
modelo = TiendaModel()

# 1. CREACIÓN
id_nuevo = modelo.crear_cliente("María López", "maria@email.com", "987654321")
print(f"Cliente creado con ID: {id_nuevo}")

# 2. LECTURA
print("\nLista de clientes:")
print(modelo.leer_clientes())

# 3. ACTUALIZACIÓN
exito_act = modelo.actualizar_cliente(id_nuevo, "María José López", "mariajose@email.com", "987654321")
print(f"¿Actualización exitosa?: {exito_act}")

# 4. BORRADO
exito_borrado = modelo.borrar_cliente(id_nuevo)
print(f"¿Borrado exitoso?: {exito_borrado}")