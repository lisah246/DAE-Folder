'use strict';
module.exports = (sequelize, DataTypes) => {
  const Client = sequelize.define('Client', {
    name: DataTypes.STRING,
    email: DataTypes.STRING,
    phone: DataTypes.STRING
  }, {});
  Client.associate = (models) => {
    Client.hasMany(models.Project, { foreignKey: 'clientId' });
  };
  return Client;
};
