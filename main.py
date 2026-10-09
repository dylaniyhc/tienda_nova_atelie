# main.py
from models.categoria import CategoriaModel
from models.cliente import ClienteModel

if __name__ == "__main__":
    cat_model = CategoriaModel()
    cli_model = ClienteModel()

    # Probar Categoría
    id_cat = cat_model.crear("Tecnología", "tecnologia")
    print(f"Categoría creada con ID: {id_cat}")
    print("Categorías:", cat_model.obtener_todos())

    # Probar Cliente
    id_cli = cli_model.crear("Juan Pérez", "juan@email.com", "123456789")
    print(f"Cliente creado con ID: {id_cli}")
    print("Clientes:", cli_model.obtener_todos())