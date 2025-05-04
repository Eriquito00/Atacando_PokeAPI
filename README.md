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

- [Python 3.12 o superior](https://www.python.org/downloads/).

- [MySQL Workbench 8.0 o superior](https://dev.mysql.com/downloads/workbench/).

- [Xampp 8.2 o superior](https://www.apachefriends.org/es/index.html).

### Clonacio i instalacio de dependencies

Una vegada tenim ja els requisits podem procedir a la clonacio del repositori, podem clonar el repositori amb la seguent comanda:

```
git clone https://github.com/Eriquito00/Atacando_PokeAPI.git
```

Ara que tenim el repositori clonat executarem les dues comandes seguents per entrar a la carpeta del repositori clonat:

```
cd Atacando_PokeAPI
```

I la seguent comanda per instalar les llibreries necesaries de Python:

```
pip install -r requirements.txt
```

### Aixecament de la base de dades

Ara es on utilitzarem Xampp per aixecar el servei MySQL. Ara obrirem Xampp i li donarem a 'Start' per iniciar el servei. Una vegada iniciat podem entrar amb MySQL WorkBench.

Una vegada estiguem amb el servei MySQL aixecat podem executar el script 'pokemon_db_ddl.sql' que crea totes les taules necesaries de la base de dades.

### Us dels scripts de consum

Ara per consumir la informacio de la PokeAPI podem consumirla amb els scripts de la carpeta 'script'.

Absorbiran tota la informacio de la API i crearan un fitxer json amb tota aquesta informacio per posteriorment insertarla a la base de dades.

Una vegada tenim tots els fitxers json a la carpeta 'data' podem començar amb els scripts per inserir la informacio a la base de dades.

> [!NOTE]
> Els fitxers json amb totes les dades de la API ja esta desde un principi al repositori.

### Us dels scripts de insert

El fitxers de insert s'han d'executar en un ordre especific, per les claus foranes ja que no es poden enllaçar taules amb altres taules que no existeixen.

El ordre es el seguent:
1. sprites_json.py
2. types_json.py
3. regions_json.py
4. generations_json.py
5. pokemons_json.py
6. locations_json.py
7. version-groups_json.py
8. versions_json.py

Ara ja tindriem la base de dades aixecada, amb les dades introduides i tot preparat per utilitzar les dades amb dades actualitzades de la PokeAPI.

## Altre informacio del projecte

#### Perque hem utilitzat Xampp i no docker?

Nosaltres hem volgut utilitzar Xampp per aixecar la base de dades ja que encara no dominem docker com per crear un projecte solid utilitzant docker pero acceptem alguna pull request del projecte amb altres features o utilitzant docker tot i que fer-ho mes endavant amb docker es una idea que tenim en ment.

#### Perque no s'inserten les dades consumides directament a la base de dades?

Hem decidit finalment fer scripts de consum i de insert totalment separats perque obtenir les dades de la API es un proces lent i no voliem que cada vegada que fem un cambi o que necesitem fer un clon del repositori tinguem que esperar una bona estona per tenir les dades.

Per aixo vam fer scripts per obtenir dades i guardarles als fitxers json i que nomes tinguem que executar els scripts de consum quan hi hagin mes pokemons, mes regions, mes versions etc i tenir les dades preparades per ser insertades a la base de dades en qualsevol moment.

##### Tambe tenim varies consultes al fitxer 'pokemon_db_dml.sql' per poder fer tests amb varies consultes a la nostre base de dades.

###### BY: **[Eriquito00](https://github.com/Eriquito00)** and **[Ikerby341](https://github.com/Ikerby341)**
