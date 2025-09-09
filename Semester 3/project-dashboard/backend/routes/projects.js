const express = require("express");
const router = express.Router();
const { Project, Client } = require("../models");

// GET /api/projects  (ordered by dueDate for SQL-2 ORDER BY)
router.get("/projects", async (_req, res) => {
  try {
    const projects = await Project.findAll({
      include: [{ model: Client, attributes: ["name"] }],
      order: [["dueDate", "ASC"]]
    });
    res.json(projects);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// POST /api/projects
router.post("/projects", async (req, res) => {
  const { clientId, name, description, dueDate } = req.body || {};
  if (!clientId || !name) return res.status(400).json({ error: "clientId and name are required" });
  try {
    const project = await Project.create({ clientId, name, description, dueDate });
    res.status(201).json(project);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// PUT /api/projects/:id
router.put("/projects/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const [count] = await Project.update(req.body, { where: { id } });
    if (!count) return res.status(404).json({ error: "Not found" });
    const updated = await Project.findByPk(id);
    res.json(updated);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// DELETE /api/projects/:id
router.delete("/projects/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const count = await Project.destroy({ where: { id } });
    if (!count) return res.status(404).json({ error: "Not found" });
    res.json({ ok: true });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

module.exports = router;