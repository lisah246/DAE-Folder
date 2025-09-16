// backend/server.js
const express = require("express");
const app = express();

app.use(express.json());

// ⬇️ IMPORT ROUTES — only once
const projectRoutes = require("./routes/projects");
const clientRoutes  = require("./routes/clients");
const reportRoutes = require("./routes/reports");


// ⬇️ REGISTER ROUTES — only once
app.use("/api", projectRoutes);
app.use("/api", clientRoutes);
app.use("/api/reports", reportRoutes);

// Health check
app.get("/", (_req, res) => res.send("Backend is working!"));

// Start
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));