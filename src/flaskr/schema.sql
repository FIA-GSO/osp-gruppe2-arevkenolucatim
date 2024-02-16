/*
DROP TABLE IF EXISTS faq;

CREATE TABLE faq (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    question  TEXT NOT NULL,
    answer    TEXT NOT NULL
);
*/
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS User (
	ID	        INTEGER NOT NULL,
	Company	    TEXT NOT NULL,
	Password	TEXT NOT NULL,
	Email	    TEXT NOT NULL,
	Contact	    TEXT,
	Telephone	TEXT,
	PRIMARY KEY(ID AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS Faq (
	ID	        INTEGER NOT NULL,
	Question	TEXT,
	Answer	    TEXT,
	PRIMARY KEY(ID AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS Application (
	ID	            INTEGER NOT NULL,
	UserID	        INTEGER NOT NULL,
	Days	        INTEGER NOT NULL,
	Remarks	        TEXT,
	Table	        INTEGER,
	Chair	        INTEGER,
	LectureTopic	TEXT,
	LectureLenght   INTEGER,
	Status	        INTEGER NOT NULL,
	PRIMARY KEY(ID,UserID)
);
COMMIT;