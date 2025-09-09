'use strict';
module.exports = (sequelize, DataTypes) => {
  const Task = sequelize.define('Task', {
    projectId: DataTypes.INTEGER,
    title: DataTypes.STRING,
    status: DataTypes.STRING,
    dueDate: DataTypes.DATE
  }, {});
  Task.associate = (models) => {
    Task.belongsTo(models.Project, { foreignKey: 'projectId' });
    Task.hasMany(models.Attachment, { foreignKey: 'taskId' });
  };
  return Task;
};
