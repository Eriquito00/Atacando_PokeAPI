import requests
import json
import os

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

def save_generations_to_json(generations_data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(parent_directory, '..', 'data')
    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, "data_generations_consumer.json")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(generations_data, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    print("Obteniendo datos de las generaciones de Pokémon...")
    generations_data = get_generations_data()
    save_generations_to_json(generations_data)