import requests
import mysql.connector
from mysql.connector import Error

def get_generations_data():
    url = "https://pokeapi.co/api/v2/generation"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener los datos: {response.status_code}")
        return []

    data = response.json()
    generations = data.get("results", [])
    
    generations_data = []
    for generation in generations:
        generation_url = generation["url"]
        gen_response = requests.get(generation_url)
        if gen_response.status_code == 200:
            gen_data = gen_response.json()
            region_name = gen_data["id"]
            generation_name = gen_data["name"]
            generations_data.append({
                "nombre": generation_name,
                "region_id": region_name
            })

    return generations_data

def insert_generations_to_db(generations_data):
    connection = None
    try:
        # Conexión a la base de datos
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
            for generation_entry in generations_data:
                try:
                    cursor.execute(
                        "INSERT INTO generations (name, region_id) VALUES (%s, %s)", 
                        (generation_entry["nombre"], generation_entry["region_id"])
                    )
                    insertados += cursor.rowcount
                except Error as e:
                    print(f"Error al insertar generación '{generation_entry['nombre']}': {e}")

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
    print("Obteniendo datos de las generaciones de Pokémon desde la API...")
    generations_data = get_generations_data()
    insert_generations_to_db(generations_data)