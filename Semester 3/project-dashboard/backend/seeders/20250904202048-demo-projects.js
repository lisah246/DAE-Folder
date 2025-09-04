module.exports = {
  async up (qi) {
    await qi.bulkInsert('Projects', [
      { clientId:1, name:'Website Revamp', description:'Marketing site',   dueDate:'2025-10-15', createdAt:new Date(), updatedAt:new Date() },
      { clientId:1, name:'Mobile App',     description:'iOS + Android',    dueDate:'2025-11-01', createdAt:new Date(), updatedAt:new Date() },
      { clientId:2, name:'Data Pipeline',  description:'ETL improvements', dueDate:'2025-12-10', createdAt:new Date(), updatedAt:new Date() },
    ]);
  },
  async down (qi) { await qi.bulkDelete('Projects', null, {}); }
};