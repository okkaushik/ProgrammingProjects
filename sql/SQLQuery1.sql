CREATE DATABASE music_app;
/* using the default dbo as the schema */

CREATE TABLE music_app.dbo.Artists(
artistID int PRIMARY KEY,
artistName character(20) NOT NULL,
solo character(20),
bands character(20)
);

CREATE TABLE music_app.dbo.Producer(
producerID int PRIMARY KEY,
producerName character(20) NOT NULL
);

CREATE TABLE music_app.dbo.Albums(
albumID int PRIMARY KEY,
albumName character(20) NOT NULL,
releaseDate date NOT NULL,
artistID int,
producerID int,
FOREIGN KEY(artistID) REFERENCES music_app.dbo.Artists(artistID),
FOREIGN KEY(producerID) REFERENCES music_app.dbo.Producer(producerID)
);

CREATE TABLE music_app.dbo.Songs(
songID int PRIMARY KEY,
songTitle character(20) NOT NULL,
songLength time NOT NULL,
albumID int,
FOREIGN KEY(albumID) REFERENCES music_app.dbo.Albums(albumID)
);

CREATE TABLE music_app.dbo.Playlist(
playlistID int PRIMARY KEY,
playlistTitle character(20) NOT NULL,
playlistLength time,
songID int,
playlist_timestamp timestamp,
FOREIGN KEY(songID) REFERENCES music_app.dbo.Songs(songID)
);

