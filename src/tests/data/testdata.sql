BEGIN TRANSACTION;
INSERT INTO User (Company,Password,Email,Contact,Telephone) VALUES
    ('TestCompany', 'Test123', 'Test@email.com', 'Max Mustermann', '123456789'),
    ('Pellentesque Habitant Associates','montes,','malesuada.vel@icloud.ca','Hyatt Bowman','(0066) 72440298'),
    ('Amet Dapibus PC','a','iaculis.odio.nam@google.com','Coby Baker','(039616) 378433'),
    ('Id Blandit Industries','ligula','metus@outlook.org','Zane Floyd','(032822) 868843'),
    ('Ultrices Vivamus Rhoncus LLP','Duis','non@hotmail.edu','Fitzgerald Webster','(084) 58932177'),
    ('Porttitor Vulputate Incorporated','mauris.','dapibus@yahoo.edu','Odysseus Yates','(09677) 5835891'),
    ('Risus Consulting','consectetuer','fermentum.convallis.ligula@yahoo.couk','Jayme Nolan','(0460) 43159647'),
    ('Dui Lectus Rutrum Industries','augue','magna.nec.quam@icloud.couk','Elliott Snider','(038035) 033847'),
    ('Pede Suspendisse Institute','vitae,','arcu.iaculis@icloud.ca','Tallulah Grimes','(05221) 6468975'),
    ('Interdum Ligula Inc.','erat,','elit.fermentum.risus@outlook.net','Paula Patrick','(01973) 3854046'),
    ('Nam Tempor LLC','luctus','rutrum.magna@icloud.ca','Connor Anthony','(0841) 31273889');

INSERT INTO Faq (Question, Answer) VALUES
    ('Wer bin Ich?','A'),
    ('Wo bin Ich?', 'B'),
    ('Was bin Ich?', 'C'),
    ('Wie bin Ich?', 'D');

INSERT INTO Request VALUES
/* ID, UserID, Days, Remarks, TableCount, ChairCount, LectureTopic, LectureLenght, Status*/
    (1,7,2,'dis parturient',1,4,'mattis. Cras eget nisi dictum',45,1),
    (2,6,2,'penatibus et',0,5,'Duis ac arcu. Nunc mauris.',3,1),
    (3,6,3,'elit. Nulla',1,3,'ac mi eleifend egestas. Sed',10,1),
    (4,8,2,'dolor. Fusce',2,1,'orci, in consequat enim diam',29,1),
    (5,3,1,'sit amet',1,0,'placerat. Cras dictum ultricies ligula.',35,2);
COMMIT;