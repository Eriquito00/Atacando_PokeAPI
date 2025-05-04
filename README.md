# Atacando una API

Aquest projecte té com a objectiu consumir la [PokeAPI](https://pokeapi.co/), emmagatzemar les dades en una base de dades relacional MySQL.

## Objectius

- Dissenyar un model entitat relacio i model relacional.

- Crear una base de dades relacional amb MySQL

- Obtenir dades de una API i carregarles a la nostre base de dades.

## Estructura del repositori

```
- README.md             # Descripció del projecte
- database/             # Model de dades i scripts SQL
  - ddl/                # Sentències DDL per crear la base de dades
  - dml/                # Sentències DML per inserir dades
- doc/                  # Documentació addicional
  - Entitat Relacio/    # Grafic entitat relacio
  - Model Relacional/   # Grafic model relacional
- src/                  # Codi font
  - consumer/           # Scripts per consumir la PokeAPI
    - data/             # Dades consumides de la API
    - insert/           # Scripts per introduir les dades
    - script/           # Scripts per obtenir les dades
```

## Us del repositori

Principalment necesitarem uns requisits per utilitzar tant els scripts de consumicio de la API com per poder aixecar i utilitzar la base de dades.

### Requisits



###### BY: **[Eriquito00](https://github.com/Eriquito00)** and **[Ikerby341](https://github.com/Ikerby341)**