import requests
import json
import os

def get_total_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("count", 1025)
    return 1025

def get_pokemon_sprite_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    sprite_url = data["sprites"].get("front_default")
    
    if not sprite_url:
        return None
    
    return sprite_url

def get_all_sprites():
    all_sprites_data = []
    
    for pokemon_id in range(1, get_total_pokemon() + 1):
        try:
            sprite_url = get_pokemon_sprite_data(pokemon_id)
            if sprite_url:
                all_sprites_data.append({"sprite_url": sprite_url})
                print(f"Datos obtenidos para el Pokémon ID {pokemon_id}")
        except Exception as e:
            print(f"Error con el Pokémon ID {pokemon_id}: {e}")
    
    return all_sprites_data

def save_sprites_to_json(sprites_data):
    parent_directory = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(parent_directory, '..', 'data')
    os.makedirs(data_directory, exist_ok=True)

    file_path = os.path.join(data_directory, "data_sprites_consumer.json")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(sprites_data, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    print("Obteniendo datos de los sprites de los Pokémon...")
    
    all_sprites = get_all_sprites()

    save_sprites_to_json(all_sprites)