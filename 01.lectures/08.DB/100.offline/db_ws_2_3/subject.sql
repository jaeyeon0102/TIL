SELECT * 
FROM movie_list
WHERE
release_year >= 2000 and release_year <= 2010;

SELECT * 
FROM movie_list
WHERE
title >= 'A' AND title < 'M';


SELECT * 
FROM movie_list
WHERE
genre = 'Drama' AND release_year >1990 AND release_year < 2000;

SELECT * 
FROM movie_list
WHERE
release_year >=2015 AND release_year <= 2020
AND (genre = 'Sci-Fi' OR genre = 'Action');

SELECT * 
FROM movie_list
WHERE
release_year >= 2005 and release_year < 2015;