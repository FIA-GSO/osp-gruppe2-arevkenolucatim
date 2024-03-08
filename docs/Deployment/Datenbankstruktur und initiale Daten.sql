-- Deployment Script for initializing the structure and initial data of the DB during deployment
DROP TABLE IF EXISTS Faq;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Request;
DROP TABLE IF EXISTS GuestRequest;

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

-- Insert ORGA user
INSERT INTO User (Company, Password, Email, Contact, Telephone)
VALUES ('ORGA', 'PXELKJn1fx1GDN6', 'orga@gso.schule.koeln', 'N/A', 'N/A')

-- Insert initial questions
INSERT INTO Faq (Question, Answer)
VALUES
('Welche Vorteile haben eine Registrierung vs. ein Gastanmeldung für den GSO Marketplace?', 'Sie können jederzeit Ihre Firmendaten sowie Ihren Antrag, für die Teilnahme am GSO Marketplace, bearbeiten. Anmeldeschluss ist eine Woche vor Tag 1 des Jährlichen GSO Marketplace.'),
('Wie kann ich Sie kontaktieren?', 'Bei weiteren Fragen können Sie uns jederzeit über gsomarketplace@gso.schule.koeln Kontaktieren.'),
('Wie können wir Sie unterstützen?', 'Mit einem Jahresbeitrag von mindestens € 12,- können Sie den den “Verein der Freunde, Förderer und Ehemaligen der GEORG-SIMON-OHM-SCHULE, Köln e.V.” unterstützen. Die Satzung des Vereins kann unter https://www.gso-koeln.de/wp-content/uploads/2020/08/Foerderverein-Satzung.pdf eingesehen werden. Bankverbindung: IBAN DE76 3705 0198 0014 6320 79'),
('Kann ich meine Firmen- und Kontaktdaten ändern?', 'Ja, wenn Sie registriert sind.'),
('Was sind die Limits für einen Stand?', 'Abmessungen der Standfläche: ca. 3m x 3m. Stromanschluss (z.B. Beamer/Laptop) vorhanden. Darüber hinaus gehenden Leistungsbedarf bitte im Antrag mit angeben. WLAN-Zugang Vorhanden.')


