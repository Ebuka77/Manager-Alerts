# Manager-Alerts
Manager Alerts dashboard (Django + React) — simplified implementation of alerts filtering 

This is a junior-friendly full-stack project demonstrating a Manager Alerts system. It includes a Django backend (with SQLite seed data) and a React + TypeScript frontend.  
Users can view alerts for employees under a manager, filter by severity or name, toggle between direct and subtree reports, and dismiss alerts.  

The project implements many of the core features requested in the take-home test, with some simplifications.

# Notes before running: 

1. **Backend**: create virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt

2. **Frontend**: install dependencies
npm install
npm run dev

## Features

**Backend**
- Django + Django REST Framework
- `GET /api/alerts?manager_id=<id>&scope=direct|subtree[&severity=&q=]`
- `POST /api/alerts/<id>/dismiss`
- Uses SQLite with seed data (`backend/seed_data.json`)
- Direct and subtree employee reports
- Filtering by severity and employee name
- Simplified subtree traversal (no cycle detection for clarity)

**Frontend**
- React + TypeScript (Vite)
- Table showing alerts: employee name, category, severity, status, created_at
- Scope selector (direct/subtree)
- Severity filter and text search

---

## Design Choices

- **Cycle detection:** The full spec requested cycle-safe traversal. For this junior-friendly implementation, I used a simple subtree expansion without cycle detection to keep the logic readable.
- **Filters:** Supports single-value severity; multi-value comma-separated filters are not implemented to reduce complexity.
- **Idempotency:** The dismiss endpoint updates the alert to `"dismissed"`. Full idempotency is not implemented for simplicity.
- **Sorting:** Alerts are sorted by `created_at` descending. Tie-breaker by `id` is omitted because seed timestamps are unique.
- **Testing:** No full test suite is included to focus on core functionality, but the code is structured for easy addition of tests later.

---

## Technologies

- **Backend:** Python 3.10+, Django, Django REST Framework, SQLite, django-cors-headers  
- **Frontend:** Node.js 18+, React 18, TypeScript, Vite, Axios

---

## How to Run

### Backend

```bash
cd backend
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
# venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver

backend runs by default at http://127.0.0.1:8000.

### Frontend


cd frontend
npm install
npm run dev


The frontend runs by default at http://localhost:5173 and will call the backend automatically.

---

### Next Steps 

- Add proper cycle detection in subtree traversal

- Implement multi-value severity and status filters

- Add idempotency guarantees for the dismiss endpoint

- Add query-string persistence for filters in the UI

- Add automated tests (pytest for backend, Vitest for frontend)

- Enhance UI with severity color chips, responsive design, and accessibility improvements
