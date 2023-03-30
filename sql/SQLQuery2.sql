INSERT INTO music_app.dbo.Artists
VALUES (1,'Rich Brian','Solo',NULL),
	   (2, 'Maroon 5',NULL,'Bands'),
	   (3, 'Justin Bieber','Solo',NULL);

INSERT INTO music_app.dbo.Producer
VALUES (1,'John McDonald'),
	   (2, 'Kenzy Upton'),
	   (3, 'John Still');

INSERT INTO music_app.dbo.Albums
VALUES (1,'Cat Paws','2020-10-2',1,1),
	   (2, 'Cheesecake','2018-05-12',2,3),
	   (3, 'Rolling Rocks','2017-12-12',3,2);

INSERT INTO music_app.dbo.Songs
VALUES (1,'Dark Rooms','3:30',3),
	   (2, 'Sweet Bullet','4:40',2),
	   (3, 'Meow Meow 9000','2:58',1);

INSERT INTO music_app.dbo.Playlist
VALUES (1,'Best of the Best','10:00',1,NULL),
	   (2, 'Earth is flat','15:13',2,NULL),
	   (3, 'I am hungry','7:59',3,NULL);
