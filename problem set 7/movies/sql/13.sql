SELECT DISTINCT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT movies.id FROM movies JOIN stars ON movies.id = stars.movie_id WHERE person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958))) AND people.name != "Kevin Bacon";