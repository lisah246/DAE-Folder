'use strict';
module.exports = (sequelize, DataTypes) => {
  const Note = sequelize.define('Note', {
    projectId: DataTypes.INTEGER,
    content: DataTypes.TEXT
  }, {});
  Note.associate = (models) => {
    Note.belongsTo(models.Project, { foreignKey: 'projectId' });
  };
  return Note;
};
