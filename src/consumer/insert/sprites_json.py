import json
import mysql.connector
from mysql.connector import Error

def insert_sprites_from_json(json_file):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="pokemon_db",
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()

            with open(json_file, 'r', encoding='utf-8') as file:
                sprites_data = json.load(file)
            
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

            connection.commit()
            print(f"{insertados} registros insertados (o ignorados si ya existían).")
            cursor.close()

    except Error as e:
        print(f"Error de conexión o ejecución: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    json_file_path = '../data/data_sprites_consumer.json'
    print("Insertando datos de los sprites desde el archivo JSON...")
    insert_sprites_from_json(json_file_path)