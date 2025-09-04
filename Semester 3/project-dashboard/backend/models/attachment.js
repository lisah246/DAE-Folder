'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Attachment extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Attachment.associate = function(models) {
      Attachment.belongsTo(models.Task, { foreignKey: 'taskId' });
  };
    }
  }
  Attachment.init({
    taskId: DataTypes.INTEGER,
    originalName: DataTypes.STRING,
    storedName: DataTypes.STRING,
    mimeType: DataTypes.STRING,
    size: DataTypes.INTEGER,
    uploadedAt: DataTypes.DATE
  }, {
    sequelize,
    modelName: 'Attachment',
  });
  return Attachment;
};