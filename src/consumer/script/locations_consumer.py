import requests
import json
import os

def get_total_locations():
    """Obtiene el número total de ubicaciones disponibles en la API."""
    url = "https://pokeapi.co/api/v2/location?limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("count", 0)
    return 0

def get_location_data(location_id):
    """Obtiene el nombre de la ubicación y el ID de la región a partir del ID de ubicación."""
    url = f"https://pokeapi.co/api/v2/location/{location_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    location_name = data.get("name")
    region_url = data.get("region", {}).get("url")
    
    if not location_name or not region_url:
        return None

    region_id = int(region_url.strip('/').split('/')[-1])
    
    return {
        "location": location_name,
        "region_id": region_id
    }

def get_all_locations():
    total_locations = get_total_locations()
    all_location_data = []

    for location_id in range(1, total_locations + 1):
        try:
            location_data = get_location_data(location_id)
            if location_data:
                all_location_data.append(location_data)
                print(f"Obtenido: {location_data['location']} (Region ID: {location_data['region_id']})")
        except Exception as e:
            print(f"Error con la ubicación ID {location_id}: {e}")

    return all_location_data

def save_to_json(data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(parent_directory, '..', 'data')
    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, "data_locations_consumer.json")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nArchivo guardado en: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    print("Recopilando ubicaciones y sus regiones...")
    data = get_all_locations()
    save_to_json(data)