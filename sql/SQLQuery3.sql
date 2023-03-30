SELECT *
FROM music_app.dbo.Playlist
/* this shows Playlist table */

SELECT *
FROM music_app.dbo.Songs
WHERE songLength > '0:20'
/* this shows Songs with length > 0:20 */

INSERT INTO music_app.dbo.Artists
VALUES (4, 'Taylor Swift','Solo',NULL);
/* this inserts new entities into the Artists table */

SELECT *
FROM music_app.dbo.Artists
/* this shows the updated Artists table */

INSERT INTO music_app.dbo.Artists
VALUES (1001,'The Bandz',NULL,'Bands');
/* this inserts new data into the Artists table */

INSERT INTO music_app.dbo.Albums(albumID,albumName,artistID,releaseDate)
VALUES (4,'The White Room',1001,'2010-07-12'),
	   (5, 'SPIRIT',1001,'2013-07-20'),
	   (6, 'Melancholy',1001,'2015-07-17');
/* this inserts new entities for the new Artist into the Albums table */

SELECT *
FROM music_app.dbo.Albums
/* this shows the updated Albums table */

SELECT *
FROM music_app.dbo.Albums
ORDER BY releaseDate
/* this sorts the Albums table by release date */

INSERT INTO music_app.dbo.Albums(albumID, albumName,artistID,releaseDate)
VALUES (1002,'Live Entity',1001,'2019-05-18');
SELECT *
FROM music_app.dbo.Albums
/* this inserts new data to the Albums table */

DELETE FROM music_app.dbo.Albums
WHERE albumName like '%Live%'
SELECT *
FROM music_app.dbo.Albums
ORDER BY releaseDate
/* remove any albums with the word 'Live' in their names and sort by release date */

SELECT *
FROM music_app.dbo.Artists
LEFT JOIN music_app.dbo.Albums
ON music_app.dbo.Artists.artistID = music_app.dbo.Albums.artistID;
/* gets all the values from the Artists and Albums tables */




