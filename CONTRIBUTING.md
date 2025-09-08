# Contributing to Project Dashboard

Thank you for your interest in contributing to **Project Dashboard**!  
This project is a learning-focused web app that helps track Clients, Projects, Tasks, Notes, and Attachments. It is built with Node.js + Express (backend), SQLite + Sequelize (database), and Next.js + Tailwind/ShadCN (frontend). We welcome contributions that improve code, design, documentation, and testing.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Testing](#testing)
- [Deliverables](#deliverables)
- [Community](#community)

---

## Code of Conduct

This project is governed by a simple code of conduct. By contributing, you agree to:

- **Be respectful**: Treat peers, instructors, and reviewers with courtesy.  
- **Be inclusive**: Contributions are welcome from everyone, regardless of experience level.  
- **Be collaborative**: Ask questions, document changes, and review others’ work constructively.  
- **Be constructive**: Suggest improvements kindly, avoid negative or dismissive language.  

If you encounter inappropriate behavior, please report it directly to the course instructor.

---

## Getting Started

### Prerequisites

- Node.js (LTS, v18+ recommended)  
- Git  
- SQLite3 (bundled with Sequelize; optional CLI for dumps)  
- Netlify CLI (for backend deployment)  
- Vercel CLI (for frontend deployment)

### First-Time Setup

1. **Fork the repository**
   ```bash
   # On GitHub, click "Fork" and fork to your account

2. **Clone your fork**
git clone https://github.com/YOUR_USERNAME/project-dashboard.git
cd project-dashboard

3. **Backend install**
cd backend
npm install

4. **Frontend intall (after Week 2 setup)**
cd ../frontend
npm install

## Development Setup
## Backend (Express + Sequelize + SQLite)
cd backend
npm run dev

Runs API at: http://localhost:3001

Example: http://localhost:3001/api/projects

## Frontend (Next.js + Tailwind/ShadCN)
cd frontend
npm run dev

Runs app at: http://localhost:3000

## Deployment

Backend: Netlify Functions

Frontend: Vercel

## Coding Standards
JavaScript Guidelines

Use camelCase for variables and functions.

Use PascalCase for React components and classes.

Use async/await for async flows.

Keep routes small; move logic into controllers/ if needed.

## File Organization
project-dashboard/
├── backend/
│   ├── routes/         # Express route handlers
│   ├── models/         # Sequelize models
│   ├── migrations/     # Sequelize migrations
│   └── seeders/        # Sample data
├── frontend/
│   ├── pages/          # Next.js routes
│   ├── components/     # UI components
│   └── styles/         # Tailwind styles
├── docs/adr/           # Architecture Decision Records
└── deliverables/       # Weekly rubric evidence

## Commit Guidelines
## Format
type(scope): description

## Types

feat: New feature

fix: Bug fix

docs: Documentation changes

style: Code style only (no logic)

refactor: Code refactoring

test: Adding/updating tests

chore: Maintenance tasks

## Examples
feat(projects): add CRUD endpoints for projects
fix(tasks): correct status filter query
docs(contributing): add ADR references

## Pull Request Process
## Before Submitting

 Code follows style guidelines

 Queries and endpoints tested locally

 Screenshots or .sql/JSON deliverables saved in correct week folder

 Documentation updated if needed

## PR Template
## Description
[Brief description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Breaking change

## Testing
- [ ] Queries tested locally
- [ ] Endpoints verified
- [ ] Deliverables added

## Screenshots (if applicable)

## Issue Reporting
## Bug Report Template
**Bug Description**
Clear explanation of what is broken.

**Steps to Reproduce**
1. ...
2. ...
3. ...

**Expected Behavior**
...

**Actual Behavior**
...

**Environment**
- OS: Windows 10/macOS 12
- Browser: Chrome/Edge
- Node.js version: v18

Feature Request Template
**Feature Description**
Describe the feature idea.

**Problem Statement**
Why is this needed?

**Proposed Solution**
How it should work.

**Alternatives**
Other ways considered.

**Testing**
Running Tests

Currently, manual testing with curl or browser:
# List projects
curl.exe http://localhost:3001/api/projects

# Create a project
curl.exe -X POST http://localhost:3001/api/projects ^
  -H "Content-Type: application/json" ^
  -d "{\"clientId\":1,\"name\":\"Website Revamp\",\"description\":\"Marketing site\"}"

**Future**

Unit tests: Jest (planned)

Integration tests: API + DB checks

End-to-end: Browser-based flows once frontend matures

**Deliverables**

Each week’s rubric evidence is saved under /deliverables/weekX/.
Examples:

week1/01_server_running.png

week2/sql2_queries.sql

week3/report-week3.pdf

week4/FIGMA_PROTOTYPE_LINK.txt

This ensures instructors can quickly verify rubric completion.

**Community**

ADRs: All major technical decisions are recorded under docs/adr/.

Communication: Use GitHub issues + pull requests for collaboration.

Acknowledgments: Contributions (even documentation or bug reports) are valued and credited in commits + PRs.


---

👉 This version is customized to your **Project Dashboard** (tech stack, deliverables, and rubric).  

Would you like me to also generate a **short PR template file (`.github/pull_request_template.md`)** to pair with this CONTRIBUTING guide, so every PR you open has the checklist already?
