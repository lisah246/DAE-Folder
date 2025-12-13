#ProjectPulse: Database Schema & Operations

#1. Schema Creation (DDL)
#These SQL statements define the relational structure for the application's Projects, Tasks, and Risks.
-- 1. Create Projects Table
CREATE TABLE projects (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    owner VARCHAR(100),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) CHECK (status IN ('Planning', 'In Progress', 'On Hold', 'Completed', 'At Risk')),
    progress INT DEFAULT 0
);

-- 2. Create Tasks Table (One-to-Many relationship with Projects)
CREATE TABLE tasks (
    id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(36) NOT NULL,
    title VARCHAR(255) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    due_date DATE,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- 3. Create Risks Table (One-to-Many relationship with Projects)
CREATE TABLE risks (
    id VARCHAR(36) PRIMARY KEY,
    project_id VARCHAR(36) NOT NULL,
    description TEXT NOT NULL,
    severity VARCHAR(20) CHECK (severity IN ('Low', 'Medium', 'High', 'Critical')),
    mitigation_plan TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

#2. Data Operations (DML)
#INSERT Operation
#Demonstrates how a new project is created in the system.
-- Create a new project
INSERT INTO projects (id, name, description, owner, start_date, status, progress)
VALUES (
    '550e8400-e29b-41d4-a716-446655440000', 
    'Cloud Migration Beta', 
    'Migrating legacy on-prem services to cloud infrastructure.', 
    'Jane Doe', 
    '2024-03-01', 
    'Planning', 
    0
);

#SELECT Operation (Basic)
#Used for the Dashboard view to calculate high-level metrics.
-- Retrieve all active projects and their progress
SELECT name, owner, status, progress 
FROM projects 
WHERE status != 'Completed' 
ORDER BY progress DESC;

#SELECT Operation (Join)
#Used for the Project Details view to show a project alongside its specific tasks.
-- specific project
SELECT 
    p.name AS ProjectName,
    t.title AS TaskTitle,
    t.due_date AS DueDate,
    t.is_completed AS IsDone
FROM projects p
JOIN tasks t ON p.id = t.project_id
WHERE p.id = '550e8400-e29b-41d4-a716-446655440000';