# 6-Month Backend Web Development Track

A comprehensive track emphasizing backend development, full-stack integration, and workforce readiness.

# Portfolio Links

**LinkedIn**
https://www.linkedin.com/in/lhom01/

**GitHub**
https://lisah246.github.io/DAE-Folder/

## Structure

- **Semester 1**: Foundations in Unix, Python, Logic, and early prompt engineering experiments  
  - unix_1, unix_2, python_1, python_2, logic_1, Tkinter survival game (prompt engineering)

- **Semester 2**: Workforce Development & Professional Artifacts  
  - LinkedIn profiles, resumes, GitHub portfolio pages, foundation deck, IDP, feedback summaries, project board

- **Semester 3**: Backend Development & Full-Stack Integration  
  - Client & Project Management Dashboard (Node.js, Express, SQLite/Sequelize, Next.js, ShadCN, Tailwind CSS, PDF export, notifications, role-based dashboards)

## Highlights

- **Backend Development**: Node.js + Express + SQLite/Sequelize ORM  
- **Frontend Development**: Next.js with ShadCN UI + Tailwind CSS  
- **Project Management Features**: CRUD for projects/clients/tasks, PDF reporting, notifications, role-based dashboards  
- **Workforce Development**: Professional resumes, LinkedIn profiles, and GitHub portfolios  
- **Artifacts**: Project plan, design doc, weekly milestones, deployment workflow  

## Tech Stack

**Languages**
- JavaScript (Node.js, React/Next.js)
- SQL (SQLite via Sequelize ORM)
- TypeScript (frontend)
- CSS (Tailwind CSS + TweakCN)

**Backend**
- Runtime: Node.js  
- Framework: Express.js  
- ORM: Sequelize with SQLite  
- Email: Nodemailer  

**Frontend**
- Framework: Next.js (React-based)  
- UI Library: ShadCN  
- Styling: Tailwind CSS + TweakCN  
- Charts: Chart.js or Recharts  

**Additional Tools**
- PDF generation: jsPDF or pdf-lib  
- Authentication: Custom role-based (Auth.js)  
- File Handling: Multer  
- Demo Data: Faker.js  

**Deployment**
- Frontend: Vercel  
- Backend: Netlify Functions  
- Database: SQLite (with migration path to PostgreSQL)  

## Navigation

- [Semester 2 README](./semester2/README.md)
- [Semester 3 README](./semester3/README.md)

## Setup Instructions

Clone the repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/backend-track.git
cd backend-track

## Backend
cd backend
npm install
npm run dev

API available at: http://localhost:8000/api

## Frontend
cd frontend
npm install
npm run dev

Frontend available at: http://localhost:3000