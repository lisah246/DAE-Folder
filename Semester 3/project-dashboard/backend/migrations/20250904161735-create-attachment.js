'use strict';
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('Attachments', {
      id: { allowNull:false, autoIncrement:true, primaryKey:true, type:Sequelize.INTEGER },
      taskId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        references: { model: 'Tasks', key: 'id' },
        onDelete: 'CASCADE',
        onUpdate: 'CASCADE'
      },
      originalName: { type: Sequelize.STRING },
      storedName:   { type: Sequelize.STRING },
      mimeType:     { type: Sequelize.STRING },
      size:         { type: Sequelize.INTEGER },
      uploadedAt:   { type: Sequelize.DATE },
      createdAt: { allowNull:false, type:Sequelize.DATE },
      updatedAt: { allowNull:false, type:Sequelize.DATE }
    });
  },
  async down(queryInterface) { await queryInterface.dropTable('Attachments'); }
};