const { Sequelize } = require('sequelize');
const fs = require('fs');

(async () => {
  const db = new Sequelize({ dialect: 'sqlite', storage: './database.sqlite', logging: false });
  const [dump] = await db.query("SELECT sql FROM sqlite_master WHERE type IN ('table','index','trigger') ORDER BY name;");
  fs.writeFileSync('../deliverables/week1/sql1_export.sql', dump.map(r => r.sql).join(';\n') + ';');
  console.log("✅ Dump written to deliverables/week1/sql1_export.sql");
  process.exit(0);
})();