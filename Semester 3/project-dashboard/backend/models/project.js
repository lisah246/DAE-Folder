'use strict';
module.exports = (sequelize, DataTypes) => {
  const Project = sequelize.define('Project', {
    clientId: DataTypes.INTEGER,
    name: DataTypes.STRING,
    description: DataTypes.TEXT,
    dueDate: DataTypes.DATE
  }, {});
  Project.associate = (models) => {
    Project.belongsTo(models.Client, { foreignKey: 'clientId' });
    Project.hasMany(models.Task,  { foreignKey: 'projectId' });
    Project.hasMany(models.Note,  { foreignKey: 'projectId' });
  };
  return Project;
};
