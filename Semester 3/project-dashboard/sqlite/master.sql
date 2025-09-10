PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Attachments;
DROP TABLE IF EXISTS Notes;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Clients;

CREATE TABLE Clients(
  id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, phone TEXT
);
CREATE TABLE Projects(
  id INTEGER PRIMARY KEY, clientId INTEGER NOT NULL, name TEXT NOT NULL,
  dueDate TEXT, FOREIGN KEY (clientId) REFERENCES Clients(id) ON DELETE CASCADE
);
CREATE TABLE Tasks(
  id INTEGER PRIMARY KEY, projectId INTEGER NOT NULL, title TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN('todo','in_progress','done')),
  dueDate TEXT, FOREIGN KEY(projectId) REFERENCES Projects(id) ON DELETE CASCADE
);
CREATE TABLE Notes(
  id INTEGER PRIMARY KEY, projectId INTEGER NOT NULL, content TEXT NOT NULL,
  FOREIGN KEY(projectId) REFERENCES Projects(id) ON DELETE CASCADE
);
CREATE TABLE Attachments(
  id INTEGER PRIMARY KEY, taskId INTEGER NOT NULL, originalName TEXT,
  size INTEGER, FOREIGN KEY(taskId) REFERENCES Tasks(id) ON DELETE CASCADE
);

INSERT INTO Clients(name,email,phone) VALUES
 ('Acme Co','info@acme.com','555-1001'),
 ('Globex Inc','hello@globex.io','555-1002'),
 ('Initech','contact@initech.com','555-1003');

INSERT INTO Projects(clientId,name,dueDate) VALUES
 (1,'Website Revamp','2025-10-15'),
 (1,'Mobile App','2025-11-01'),
 (2,'Data Pipeline','2025-12-05');

INSERT INTO Tasks(projectId,title,status,dueDate) VALUES
 (1,'Wireframes','done','2025-09-10'),
 (1,'Frontend build','in_progress','2025-09-20'),
 (2,'ETL step','todo','2025-09-22');

INSERT INTO Notes(projectId,content) VALUES
 (1,'Kickoff complete'), (2,'Data mapping approved');

INSERT INTO Attachments(taskId,originalName,size) VALUES
 (2,'ui.png',10240), (3,'etl.pdf',20480);

-- Examples to run after loading:
-- .headers on
-- .mode column
-- SELECT * FROM Clients;
