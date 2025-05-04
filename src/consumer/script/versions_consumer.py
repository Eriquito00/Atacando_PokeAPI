import requests
import json
import os

def get_total_versions():
    url = "https://pokeapi.co/api/v2/version?limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("count", 0)
    return 0

def get_version_data(version_id):
    url = f"https://pokeapi.co/api/v2/version/{version_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    name = data.get("name")
    version_group_url = data.get("version_group", {}).get("url")

    if not version_group_url:
        return None

    version_group_id = int(version_group_url.strip("/").split("/")[-1])

    return {
        "name": name,
        "version_group_id": version_group_id
    }

def get_all_versions():
    total = get_total_versions()
    all_data = []

    for version_id in range(1, total + 1):
        try:
            data = get_version_data(version_id)
            if data:
                all_data.append(data)
                print(f"Versión {data['name']} → Grupo {data['version_group_id']}")
        except Exception as e:
            print(f"Error con la versión ID {version_id}: {e}")
    
    return all_data

def save_to_json(data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(parent_directory, '..', 'data')
    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, "data_versions_consumer.json")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nArchivo guardado en: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    print("Obteniendo datos de versiones...")
    version_data = get_all_versions()
    save_to_json(version_data)