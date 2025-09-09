-- ORDER BY (Projects by due date)
SELECT id, name, dueDate FROM Projects ORDER BY dueDate ASC;

-- WHERE (Clients with '.com' emails)
SELECT id, name, email FROM Clients WHERE email LIKE '%com%';
