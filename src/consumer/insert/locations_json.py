import json
import mysql.connector
from mysql.connector import Error

def insert_locations_from_json(json_file):
    """Lee el archivo JSON y guarda los datos en la tabla 'locations'."""
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

            # Insertar los datos
            insert_count = 0
            for location in data:
                location_name = location["location"]
                region_id = location["region_id"]

                cursor.execute("SELECT region_id FROM regions WHERE region_id = %s", (region_id,))
                result = cursor.fetchone()
                
                if result:
                    try:
                        cursor.execute(
                            "INSERT INTO locations (name, region_id) VALUES (%s, %s)",
                            (location_name, region_id)
                        )
                        insert_count += cursor.rowcount
                    except Error as e:
                        print(f"Error al insertar la ubicación {location_name}: {e}")
                else:
                    print(f"Region ID {region_id} no encontrado en la tabla 'regions'.")

            connection.commit()
            print(f"{insert_count} ubicaciones insertadas.")
            cursor.close()

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    json_file = "../data/data_locations_consumer.json"
    insert_locations_from_json(json_file)