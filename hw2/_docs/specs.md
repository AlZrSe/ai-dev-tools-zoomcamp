# kanban-mini - Specification

## Overview

A lightweight Kanban board application with a Node.js frontend and Python (FastAPI) backend. MVP includes three fixed columns (Todo, In Progress, Done) with drag-and-drop task management and persistence via SQLite.

---

## Tech Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Frontend | React + TypeScript + Vite | React 18, TS 5.x |
| Backend | Python FastAPI | Python 3.11+, FastAPI 0.100+ |
| Communication | REST API + WebSocket (optional) | JSON over HTTP |
| Persistence | SQLite (file-based) | SQLite3 |
| Drag & Drop | @dnd-kit/core | Latest |
| Package Manager (Backend) | **uv** | Latest |

---

## Project Structure

```
hw2/
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── hooks/          # Custom hooks
│   │   ├── services/       # API client
│   │   ├── types/          # TypeScript interfaces
│   │   └── App.tsx
│   ├── package.json        # name: "kanban-mini"
│   └── vite.config.ts
├── backend/
│   ├── app/
│   │   ├── api/            # FastAPI routes
│   │   ├── models/         # Pydantic models
│   │   ├── services/       # Business logic
│   │   ├── db/             # Database setup
│   │   └── main.py
│   ├── pyproject.toml      # name = "kanban-mini"
│   ├── uv.lock
│   └── requirements.txt  # Optional: generated from pyproject.toml
└── SPEC.md
```

---

## Data Models

### Task (Backend - Pydantic)
```python
class TaskBase(BaseModel):
    title: str
    description: str = ""
    column: Literal["todo", "in_progress", "done"] = "todo"
    order: int = 0

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    column: Optional[Literal["todo", "in_progress", "done"]] = None
    order: Optional[int] = None

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
```

### Task (Frontend - TypeScript)
```typescript
type ColumnId = 'todo' | 'in_progress' | 'done';

interface Task {
  id: number;
  title: string;
  description: string;
  column: ColumnId;
  order: number;
  createdAt: string;  // ISO 8601
  updatedAt: string;
}
```

---

## API Endpoints

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | List all tasks (ordered by column + order) |
| POST | `/api/tasks` | Create new task |
| GET | `/api/tasks/{id}` | Get single task |
| PATCH | `/api/tasks/{id}` | Update task (partial) |
| DELETE | `/api/tasks/{id}` | Delete task |
| POST | `/api/tasks/reorder` | Bulk reorder (column + order changes) |

### Reorder Request Body
```json
{
  "tasks": [
    { "id": 1, "column": "in_progress", "order": 0 },
    { "id": 2, "column": "todo", "order": 1 }
  ]
}
```

---

## Frontend Components

### Component Hierarchy
```
App
├── Board
│   ├── Column (x3: Todo, In Progress, Done)
│   │   ├── ColumnHeader
│   │   └── TaskList (Droppable)
│   │       └── TaskCard (Draggable) × N
│   └── AddTaskModal
```

### Key Components

**Board.tsx** - Main container, manages columns layout
**Column.tsx** - Renders single column with header + task list
**TaskCard.tsx** - Draggable task card, shows title + truncated description
**AddTaskModal.tsx** - Form for creating new tasks

---

## User Stories (MVP)

| ID | Story | Acceptance Criteria |
|----|-------|---------------------|
| US-1 | As a user, I want to see three columns (Todo, In Progress, Done) | Three columns render side-by-side with headers |
| US-2 | As a user, I want to add a task to any column | Click "+" in column → modal opens → submit creates task in that column |
| US-3 | As a user, I want to drag tasks between columns | Drag task → drop in another column → API called → UI updates |
| US-4 | As a user, I want to reorder tasks within a column | Drag task up/down → drop → order persisted |
| US-5 | As a user, I want to edit a task | Click task → modal with title/description → save updates |
| US-6 | As a user, I want to delete a task | Task menu → delete → confirmation → task removed |
| US-7 | As a user, I want data to persist after refresh | Reload page → all tasks restored in correct columns/orders |

---

## Database Schema (SQLite)

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT DEFAULT '',
    column TEXT NOT NULL CHECK (column IN ('todo', 'in_progress', 'done')),
    "order" INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tasks_column_order ON tasks(column, "order");
```

---

## Backend Implementation Notes (with uv)

### Setup with uv
```bash
cd backend
uv init  # Creates pyproject.toml
uv add fastapi uvicorn sqlalchemy aiosqlite pydantic pydantic-settings python-multipart
uv add --dev pytest pytest-asyncio httpx ruff
uv run uvicorn app.main:app --reload --port 8000
```

### pyproject.toml (minimal)
```toml
[project]
name = "kanban-mini"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.100",
    "uvicorn>=0.23",
    "sqlalchemy>=2.0",
    "aiosqlite>=0.19",
    "pydantic>=2.0",
    "pydantic-settings>=2.0",
    "python-multipart>=0.0.6",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.4",
    "pytest-asyncio>=0.21",
    "httpx>=0.24",
    "ruff>=0.1",
]
```

### Benefits of uv
- **Faster** installs (Rust-based, parallel downloads)
- **Single tool** replaces pip + venv + pip-tools
- **Lockfile** (`uv.lock`) for reproducible builds
- **Virtual env** managed automatically (`.venv/`)

### Implementation Points
- Use SQLAlchemy 2.0 (async) or raw aiosqlite
- Enable CORS for frontend origin (http://localhost:5173)
- Validate column values server-side
- Return 404 for non-existent task IDs
- Bulk reorder in single transaction

---

## Frontend Implementation Notes

- Use `@dnd-kit/core` + `@dnd-kit/sortable` for drag-and-drop
- Optimistic UI updates with rollback on API failure
- React Query (TanStack Query) for server state management
- Debounced auto-save for task edits (optional)

---

## Development Setup

```bash
# Backend
cd backend
uv init  # if not already done
uv sync  # installs from pyproject.toml
uv run uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend
# Ensure package.json has name: "kanban-mini"
npm install
npm run dev  # Runs on http://localhost:5173
```

---

## Future Enhancements (Post-MVP)

- Multiple boards
- Task assignees, labels, due dates
- Column customization (add/remove/rename)
- WebSocket for real-time collaboration
- Dark mode
- Keyboard accessibility improvements
- Export/import board data
- Docker containerization
- GitHub Actions CI/CD