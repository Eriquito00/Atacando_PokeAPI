# Atacando una API

Principalmente guardaremos la siguiente informacion ofrecida por la Poke API:

[] Si este simbolo esta en algun atributo, es porque es un atributo tipo array.

? Si este simbolo esta en algun atributo, significa que podria esta bien pedir mas datos sobre ese parametro

## Enllaços de consulta a la API

### evolution-chain/1-449
    - chain
        - evolves_to[]
            - species
                - name
            - evolves_to[]
                - species
                    - name
        - species
            - name
    - evolution_details[]
        - min_level
        - trigger
            - name
        - item
            - name

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

### pokedex/1-33
    - name
    - pokemon_entries[]
        - pokemon_species
            - name
    - version_groups[]
        - name
    - region
        - name

### pokemon/1-1025
    - height
    - name
    - types[] 
        - name
    - weight
    - abilities[]
        - ability
            - name
    - moves[]
        - move
            - name
    - sprites[]
        - default_front

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