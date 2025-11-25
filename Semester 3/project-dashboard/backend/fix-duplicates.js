// backend/fix-duplicates.js
const { sequelize } = require("./models");

async function fixDuplicates() {
  try {
    // Rename duplicates to make them unique
    await sequelize.query(`UPDATE Projects SET name = 'Website Revamp v2' WHERE id = 4`);
    await sequelize.query(`UPDATE Projects SET name = 'Mobile App v2' WHERE id = 5`);
    await sequelize.query(`UPDATE Projects SET name = 'Data Pipeline v2' WHERE id = 6`);
    await sequelize.query(`UPDATE Projects SET name = 'Temp Delete v2' WHERE id = 9`);
    await sequelize.query(`UPDATE Projects SET name = 'Temp Delete v3' WHERE id = 10`);

    console.log("✅ Duplicates renamed successfully!");
    
    // Show updated projects
    const [projects] = await sequelize.query(`SELECT id, name FROM Projects ORDER BY id`);
    console.log("Updated projects:", projects);
    
  } catch (error) {
    console.error("❌ Error fixing duplicates:", error);
  } finally {
    await sequelize.close();
  }
}

fixDuplicates();