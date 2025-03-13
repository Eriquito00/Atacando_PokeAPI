CREATE DATABASE pokemon_db;

USE pokemon_db;

CREATE TABLE sprites (
	  sprite_id	  INT UNSIGNED AUTO_INCREMENT,
    sprite			VARCHAR(45),
    CONSTRAINT pk_sprites PRIMARY KEY (sprite_id)
);

CREATE TABLE pokedexes (
	  pokedex_id		INT UNSIGNED AUTO_INCREMENT,
    num_pokedex		INT UNSIGNED NOT NULL,
    name		    	VARCHAR(45) NOT NULL,
    CONSTRAINT pk_pokedexes PRIMARY KEY (pokedex_id)
);

CREATE TABLE types (
	  type_id		INT UNSIGNED AUTO_INCREMENT,
    name			VARCHAR(45) NOT NULL,
    CONSTRAINT pk_types PRIMARY KEY (type_id)
);

CREATE TABLE moves (
	  move_id		  INT UNSIGNED AUTO_INCREMENT,
    name			  VARCHAR(45) NOT NULL,
    type_id			INT UNSIGNED,
    CONSTRAINT pk_moves PRIMARY KEY (move_id),
    CONSTRAINT fk_types_moves FOREIGN KEY (type_id)
		REFERENCES types (type_id)
);

CREATE TABLE regions (
	region_id		INT UNSIGNED AUTO_INCREMENT,
    name			VARCHAR(45) NOT NULL,
    CONSTRAINT pk_regions PRIMARY KEY (region_id)
);

CREATE TABLE pokemons (
	  pokemon_id		    INT UNSIGNED AUTO_INCREMENT,
    name			      	VARCHAR(45) NOT NULL,
    weight			    	FLOAT NOT NULL,
    height			    	FLOAT NOT NULL,
    min_level		    	TINYINT UNSIGNED,
    evolution_method	VARCHAR(45),
    evolution_id	    INT UNSIGNED,
    sprite_id		    	INT UNSIGNED,
    pokedex_id	   		INT UNSIGNED,
    move_id			    	INT UNSIGNED,
    type_id			    	INT UNSIGNED,
    CONSTRAINT pk_pokemons PRIMARY KEY (pokemon_id),
    CONSTRAINT ck_min_level CHECK (min_level >= 1 AND min_level <= 100),
    CONSTRAINT fk_pokemons_pokemons FOREIGN KEY (evolution_id)
		  REFERENCES pokemons (pokemon_id),
	  CONSTRAINT fk_sprites_pokemons FOREIGN KEY (sprite_id)
		  REFERENCES sprites (sprite_id),
    CONSTRAINT fk_pokedexes_pokemons FOREIGN KEY (pokedex_id)
      REFERENCES pokedexes (pokedex_id),
    CONSTRAINT fk_moves_pokemons FOREIGN KEY (move_id)
      REFERENCES moves (move_id),
    CONSTRAINT fk_types_pokemons FOREIGN KEY (type_id)
      REFERENCES types (type_id)
);

CREATE TABLE pokedexes_regions (
	  pokedex_region_id	  INT UNSIGNED AUTO_INCREMENT,
	  region_id				    INT UNSIGNED NOT NULL,
    pokedex_id				  INT UNSIGNED NOT NULL,
    CONSTRAINT pk_pokedexes_regions PRIMARY KEY (pokedex_region_id),
    CONSTRAINT fk_regions_pokedexes_regions FOREIGN KEY (region_id)
		  REFERENCES regions (region_id),
    CONSTRAINT fk_pokedexes_pokedexes_regions FOREIGN KEY (pokedex_id)
		  REFERENCES pokedexes (pokedex_id)
);

CREATE TABLE locations (
	  location_id		INT UNSIGNED AUTO_INCREMENT,
    name			    VARCHAR(45) NOT NULL,
    region_id		  INT UNSIGNED NOT NULL,
    CONSTRAINT pk_locations PRIMARY KEY (location_id),
    CONSTRAINT fk_regions_locations FOREIGN KEY (region_id)
		  REFERENCES regions (region_id)
);

CREATE TABLE generations (
	  generation_id		INT UNSIGNED AUTO_INCREMENT,
    name				    VARCHAR(45) NOT NULL,
    region_id		  	INT UNSIGNED NOT NULL,
    CONSTRAINT pk_generations PRIMARY KEY (generation_id),
    CONSTRAINT fk_regions_generations FOREIGN KEY (region_id)
		  REFERENCES regions (region_id)
);

CREATE TABLE version_groups (
	  version_group_id		INT UNSIGNED AUTO_INCREMENT,
    name					      VARCHAR(45) NOT NULL,
    region_id		    		INT UNSIGNED NOT NULL,
    generation_id		  	INT UNSIGNED NOT NULL,
    CONSTRAINT pk_version_groups PRIMARY KEY (version_group_id),
    CONSTRAINT fk_version_groups_regions FOREIGN KEY (region_id)
		  REFERENCES regions (region_id),
    CONSTRAINT fk_version_groups_generations FOREIGN KEY (generation_id)
      REFERENCES generations (generation_id)
);

CREATE TABLE pokedexes_version_groups (
	  pokedex_version_group_id		INT UNSIGNED AUTO_INCREMENT,
	  version_group_id			    	INT UNSIGNED NOT NULL,
    pokedex_id					      	INT UNSIGNED NOT NULL,
    CONSTRAINT pk_pokedexes_version_groups PRIMARY KEY (pokedex_version_group_id),
    CONSTRAINT fk_version_groups_pokedexes_version_groups FOREIGN KEY (version_group_id)
		  REFERENCES version_groups (version_group_id),
    CONSTRAINT fk_pokedexes_pokedexes_version_groups FOREIGN KEY (pokedex_id)
		  REFERENCES pokedexes (pokedex_id)
);

CREATE TABLE versions (
	  version_id			    INT UNSIGNED AUTO_INCREMENT,
    name			        	VARCHAR(45) NOT NULL,
    version_group_id	  INT UNSIGNED NOT NULL,
    CONSTRAINT pk_versions PRIMARY KEY (version_id),
    CONSTRAINT fk_version_groups_versions FOREIGN KEY (version_group_id)
		  REFERENCES version_groups (version_group_id)
);

CREATE TABLE types_generations (
	type_generation_id		INT UNSIGNED AUTO_INCREMENT,
	type_id				      	INT UNSIGNED NOT NULL,
    generation_id		  	INT UNSIGNED NOT NULL,
    CONSTRAINT pk_types_generations PRIMARY KEY (type_generation_id),
    CONSTRAINT fk_types_types_generations FOREIGN KEY (type_id)
		  REFERENCES types (type_id),
    CONSTRAINT fk_generations_types_generations FOREIGN KEY (generation_id)
		  REFERENCES generations (generation_id)
);