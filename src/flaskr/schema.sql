DROP TABLE IF EXISTS Faq;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Request;

/*
 * Alle registrierten Benutzer und Organisationsteam
 */
CREATE TABLE User (
	ID	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Company	    TEXT NOT NULL,
	Password	TEXT NOT NULL,
	Email	    TEXT NOT NULL,
	Contact	    TEXT,
	Telephone	TEXT
);

/*
 * FAQ
 */
CREATE TABLE Faq (
	ID	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Question	TEXT,
	Answer	    TEXT
);

/*
 * Anmeldeformulardaten
 */
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

/*
 * Anmeldeformulardaten
 */
CREATE TABLE GuestRequest (
	ID	            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Company			TEXT,
	Email			TEXT,
	Telephone		TEXT,
	Contact			TEXT,
	Remarks			TEXT,
	Days	        INTEGER NOT NULL,
	TableCount	    INTEGER,
	ChairCount	    INTEGER,
	LectureTopic	TEXT,
	LectureLength   INTEGER,
	Status	        INTEGER NOT NULL
);