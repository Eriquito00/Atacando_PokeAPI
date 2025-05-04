USE pokemon_db;

/* Pokemons con su tipo y su generacion */

SELECT p.name AS pokemon, t.name AS type, g.name AS generation
	FROM pokemons p
	INNER JOIN types t ON p.type_id = t.type_id
	INNER JOIN generations g ON p.generation_id = g.generation_id;
    
/* Pokemons ordenados por altura y por peso */
SELECT name, height, weight
	FROM pokemons
ORDER BY height DESC, weight DESC;

/* Regiones con las versiones que tiene cada una */
SELECT r.name AS region, v.name AS version
	FROM versions v
	INNER JOIN version_groups vg ON v.version_group_id = vg.version_group_id
	INNER JOIN regions r ON vg.region_id = r.region_id;
    
/* Cuantas ubicaciones tiene cada region */
SELECT r.name AS region, COUNT(l.location_id) AS cantidad
	FROM locations l
	INNER JOIN regions r ON l.region_id = r.region_id
GROUP BY r.region_id;

/* Tipos con la altura y peso promedios */
SELECT t.name AS tipo, ROUND(AVG(p.height),2) AS altura_promedio, ROUND(AVG(p.weight),2) AS peso_promedio
	FROM pokemons p
	INNER JOIN types t ON p.type_id = t.type_id
GROUP BY t.type_id;