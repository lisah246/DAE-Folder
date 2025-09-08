# ADR 0002 — Database Schema (Clients, Projects, Tasks, Notes, Attachments)
**Status:** Accepted  
**Date:** 2025-09-08

## Context
We need to track clients → projects → tasks, add notes to projects, and attach files to tasks. Reports will aggregate tasks by status and due dates.

## Decision (tables)
- **Clients**(id, name, email, phone, timestamps)
- **Projects**(id, clientId FK→Clients, name, description, dueDate, timestamps)
- **Tasks**(id, projectId FK→Projects, title, status['todo'|'in_progress'|'done'], dueDate, timestamps)
- **Notes**(id, projectId FK→Projects, content, timestamps)
- **Attachments**(id, taskId FK→Tasks, originalName, storedName, mimeType, size, uploadedAt, timestamps)

## Consequences
- Clear parent→child relationships that support JOINs and GROUP BY.
- Straightforward to implement CRUD and rubric queries.
- Supports later features: previews, reports, notifications.
