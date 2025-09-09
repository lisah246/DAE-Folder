// scripts/sql2_day1.js
const { Sequelize } = require('sequelize');

(async () => {
  const db = new Sequelize({
    dialect: 'sqlite',
    storage: './database.sqlite',
    logging: false
  });

  // ORDER BY: Projects by due date
  const [ordered] = await db.query(
    "SELECT id, name, dueDate FROM Projects ORDER BY dueDate ASC;"
  );
  console.log("\n=== ORDER BY (Projects by dueDate ASC) ===");
  console.table(ordered);

  // WHERE: Clients with '.com' in email
  const [filtered] = await db.query(
    "SELECT id, name, email FROM Clients WHERE email LIKE '%com%';"
  );
  console.log("\n=== WHERE (Clients WHERE email LIKE '%com%') ===");
  console.table(filtered);

  process.exit(0);
})();