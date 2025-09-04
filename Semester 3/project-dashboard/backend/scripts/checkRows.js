const { Sequelize } = require('sequelize');
(async () => {
  const db = new Sequelize({ dialect:'sqlite', storage:'./database.sqlite', logging:false });
  const [clients]  = await db.query('SELECT id, name, email FROM Clients;');
  const [projects] = await db.query('SELECT id, clientId, name FROM Projects;');
  console.log('\nClients:');  console.table(clients);
  console.log('\nProjects:'); console.table(projects);
  process.exit(0);
})();