'use strict';
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('Notes', {
      id: { allowNull:false, autoIncrement:true, primaryKey:true, type:Sequelize.INTEGER },
      projectId: {
        type: Sequelize.INTEGER,
        allowNull: false,
        references: { model: 'Projects', key: 'id' },
        onDelete: 'CASCADE',
        onUpdate: 'CASCADE'
      },
      content: { type: Sequelize.TEXT },
      createdAt: { allowNull:false, type:Sequelize.DATE },
      updatedAt: { allowNull:false, type:Sequelize.DATE }
    });
  },
  async down(queryInterface) { await queryInterface.dropTable('Notes'); }
};