import json
import mysql.connector
from mysql.connector import Error

def insert_version_groups_from_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="pokemon_db",
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_count = 0
            for version_group in data:
                version_group_name = version_group["name"]
                region_id = version_group["region_id"]
                generation_id = version_group["generation_id"]

                cursor.execute("SELECT region_id FROM regions WHERE region_id = %s", (region_id,))
                region_result = cursor.fetchone()

                cursor.execute("SELECT generation_id FROM generations WHERE generation_id = %s", (generation_id,))
                generation_result = cursor.fetchone()

                if region_result and generation_result:
                    try:
                        cursor.execute(
                            "INSERT INTO version_groups (name, region_id, generation_id) VALUES (%s, %s, %s)",
                            (version_group_name, region_id, generation_id)
                        )
                        insert_count += cursor.rowcount
                    except Error as e:
                        print(f"Error al insertar el version group {version_group_name}: {e}")
                else:
                    if not region_result:
                        print(f"Region ID {region_id} no encontrado en la tabla 'regions'.")
                    if not generation_result:
                        print(f"Generation ID {generation_id} no encontrado en la tabla 'generations'.")

            connection.commit()
            print(f"{insert_count} version groups insertados.")
            cursor.close()

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    json_file = "../data/data_version-groups_consumer.json"
    insert_version_groups_from_json(json_file)