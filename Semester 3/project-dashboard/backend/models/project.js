'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Project extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Project.associate = (models) => {
        Project.belongsTo(models.Client, { foreignKey: 'clientId' });
        Project.hasMany(models.Task, { foreignKey: 'projectId' });
        Project.hasMany(models.Note, { foreignKey: 'projectId' });
};

    }
  }
  Project.init({
    clientId: DataTypes.INTEGER,
    name: DataTypes.STRING,
    description: DataTypes.TEXT,
    dueDate: DataTypes.DATE
  }, {
    sequelize,
    modelName: 'Project',
  });
  return Project;
};