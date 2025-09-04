// backend/server.js
const express = require("express");
const app = express();
app.use(express.json());

// health check
app.get("/", (_req, res) => res.send("Backend is working!"));

// start
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
