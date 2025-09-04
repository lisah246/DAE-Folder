const { Sequelize } = require('sequelize');
const tables = ['Clients','Projects','Tasks','Notes','Attachments'];

(async () => {
  const db = new Sequelize({ dialect:'sqlite', storage:'./database.sqlite', logging:false });
  for (const t of tables) {
    const [rows] = await db.query(`PRAGMA table_info(${t});`);
    console.log(`\n=== ${t} ===`);
    console.table(rows.map(r => ({
      cid: r.cid, name: r.name, type: r.type, notnull: r.notnull, pk: r.pk
    })));
  }
  process.exit(0);
})();