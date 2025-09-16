## SQL Queries

# This file contains SQL queries used in the project.

# 1) Totals (projects, clients, tasks)

SELECT
  (SELECT COUNT(*) FROM Clients)  AS clients,
  (SELECT COUNT(*) FROM Projects) AS projects,
  (SELECT COUNT(*) FROM Tasks)    AS tasks;

# 2) Task status breakdown

SELECT
  (SELECT COUNT(*) FROM Clients)  AS clients,
  (SELECT COUNT(*) FROM Projects) AS projects,
  (SELECT COUNT(*) FROM Tasks)    AS tasks;

# 3) Overdue tasks (not done)

SELECT id, title, dueDate
FROM Tasks
WHERE status != 'done'
  AND dueDate < date('now')
ORDER BY dueDate;

# 4) Upcoming tasks (next 7 days)
SELECT id, title, dueDate
FROM Tasks
WHERE status != 'done'
  AND dueDate < date('now')
ORDER BY dueDate;

# 5) Project completion % (done/total)
SELECT
  p.id,
  p.name,
  ROUND(
    100.0 * SUM(CASE WHEN t.status='done' THEN 1 ELSE 0 END) / NULLIF(COUNT(t.id),0),
    1
  ) AS completionPct
FROM Projects p
LEFT JOIN Tasks t ON t.projectId = p.id
GROUP BY p.id, p.name
ORDER BY p.id;
