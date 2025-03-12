# Revision de JSON de PokéAPI 

## INFO API

### pokemon/1-1025
- height
- moves[]
    - move
        - name
- name
- sprites
    - default_front
- types[]
    - name
- weight

### evolution-chain/1-449
- chain
    - evolves_to[]
        - evolution_details[]
            - min_level
            - trigger
                - name
        - evolves_to[]
            - evolution_details[]
                - min_level
                - trigger
                    - name
            - species
                - name
        - species
            - name

### pokedex/1-33
- name
- pokemon_entries[]
    - entry_number

### generation/1-9
    - main_region
        - name
    - name
    - pokemon_species[] 
        - name
    - types[] 
        - name
    - version_groups[]
        - name
    - abilities[]
        - name



### pokemon-habitat/1-9
    - name
    - pokemon_species[] 
        - name

### region/1-10
    - locations[]
        - name
    - main_generation
        - name
    - name
    - pokedexes[]
        - name
    - version_groups
        - name
    - legendary_pokemon[]
        - name

### type/1-19
    - damage_relations
        - double_damage_from[]
            - name
        - double_damage_to[]
            - name
        - half_damage_from[]
            - name
        - half_damage_to[]
            - name
        - no_damage_from[]
            - name
        - no_damage_to[]
            - name

### version/1-43
    - name
    - version_group
        - name

### version-group/1-27
    - generation
        - name
    - name
    - pokedexes[]
        - name
    - regions[]
        - name
    - versions[]
        - name

###### BY: **[Eriquito00](https://github.com/Eriquito00)** and **[Ikerby341](https://github.com/Ikerby341)**