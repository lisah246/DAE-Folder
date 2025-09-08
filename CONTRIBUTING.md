test
# Contributing

## Prereqs
- Node.js (LTS)
- Git
- No Postman/AWS (per course rules)

## Getting Started
```bash
# backend
cd project-dashboard/backend
npm install
npm run dev  # http://localhost:3001

# frontend (later in Week 2 Day 3)
cd ../frontend
# npx create-next-app .  (done later)

## Branch & Commit

Create feature branches: feat/<short-name> (e.g., feat/projects-crud).

Commit messages: short, present-tense (“add projects list”, “fix client update”).

Open small PRs. Link to issue/task if applicable.

## Code Style

JS/Node (CommonJS). 2-space indent, semicolons ok or not—be consistent.

Routes under backend/routes/. Keep handlers small and async/await based.

No Postman. Use browser or curl to test.

## Testing Locally (examples)
# list projects
curl.exe http://localhost:3001/api/projects

# create a project
curl.exe -X POST http://localhost:3001/api/projects ^
  -H "Content-Type: application/json" ^
  -d "{\"clientId\":1,\"name\":\"Website Revamp\",\"description\":\"Marketing site\"}"

## Deliverables

Save screenshots and .sql/JSON proof in deliverables/weekX/.

Commit these:
```bat
git add docs\adr\0001-stack-and-deployment.md docs\adr\0002-database-schema.md CONTRIBUTING.md
git commit -m "docs: add ADRs and CONTRIBUTING"
