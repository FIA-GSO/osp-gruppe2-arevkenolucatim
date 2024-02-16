/*

CREATE TABLE faq (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    question  TEXT NOT NULL,
    answer    TEXT NOT NULL
);
*/
DROP TABLE IF EXISTS Faq;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Request;

CREATE TABLE User (
	ID	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Company	    TEXT NOT NULL,
	Password	TEXT NOT NULL,
	Email	    TEXT NOT NULL,
	Contact	    TEXT,
	Telephone	TEXT
);

CREATE TABLE Faq (
	ID	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Question	TEXT,
	Answer	    TEXT
);

CREATE TABLE Request (
	ID	            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	UserID	        INTEGER NOT NULL,
	Days	        INTEGER NOT NULL,
	Remarks	        TEXT,
	TableCount	    INTEGER,
	ChairCount	    INTEGER,
	LectureTopic	TEXT,
	LectureLength   INTEGER,
	Status	        INTEGER NOT NULL
);