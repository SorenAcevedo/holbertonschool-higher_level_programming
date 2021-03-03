-- Script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_show ON tv_show_genres.show_id = tv_show.id
WHERE tv_show.name = "Dexter"
ORDER BY tv_genres.name;