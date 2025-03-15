import requests
import json
import os

def get_total_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon-species/?limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("count", 1025)
    return 1025

def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    species_url = data["species"]["url"]
    species_response = requests.get(species_url)
    if species_response.status_code != 200:
        return None
    
    species_data = species_response.json()
    evolution_chain_url = species_data.get("evolution_chain", {}).get("url")
    
    evolution_info = {"evolution_id": None, "min_level": None, "evolution_method": None}
    
    if evolution_chain_url:
        evolution_response = requests.get(evolution_chain_url)
        if evolution_response.status_code == 200:
            evolution_data = evolution_response.json().get("chain", {})
            
            def get_first_evolution(chain, pokemon_name):
                if not chain or "species" not in chain:
                    return None
                
                if chain["species"]["name"] == pokemon_name.lower():
                    if chain.get("evolves_to") and len(chain["evolves_to"]) > 0:
                        first_evo = chain["evolves_to"][0]
                        evo_details = first_evo.get("evolution_details", [{}])
                        evo_details = evo_details[0] if evo_details else {}
                        return {
                            "evolution_id": int(first_evo["species"]["url"].split("/")[-2]) if "species" in first_evo else None,
                            "min_level": evo_details.get("min_level"),
                            "evolution_method": evo_details.get("trigger", {}).get("name")
                        }
                for evo in chain.get("evolves_to", []):
                    result = get_first_evolution(evo, pokemon_name)
                    if result:
                        return result
                return None
            
            evolution_info = get_first_evolution(evolution_data, data["name"]) or evolution_info
    
    return {
        "name": data["name"],
        "weight": data["weight"],
        "height": data["height"],
        "min_level": evolution_info["min_level"],
        "evolution_method": evolution_info["evolution_method"],
        "evolution_id": evolution_info["evolution_id"],
        "sprite_id": int(data["id"]),
        "type_id": int(data["types"][0]["type"]["url"].split("/")[-2]) if data["types"] else None,
        "num_pokedex": int(data["id"]),
        "generation_id": int(species_data["generation"]["url"].split("/")[-2])
    }

def get_all_pokemon():
    total_pokemon = 5
    all_pokemon_data = []
    
    for pokemon_id in range(1, total_pokemon + 1):
        try:
            pokemon_data = get_pokemon_data(pokemon_id)
            if pokemon_data:
                all_pokemon_data.append(pokemon_data)
                print(f"Datos obtenidos para el Pokémon ID {pokemon_id}")
        except Exception as e:
            print(f"Error con el Pokémon ID {pokemon_id}: {e}")
    
    os.makedirs("caballo\data", exist_ok=True)
    with open(os.path.join("..","data", "data_pokemons_consumer_PRUEBA.json"), "w", encoding="utf-8") as f:
        json.dump(all_pokemon_data, f, indent=4, ensure_ascii=False)
    
    return all_pokemon_data

if __name__ == "__main__":
    print("Obteniendo datos de todos los Pokémon...")
    all_pokemon = get_all_pokemon()
    print("Datos guardados en data_pokemons_consumer_PRUEBA.json")