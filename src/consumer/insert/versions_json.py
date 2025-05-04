import json
import mysql.connector
from mysql.connector import Error

def insert_versions_from_json(json_file):
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
            for version in data:
                version_name = version["name"]
                version_group_id = version["version_group_id"]

                cursor.execute("SELECT version_group_id FROM version_groups WHERE version_group_id = %s", (version_group_id,))
                version_group_result = cursor.fetchone()

                if version_group_result:
                    try:
                        cursor.execute(
                            "INSERT INTO versions (name, version_group_id) VALUES (%s, %s)",
                            (version_name, version_group_id)
                        )
                        insert_count += cursor.rowcount
                    except Error as e:
                        print(f"Error al insertar la versión {version_name}: {e}")
                else:
                    print(f"version_group_id {version_group_id} no encontrado en la tabla 'version_groups'.")

            connection.commit()
            print(f"{insert_count} versiones insertadas.")
            cursor.close()

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    json_file = "../data/data_versions_consumer.json"
    insert_versions_from_json(json_file)