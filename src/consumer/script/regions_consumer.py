import requests
import json
import os

def get_types_data():
    url = "https://pokeapi.co/api/v2/region"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al obtener los datos: {response.status_code}")
        return []

    data = response.json()
    types = data.get("results", [])
    
    return [{"region": type_info["name"]} for type_info in types]

def save_types_to_json(types_data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(parent_directory, '..', 'data')
    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, "data_regions_consumer.json")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(types_data, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    print("Obteniendo datos de las regiones...")
    types_data = get_types_data()
    save_types_to_json(types_data)