const express = require("express");
const router = express.Router();
const { sequelize } = require("../models");

// GET /api/reports/summary
router.get("/summary", async (req, res) => {
  try {
    const [[totals]] = await sequelize.query(`
      SELECT
        (SELECT COUNT(*) FROM Clients)  AS clients,
        (SELECT COUNT(*) FROM Projects) AS projects,
        (SELECT COUNT(*) FROM Tasks)    AS tasks
    `);

    const [statusBreakdown] = await sequelize.query(`
      SELECT status, COUNT(*) AS count
      FROM Tasks
      GROUP BY status
      ORDER BY count DESC, status
    `);

    const [overdue] = await sequelize.query(`
      SELECT id, title, dueDate
      FROM Tasks
      WHERE status != 'done' AND dueDate < date('now')
      ORDER BY dueDate
    `);

    const [upcoming] = await sequelize.query(`
      SELECT id, title, dueDate
      FROM Tasks
      WHERE dueDate BETWEEN date('now') AND date('now','+7 day')
      ORDER BY dueDate
    `);

    const [completion] = await sequelize.query(`
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
      ORDER BY p.id
    `);

    res.json({ totals, statusBreakdown, overdue, upcoming, completion });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "report_failed" });
  }
});

module.exports = router;
