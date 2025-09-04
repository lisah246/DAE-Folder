'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Task extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Task.associate = function(models) {
      Task.belongsTo(models.Project, { foreignKey: 'projectId' });
      Task.hasMany(models.Attachment, { foreignKey: 'taskId' });
  };
    }
  }
  Task.init({
    projectId: DataTypes.INTEGER,
    title: DataTypes.STRING,
    status: DataTypes.STRING,
    dueDate: DataTypes.DATE
  }, {
    sequelize,
    modelName: 'Task',
  });
  return Task;
};