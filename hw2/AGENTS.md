# AGENTS.md - Agent Guidelines for kanban-mini

This file provides guidance for AI agents (like myself) working on the kanban-mini project.

## Project Overview
kanban-mini is a lightweight Kanban board with React/Vite frontend and FastAPI/backend.

## Coding Standards

### Backend (Python)
- Use Python 3.11+ type hints
- Follow PEP 8 style guide
- Use FastAPI dependency injection for services
- Validate all inputs with Pydantic models
- Use async/await for database operations
- Keep business logic in service layer, not in route handlers

### Frontend (React/TypeScript)
- Use functional components with hooks
- Follow TypeScript strict mode
- Use React Query for server state management
- Implement optimistic updates for mutations
- Keep components small and focused
- Use proper error boundaries

## File Organization

### Backend
```
backend/app/
├── api/          # Route definitions
├── models/       # Pydantic models (DTOs)
├── services/     # Business logic
├── db/           # Database setup and models
└── main.py       # App entry point
```

### Frontend
```
frontend/src/
├── components/   # Reusable UI components
├── hooks/        # Custom React hooks
├── services/     # API client functions
├── types/        # TypeScript interfaces
└── App.tsx       # Root component
```

## Development Workflow

1. **Backend Changes**
   - Run tests: `uv run pytest`
   - Type checking: `uv run mypy .`
   - Linting: `uv run ruff check .`

2. **Frontend Changes**
   - Linting: `npm run lint` (if configured)
   - Type checking: `npx tsc --noEmit`

3. **Database Migrations**
   - For schema changes, update models and recreate SQLite DB if needed
   - Consider using Alembic for production migrations

## Common Tasks

### Adding a new API endpoint
1. Define Pydantic models in `backend/app/models/`
2. Add route in `backend/app/api/`
3. Implement business logic in `backend/app/services/`
4. Register router in `backend/app/main.py`

### Adding a new frontend component
1. Create component in `frontend/src/components/`
2. Add any needed hooks in `frontend/src/hooks/`
3. Update types in `frontend/src/types/` if needed
4. Use component in appropriate parent component

## Testing Guidelines

### Backend
- Unit tests for service functions
- Integration tests for API endpoints
- Use pytest and httpx for testing
- Mock external dependencies

### Frontend
- Unit tests for hooks and utilities
- Component tests with React Testing Library
- E2E tests with Cypress or Playwright (future)

## Performance Considerations
- Use React.memo for expensive components
- Implement pagination for large task lists
- Use database indexes for frequent queries
- Enable gzip compression in production
- Use caching strategies with React Query

## Security Considerations
- Validate all inputs on backend
- Use proper CORS configuration
- Implement rate limiting for API endpoints
- Sanitize user-generated content
- Use HTTPS in production

## Debugging
- Backend logs: Check console output from uvicorn
- Frontend logs: Use React DevTools and browser console
- Network requests: Use browser dev tools Network tab
- Database: Inspect SQLite file directly or use DB browser