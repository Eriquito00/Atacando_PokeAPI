import requests
import mysql.connector
from mysql.connector import Error

def get_types_data():
    url = "https://pokeapi.co/api/v2/region"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener los datos: {response.status_code}")
        return []

    data = response.json()
    types = data.get("results", [])
    
    return [{"name": type_info["name"]} for type_info in types]

def insert_regions_to_db(regions_data):
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
            for region_entry in regions_data:
                try:
                    cursor.execute(
                        "INSERT INTO regions (name) VALUES (%s)", 
                        (region_entry["name"],)
                    )
                    insertados += cursor.rowcount
                except Error as e:
                    print(f"Error al insertar región '{region_entry['name']}': {e}")

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
    print("Obteniendo datos de las regiones desde la API...")
    regions_data = get_types_data()
    insert_regions_to_db(regions_data)