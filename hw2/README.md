# kanban-mini

A lightweight Kanban board application with a Node.js frontend (React + TypeScript + Vite) and Python backend (FastAPI + SQLite).

## Overview

kanban-mini is a minimal, efficient Kanban board app featuring:
- Three fixed columns: Todo, In Progress, Done
- Drag-and-drop task management
- Task creation, editing, and deletion
- Persistent storage via SQLite
- REST API communication between frontend and backend

## Tech Stack

**Frontend:**
- React 18 + TypeScript
- Vite (build tool)
- @dnd-kit/core (drag and drop)
- React Query (TanStack Query) for state management

**Backend:**
- Python 3.11+
- FastAPI (web framework)
- SQLAlchemy 2.0 + aiosqlite (database ORM)
- Pydantic (data validation)
- uv (package manager)

## Project Structure

```
kanban-mini/
├── _docs/
│   └── specs.md          # Detailed specification
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routes
│   │   ├── models/       # Pydantic models
│   │   ├── services/     # Business logic
│   │   ├── db/           # Database setup
│   │   └── main.py       # Application entry point
│   ├── pyproject.toml    # uv configuration
│   └── uv.lock           # Lockfile
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom hooks
│   │   ├── services/     # API client
│   │   ├── types/        # TypeScript interfaces
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
└── .gitignore
```

## Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.11+)
- uv (Python package manager)

### Backend Setup
```bash
cd backend
uv sync                 # Install dependencies
uv run uvicorn app.main:app --reload --port 8000
```

### Frontend Setup
```bash
cd frontend
npm install             # Install dependencies
npm run dev             # Start dev server (http://localhost:5173)
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | List all tasks |
| POST | `/api/tasks` | Create new task |
| GET | `/api/tasks/{id}` | Get single task |
| PATCH | `/api/tasks/{id}` | Update task |
| DELETE | `/api/tasks/{id}` | Delete task |
| POST | `/api/tasks/reorder` | Bulk reorder tasks |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT