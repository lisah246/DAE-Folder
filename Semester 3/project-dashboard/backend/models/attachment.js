'use strict';
module.exports = (sequelize, DataTypes) => {
  const Attachment = sequelize.define('Attachment', {
    taskId: DataTypes.INTEGER,
    originalName: DataTypes.STRING,
    storedName: DataTypes.STRING,
    mimeType: DataTypes.STRING,
    size: DataTypes.INTEGER,
    uploadedAt: DataTypes.DATE
  }, {});
  Attachment.associate = (models) => {
    Attachment.belongsTo(models.Task, { foreignKey: 'taskId' });
  };
  return Attachment;
};
