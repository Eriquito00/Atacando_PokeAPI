import json
import mysql.connector
from mysql.connector import Error

def insert_pokemon_to_db(pokemon_data):
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
            for pokemon_entry in pokemon_data:
                try:
                    cursor.execute(
                        """INSERT INTO pokemons (
                            name, weight, height, min_level, evolution_method,
                            evolution_id, sprite_id, type_id, generation_id, num_pokedex
                        ) VALUES (%s, %s, %s, %s, %s, NULL, %s, %s, %s, %s)""",
                        (
                            pokemon_entry["name"],
                            pokemon_entry["weight"],
                            pokemon_entry["height"],
                            pokemon_entry["min_level"],
                            pokemon_entry["evolution_method"],
                            pokemon_entry["sprite_id"],
                            pokemon_entry["type_id"],
                            pokemon_entry["generation_id"],
                            pokemon_entry["num_pokedex"]
                        )
                    )
                    insertados += cursor.rowcount
                except Error as e:
                    print(f"Error al insertar el Pokémon '{pokemon_entry['name']}': {e}")

            connection.commit()
            print(f"{insertados} Pokémon insertados (sin relaciones de evolución).")
            cursor.close()

    except Error as e:
        print(f"Error de conexión o ejecución: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

def update_evolution_ids(pokemon_data):
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

            update_count = 0
            for pokemon_entry in pokemon_data:
                if pokemon_entry.get("evolution_id") is not None:
                    try:
                        cursor.execute(
                            """UPDATE pokemons 
                               SET evolution_id = %s 
                               WHERE num_pokedex = %s""",
                            (pokemon_entry["evolution_id"], pokemon_entry["num_pokedex"])
                        )
                        update_count += cursor.rowcount
                    except Error as e:
                        print(f"Error al actualizar el Pokémon ID {pokemon_entry['num_pokedex']}: {e}")

            connection.commit()
            print(f"{update_count} relaciones de evolución actualizadas.")
            cursor.close()

    except Error as e:
        print(f"Error de conexión o ejecución: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

def load_pokemon_data_from_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            pokemon_data = json.load(f)
        print(f"Datos cargados desde {file_path}")
        return pokemon_data
    except Exception as e:
        print(f"Error al cargar los datos del archivo JSON: {e}")
        return []

if __name__ == "__main__":
    file_path = "../data/data_pokemons_consumer.json"

    print("Cargando datos de Pokémon desde el archivo JSON...")
    pokemon_data = load_pokemon_data_from_json(file_path)

    if pokemon_data:
        print("Insertando todos los Pokémon en la base de datos...")
        insert_pokemon_to_db(pokemon_data)

        print("Actualizando relaciones de evolución...")
        update_evolution_ids(pokemon_data)

        print("Todos los Pokémon han sido insertados y actualizados con las relaciones de evolución.")
    else:
        print("No se encontraron datos para insertar.")