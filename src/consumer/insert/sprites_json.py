import json
import mysql.connector
from mysql.connector import Error

# Función para insertar los datos del JSON en la base de datos
def insert_sprites_from_json(json_file):
    connection = None
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",  # Cambia esto según tu configuración
            password="",  # Cambia esto según tu configuración
            database="pokemon_db",  # Cambia esto si el nombre de la base de datos es diferente
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Abrir y leer el archivo JSON
            with open(json_file, 'r', encoding='utf-8') as file:
                sprites_data = json.load(file)
            
            # Contar cuántos sprites se insertarán
            insertados = 0
            for sprite_entry in sprites_data:
                try:
                    cursor.execute(
                        "INSERT INTO sprites (sprite) VALUES (%s)", 
                        (sprite_entry["sprite_url"],)
                    )
                    insertados += cursor.rowcount
                except Error as e:
                    print(f"Error al insertar sprite '{sprite_entry['sprite_url']}': {e}")

            # Confirmar los cambios en la base de datos
            connection.commit()
            print(f"{insertados} registros insertados (o ignorados si ya existían).")
            cursor.close()

    except Error as e:
        print(f"Error de conexión o ejecución: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

# Ejecutar el script para insertar los datos desde el archivo JSON
if __name__ == "__main__":
    json_file_path = '../data/data_sprites_consumer.json'  # Cambia esta ruta si el archivo está en otro lugar
    print("Insertando datos de los sprites desde el archivo JSON...")
    insert_sprites_from_json(json_file_path)