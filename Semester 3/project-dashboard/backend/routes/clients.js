const express = require("express");
const router = express.Router();
const { Client } = require("../models");

// GET /api/clients (ordered by name)
router.get("/clients", async (_req, res) => {
  try {
    const clients = await Client.findAll({ order: [["name", "ASC"]] });
    res.json(clients);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// POST /api/clients
router.post("/clients", async (req, res) => {
  const { name, email, phone } = req.body || {};
  if (!name || !email) {
    return res.status(400).json({ error: "name and email are required" });
  }
  try {
    const client = await Client.create({ name, email, phone });
    res.status(201).json(client);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// PUT /api/clients/:id
router.put("/clients/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const [count] = await Client.update(req.body, { where: { id } });
    if (!count) return res.status(404).json({ error: "Not found" });
    const updated = await Client.findByPk(id);
    res.json(updated);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// DELETE /api/clients/:id
router.delete("/clients/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const count = await Client.destroy({ where: { id } });
    if (!count) return res.status(404).json({ error: "Not found" });
    res.json({ ok: true });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

module.exports = router;