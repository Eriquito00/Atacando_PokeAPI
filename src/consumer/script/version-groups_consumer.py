import requests
import json
import os

def get_total_version_groups():
    url = "https://pokeapi.co/api/v2/version-group?limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("count", 0)
    return 0

def get_version_group_data(vg_id):
    url = f"https://pokeapi.co/api/v2/version-group/{vg_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    name = data.get("name")
    generation_url = data.get("generation", {}).get("url")

    if not generation_url:
        return None

    generation_id = int(generation_url.strip("/").split("/")[-1])

    # Obtener región desde la generación
    gen_response = requests.get(generation_url)
    if gen_response.status_code != 200:
        return None

    gen_data = gen_response.json()
    region_url = gen_data.get("main_region", {}).get("url")

    if not region_url:
        return None

    region_id = int(region_url.strip("/").split("/")[-1])

    return {
        "name": name,
        "generation_id": generation_id,
        "region_id": region_id
    }

def get_all_version_groups():
    total = get_total_version_groups()
    all_data = []

    for vg_id in range(1, total + 1):
        try:
            data = get_version_group_data(vg_id)
            if data:
                all_data.append(data)
                print(f"{data['name']} → Gen {data['generation_id']}, Región {data['region_id']}")
        except Exception as e:
            print(f"Error con version-group ID {vg_id}: {e}")
    
    return all_data

def save_to_json(data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(parent_directory, '..', 'data')
    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, "data_version-groups_consumer.json")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nArchivo guardado en: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    print("Obteniendo datos de version-groups...")
    version_group_data = get_all_version_groups()
    save_to_json(version_group_data)