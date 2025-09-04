module.exports = {
  async up (qi) {
    await qi.bulkInsert('Clients', [
      { name:'Acme Co',    email:'info@acme.com',       phone:'555-1001', createdAt:new Date(), updatedAt:new Date() },
      { name:'Globex Inc', email:'hello@globex.io',     phone:'555-1002', createdAt:new Date(), updatedAt:new Date() },
      { name:'Initech',    email:'contact@initech.com', phone:'555-1003', createdAt:new Date(), updatedAt:new Date() },
    ]);
  },
  async down (qi) { await qi.bulkDelete('Clients', null, {}); }
};