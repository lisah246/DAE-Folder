# ADR 0003 — Role-Based Dashboards & Authentication
**Status:** Accepted  
**Date:** 2025-09-08

## Context
The application serves three types of users: Project Managers, Clients, and Developers. Each group needs different access: PMs require full control, Clients should only see their own projects, and Developers focus on assigned tasks. Role separation is critical for clarity and security.

## Decision
- Implement **custom role-based authentication** in Week 6 of the plan.
- Roles:
  - **Project Manager (PM):** Full access to projects, tasks, notes, reports, client dashboards.
  - **Client:** Read-only access to their projects, ability to comment.
  - **Developer:** Access to tasks assigned to them.
- Frontend will render different dashboards per role:
  - **PM Dashboard:** Projects overview, reports, JIRA-style board.
  - **Client Dashboard:** Only client’s projects, comment section.
  - **Developer Dashboard:** Assigned tasks only.

## Consequences
- Simplifies user experience (users only see what matters to them).
- Supports rubric requirements for multiple dashboards (PM/Client).
- Adds complexity in Week 6 (must secure endpoints + frontend conditionals).
- Provides a strong foundation for later features (notifications, search, attachments).
