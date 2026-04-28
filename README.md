# 🎓 Student Service Desk & Registrar
 
A command-line Python application for managing student records and service tickets at a registrar's office.
 
---
 
## Features
 
- **Student Management** — Add, update, delete, and search students by ID or name
- **Grade Tracking** — Store midterm and final grades; auto-calculate weighted term grades (40% midterm / 60% final)
- **Service Tickets** — Create, list, and resolve support tickets linked to students
- **Class Reports** — View enrollment size, class average, and top-performing student
- **Input Validation** — All inputs are validated with descriptive error messages
---
 
## Project Structure
 
```
project/
├── main.py              # Entry point — launches the interactive menu
├── src/
│   ├── __init__.py
│   ├── app.py           # Core App class with all business logic
│   ├── models.py        # Student, Ticket, and TicketStatus data models
│   ├── validation.py    # Validator class and ValidationError
│   └── reports.py       # Class report generation
└── tests/
    ├── test_students.py  # Unit tests for student registry
    └── test_tickets.py   # Unit tests for ticket system
```
 
---
 
## Getting Started
 
### Requirements
 
- Python 3.10+
- No third-party dependencies
### Run the Application
 
```bash
python main.py
```
 
### Run the Tests
 
```bash
python -m pytest tests/
# or with unittest directly:
python -m unittest discover
```
 
---
 
## Usage
 
When launched, you'll see an interactive menu:
 
```
==== Student Service Desk & Registrary ====
1) Add student
2) Update student
3) Delete student
4) Find student by ID
5) Search by name
6) Print class report
7) Create service ticket
8) List tickets (filter by status)
9) Resolve ticket
0) Exit
```
 
### Student Fields
 
| Field    | Type  | Constraints           |
|----------|-------|-----------------------|
| ID       | int   | Must be unique        |
| Name     | str   | Cannot be empty       |
| Phone    | str   | Digits only           |
| Midterm  | float | 0–100                 |
| Final    | float | 0–100                 |
 
**Term Grade Formula:** `(midterm × 0.40) + (final × 0.60)`
 
### Ticket Workflow
 
1. **Create** a ticket linked to an existing student ID
2. **List** tickets filtered by `OPEN`, `RESOLVED`, or `ALL`
3. **Resolve** a ticket by ID with a resolution note
---
 
## Data Models
 
### `Student`
```python
Student(student_id, name, phone, midterm, final)
student.term_grade()  # → weighted float
```
 
### `Ticket`
```python
Ticket(ticket_id, student_id, category, description)
ticket.resolve(note)  # sets status to RESOLVED
```
 
### `TicketStatus` (Enum)
- `OPEN`
- `RESOLVED`
---
 
## Validation Rules
 
| Input  | Rule                                   |
|--------|----------------------------------------|
| ID     | Must be a valid integer                |
| Name   | Non-empty; auto-formatted to Title Case |
| Phone  | Digits only (dashes/spaces stripped)   |
| Grade  | Numeric; must be between 0 and 100     |
 
Validation failures raise `ValidationError` with a descriptive message.
 
---
 
## Known Issues & Planned Improvements
 
- [ ] Data is in-memory only — not persisted between sessions (SQLite or JSON storage planned)
- [ ] Tests expect a refactored `App` API (direct arguments instead of `input()` prompts)
- [ ] `StudentNotFoundError` referenced in `test_tickets.py` is not yet implemented in `validation.py`
- [ ] `app.students` dict referenced in tests differs from current `app.s` attribute name
- [ ] Ticket ID is not returned by `create_service_ticket()` — needed for test assertions
---
 
## License
 
MIT — free to use and modify.