const { Sequelize } = require("sequelize");
(async () => {
  try {
    const sequelize = new Sequelize({
      dialect: "sqlite",
      storage: "./database.sqlite",
      logging: false
    });
    await sequelize.authenticate();
    console.log("✅ SQLite connection OK");
    process.exit(0);
  } catch (err) {
    console.error("❌ DB connection error:", err.message);
    process.exit(1);
  }
})();
