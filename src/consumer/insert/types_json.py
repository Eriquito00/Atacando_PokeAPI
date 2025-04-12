import requests
import mysql.connector
from mysql.connector import Error

def get_types_data():
    url = "https://pokeapi.co/api/v2/type"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener los datos: {response.status_code}")
        return []

    data = response.json()
    types = data.get("results", [])
    
    return [{"name": type_info["name"]} for type_info in types]

def insert_types_to_db(types_data):
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

            insertados = 0
            for type_entry in types_data:
                try:
                    cursor.execute(
                        "INSERT INTO types (name) VALUES (%s)", 
                        (type_entry["name"],)
                    )
                    insertados += cursor.rowcount
                except Error as e:
                    print(f"Error al insertar tipo '{type_entry['name']}': {e}")

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
    print("Obteniendo datos de los tipos de los Pokémon desde la API...")
    types_data = get_types_data()
    insert_types_to_db(types_data)