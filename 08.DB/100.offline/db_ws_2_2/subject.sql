-- Active: 1752639458321@@localhost@3306@movies
SELECT * 
FROM movie_list
WHERE
release_year > 2010;


SELECT * 
FROM movie_list
WHERE
genre = 'ACTION' OR genre = 'Sci-Fi';

SELECT * 
FROM movie_list
WHERE
title LIKE '%The%';


SELECT * 
FROM movie_list
WHERE
release_year >= 2008 and release_year <= 2014;

SELECT * 
FROM movie_list
WHERE
release_year IS NULL