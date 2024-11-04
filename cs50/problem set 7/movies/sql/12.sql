SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON stars.person_id = people.id
WHERE name IN ('Bradley Cooper', 'Jennifer Lawrence')
GROUP BY movie_id
HAVING COUNT(distinct person_id) = 2;