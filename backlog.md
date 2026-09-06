# House Chore Manager - Django Backlog

## Project Overview
A Django-based household chore management system with admin interface, member tracking, room organization, chore scheduling, and assignment history.

**Current State**: ✅ Project scaffolded with models, admin, migrations, superuser, and dev server running.

---

## Backlog: Prioritized Task List

### Phase 1: Core Functionality (MVP)

| # | Task | Description | Effort |
|---|------|-------------|--------|
| 1 | **Chore List View** | Create `ChoreListView` showing all chores with filters (frequency, assignee, status, room) | M |
| 2 | **Chore Detail View** | Detail page with assignment history, completion toggle, and edit links | M |
| 3 | **Chore Create/Edit Forms** | ModelForms for Chore with Room/Member dropdowns, frequency choices, date picker | M |
| 4 | **Member Dashboard** | Per-member view showing assigned chores, due dates, completion stats | M |
| 5 | **Room Management UI** | CRUD views for Rooms with inline chore listing | S |
| 6 | **Assignment Workflow** | "Assign Chore" action: creates ChoreAssignment, sends notification (console email) | M |

### Phase 2: User Experience

| # | Task | Description | Effort |
|---|------|-------------|--------|
| 7 | **Member Login** | Custom auth views for HouseholdMember (email-based, no Django User) | M |
| 8 | **Homepage/Dashboard** | Landing page with quick stats: overdue chores, upcoming, completion rate | S |
| 9 | **Calendar View** | Monthly calendar showing chore due dates (HTML table or JS library) | L |
| 10 | **Mobile-Responsive Templates** | Bootstrap 5 / Tailwind CSS base templates with navigation | M |
| 11 | **Chore Completion UX** | One-click "Mark Complete" from list view (HTMX or AJAX) | M |
| 12 | **Notifications** | Daily email summary of due/overdue chores (management command + cron) | M |

### Phase 3: Advanced Features

| # | Task | Description | Effort |
|---|------|-------------|--------|
| 13 | **Recurring Chore Engine** | Auto-create next occurrence when recurring chore is completed | L |
| 14 | **Chore Templates** | Pre-defined chore sets (e.g., "Weekly Kitchen") for quick creation | M |
| 15 | **Points/Rewards System** | Points per chore, leaderboard, redemption for rewards | M |
| 16 | **Conflict Resolution** | Detect overlapping assignments, suggest alternatives | S |
| 17 | **Reporting** | PDF/CSV export of chore history, member workload, room cleanliness | M |
| 18 | **API Endpoints** | DRF serializers for mobile app integration (future) | L |

### Phase 4: Polish & Production

| # | Task | Description | Effort |
|---|------|-------------|--------|
| 19 | **Test Coverage** | Unit tests for models, views, forms; integration tests for workflows | M |
| 20 | **Admin Enhancements** | Custom admin actions (bulk assign, mark overdue), inline editing | S |
| 21 | **Settings Management** | Per-household settings: timezone, notification prefs, chore defaults | S |
| 22 | **Deployment Config** | Dockerfile, docker-compose, production settings, static files | M |
| 23 | **Documentation** | README, API docs, contributor guide | S |

---

## Technical Debt / Refactoring

| # | Item | Notes |
|---|------|-------|
| T1 | **Abstract Base Models** | Extract `TimestampedModel` (created_at/updated_at) |
| T2 | **Custom Managers** | `Chore.objects.due_today()`, `Member.objects.active()` |
| T3 | **Signals** | Auto-create assignment on chore save; update `completed` on assignment completion |
| T4 | **Validators** | Prevent past due_dates, ensure room/household consistency |
| T5 | **Pagination** | Add to all list views (25/page default) |

---

## Suggested Sprint Plan (2-week sprints)

| Sprint | Focus | Deliverables |
|--------|-------|--------------|
| **Sprint 1** | Core Views & Forms | Tasks 1-6: Full CRUD for chores/members/rooms via web UI |
| **Sprint 2** | Auth & Dashboard | Tasks 7-10: Member login, homepage, responsive templates |
| **Sprint 3** | Smart Features | Tasks 11-13: Quick actions, notifications, recurring engine |
| **Sprint 4** | Polish | Tasks 14-19: Templates, rewards, tests, admin enhancements |
| **Sprint 5** | Production Ready | Tasks 20-23: Settings, deploy, docs |

---

## Dependencies & Risks

- **Recurring engine (Task 13)** depends on Task 11 (completion workflow)
- **Member login (Task 7)** requires decision: custom auth vs. Django User with profile
- **Calendar (Task 9)** may need JS library (FullCalendar) → adds build step
- **Email notifications** need real SMTP config for production (currently console backend)

---

## Definition of Done (per task)
- [ ] Code implemented with type hints
- [ ] Unit tests passing (`python manage.py test`)
- [ ] Manual QA on dev server
- [ ] No new lint errors (`ruff check .`)
- [ ] Template responsive on mobile
- [ ] Admin accessible for staff users

---

## Next Steps for You

1. **Confirm priority order** - Any tasks to add/remove/reorder?
2. **Choose auth approach** - Custom `HouseholdMember` login or extend Django `User`?
3. **Frontend preference** - Server-rendered templates + HTMX, or separate SPA (React/Vue)?
4. **Timeline** - Target date for MVP?

Once you approve, I can begin implementation.

---

**Ready to proceed with Phase 1 (Tasks 1-6) when you give the go-ahead.Task #1: Chore List View - COMPLETED
