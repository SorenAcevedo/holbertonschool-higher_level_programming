SELECT cities.id, cities.name, states.name
FROM states INNER JOIN cities ON states.id = state_id
ORDER BY cities.id;