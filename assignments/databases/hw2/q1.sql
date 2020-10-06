CREATE TABLE ART (
	ITEM int NOT NULL AUTO_INCREMENT,
	NAME varchar(50),
	ARTIST varchar(50),
	ORIGIN_ID int,
	DATING varchar(50),
	MEDIA varchar(20),
	PRIMARY KEY (ITEM)
);

CREATE TABLE ORIGIN (
	ORIGIN_ID int NOT NULL AUTO_INCREMENT,
	LOCATION varchar(50),
	PRIMARY KEY (ORIGIN_ID)
);

ALTER TABLE ART AUTO_INCREMENT=1000;
ALTER TABLE ORIGIN AUTO_INCREMENT=1000;

INSERT INTO ORIGIN (ORIGIN_ID, LOCATION)
VALUES (1111, 'China'),
(3543, 'France'),
(6943, 'Japan'),
(8415, 'Sri Lanka'),
(1598, 'Tajikistan');

ALTER TABLE ART 
ADD FOREIGN KEY (ORIGIN_ID) REFERENCES ORIGIN(ORIGIN_ID);

INSERT INTO ART (ITEM, NAME, ARTIST, ORIGIN_ID, DATING, MEDIA)
VALUES (9182, 'One Hundred Horses', 'Lang Shining', 1111, '960 to 1127', 'Painting'),
(6922, 'The Great Wave off Kanagawa', 'Katsushika', 6943, '1829 to 1833', 'Painting'),
(2049, 'Toluvila statue', NULL, 8415, '300 to 400', 'Statuary'),
(2038, 'Sasanian silver vessel', NULL, 1598, '700 to 722', 'Silver'),
(3964, 'Nymph of the Luo River', 'Gu Kaizhi', 1111, '317 to 420', 'Painting'),
(3097, 'The Hunt of the Unicorn', NULL, 3543, '1680', 'Tapestries');


