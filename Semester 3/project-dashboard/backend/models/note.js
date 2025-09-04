'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Note extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Note.associate = function(models) {
      Note.belongsTo(models.Project, { foreignKey: 'projectId' });
      };
    }
  }
  Note.init({
    projectId: DataTypes.INTEGER,
    content: DataTypes.TEXT,
    createdAt: DataTypes.DATE
  }, {
    sequelize,
    modelName: 'Note',
  });
  return Note;
};