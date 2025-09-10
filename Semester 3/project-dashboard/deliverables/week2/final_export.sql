PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE hello(id INTEGER PRIMARY KEY, msg TEXT);
INSERT INTO hello VALUES(1,'Hello SQLite!');
CREATE TABLE Clients(
  id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, phone TEXT
);
INSERT INTO Clients VALUES(1,'Acme Co','info@acme.com','555-1001');
INSERT INTO Clients VALUES(2,'Globex Inc','hello@globex.io','555-1002');
INSERT INTO Clients VALUES(3,'Initech','contact@initech.com','555-1003');
CREATE TABLE Projects(
  id INTEGER PRIMARY KEY, clientId INTEGER NOT NULL, name TEXT NOT NULL,
  dueDate TEXT, FOREIGN KEY (clientId) REFERENCES Clients(id) ON DELETE CASCADE
);
INSERT INTO Projects VALUES(1,1,'Website Revamp','2025-10-15');
INSERT INTO Projects VALUES(2,1,'Mobile App','2025-11-01');
INSERT INTO Projects VALUES(3,2,'Data Pipeline','2025-12-05');
CREATE TABLE Tasks(
  id INTEGER PRIMARY KEY, projectId INTEGER NOT NULL, title TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN('todo','in_progress','done')),
  dueDate TEXT, FOREIGN KEY(projectId) REFERENCES Projects(id) ON DELETE CASCADE
);
INSERT INTO Tasks VALUES(1,1,'Wireframes','done','2025-09-10');
INSERT INTO Tasks VALUES(2,1,'Frontend build','in_progress','2025-09-20');
INSERT INTO Tasks VALUES(3,2,'ETL step','todo','2025-09-22');
CREATE TABLE Notes(
  id INTEGER PRIMARY KEY, projectId INTEGER NOT NULL, content TEXT NOT NULL,
  FOREIGN KEY(projectId) REFERENCES Projects(id) ON DELETE CASCADE
);
INSERT INTO Notes VALUES(1,1,'Kickoff complete');
INSERT INTO Notes VALUES(2,2,'Data mapping approved');
CREATE TABLE Attachments(
  id INTEGER PRIMARY KEY, taskId INTEGER NOT NULL, originalName TEXT,
  size INTEGER, FOREIGN KEY(taskId) REFERENCES Tasks(id) ON DELETE CASCADE
);
INSERT INTO Attachments VALUES(1,2,'ui.png',10240);
INSERT INTO Attachments VALUES(2,3,'etl.pdf',20480);
COMMIT;
