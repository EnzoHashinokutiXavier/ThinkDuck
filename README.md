# 🦆 ThinkDuck — Documentation

## Overview

**ThinkDuck** is a web application inspired by the *rubber duck debugging* technique. It helps developers organize their thoughts, document debugging sessions, and build a structured history of problems and solutions.

Instead of relying on informal notes or memory, ThinkDuck provides a system where developers can track their reasoning process step by step, making problem-solving more efficient and reusable over time.

---

## Objectives

- Help developers structure their thinking
- Record the full debugging process (not just the solution)
- Allow retrieval of past problems and solutions
- Improve learning through reflection
- Create a personal knowledge base

---

## MVP

### Authentication
- User registration
- Login and logout
- Session management

---

### Projects
- Create new projects
- View project list
- Access a specific project

---

### Debug Sessions
- Create sessions inside projects
- Each session represents a problem or investigation

Each session contains:
- Title
- Status (open / resolved)
- Creation date

---

### Structured Notes

Each session is divided into:

- **Problem** — description of the issue  
- **Hypotheses** — possible causes  
- **Tests** — attempts made  
- **Solution** — final resolution  

---

### Search
- Search sessions by keywords
- Quickly retrieve past solutions

---

## Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, **Jinja 2 (Template Engine)**
- **Database:** SQLite
- **Authentication:** Flask sessions

---

## Application Flow

- User registers or logs in
- User creates a project
- Inside a project:
- Creates a debug session
- Inside a session:
- Writes structured notes
- User can revisit sessions anytime

---

## Concept Behind the App

ThinkDuck is based on the idea that:

    Explaining a problem is often enough to solve it.

By structuring this explanation into a digital format, the application transforms thinking into:

- organized data
- reusable knowledge
- a long-term learning resource

---

## Design Choices & Justifications

### Technology Stack Selection

**Flask & SQLite** were chosen as the primary technologies for ThinkDuck's development for the following reasons:

#### Flask (Backend Framework)
Flask was selected as the web framework because it aligns with the practical knowledge gained during CS50's 2025 curriculum. As a lightweight and flexible microframework, Flask provides an excellent balance between simplicity and functionality for building this application. It allowed me to:
- Implement authentication and session management efficiently
- Structure routes logically using blueprints
- Focus on core business logic without unnecessary overhead
- Leverage the skills directly learned in the course

#### SQLite (Database)
SQLite was chosen for data persistence because:
- It was introduced in CS50's 2025 course, making it the natural choice for this project
- As a file-based relational database, it requires minimal setup and no external server
- It provides robust support for structured data relationships (users, projects, sessions, entries)
- It's ideal for a personal productivity application where concurrent access isn't a primary concern
- It simplifies deployment by eliminating database infrastructure dependencies

### Architectural Decisions

**Modular Structure**: The codebase is organized into separate modules (models, routes, utils) to promote maintainability and follow the MVC pattern. This separation allows for easier testing and future extensions.

**Session-Based Authentication**: Flask's built-in session management was selected over JWT tokens because it's simpler to implement and sufficient for this application's single-user-per-session use case.

#### Jinja 2 (Template Engine)

Jinja 2 was selected as the template engine because:
- It's the standard template engine for Flask applications
- It was taught in CS50's 2025 curriculum, providing consistency with course materials
- It provides a clean separation between backend logic and frontend presentation
- It supports template inheritance and reusability through `{% extends %}` and `{% include %}`
- It includes built-in security features like automatic HTML escaping to prevent XSS attacks
- It offers powerful features like filters (`|upper`, `|length`, etc.) and control structures (`if`, `for`, `while`)

**Usage pattern in ThinkDuck:**
- All templates extend from `layout.html` (base template) for consistent UI structure
- Dynamic data is passed from Flask routes using `render_template()`
- Variables are safely rendered in HTML using `{{ variable }}` syntax
- URLs are generated dynamically using `{{ url_for('route_name') }}` instead of hardcoded paths

### Trade-offs Made

While other frameworks (Django, FastAPI) or databases (PostgreSQL, MongoDB) might offer additional features, the decision to use Flask, SQLite, and Jinja 2 prioritizes:
- **Learning consistency**: Using technologies learned in the course
- **Simplicity over features**: Meeting project requirements without unnecessary complexity
- **Rapid development**: Getting a functional MVP without extensive setup
- **Security**: Built-in protection against common vulnerabilities (XSS through automatic escaping)

---

## Project Structure

```bash
thinkduck/
│
├── app.py                  # Main Flask application
├── config.py               # App configurations (secretkey, DB path)
├── requirements.txt        # Dependencies
│
├── static/
│   ├── css/
│   │   └── styles.css      # Main stylesheet
│   ├── js/
│   │   └── script.js       # Optional JS
│   └── images/
│       └── duck.png        # App assets
│
├── templates/
│   ├── layout.html         # Base template
│   ├── index.html          # Home page
│   ├── login.html
│   ├── register.html
│   │
│   ├── projects/
│   │   ├── projects.html   # List projects
│   │   └── create.html     # Create project
│   │
│   ├── sessions/
│   │   ├── sessions.html   # List sessions
│   │   ├── create.html     # Create session
│   │   └── view.html       # View/edit session
│
├── models/
│   ├── user.py
│   ├── project.py
│   ├── session.py
│   └── entry.py
│
├── routes/
│   ├── auth.py             # Login/register routes
│   ├── projects.py         # Project routes
│   └── sessions.py         # Session routes
│
├── database/
│   ├── schema.sql          # DB structure
│   └── database.db         # SQLite DB
│
└── utils/
    ├── helpers.py          # Utility functions
    └── decorators.py       # Login required, etc.
```

---

## Database Schema

```bash
users
- id (PRIMARY KEY)
- username (UNIQUE)
- password_hash

projects
- id (PRIMARY KEY)
- user_id (FOREIGN KEY)
- name

sessions
- id (PRIMARY KEY)
- project_id (FOREIGN KEY)
- title
- status
- created_at

entries
- id (PRIMARY KEY)
- session_id (FOREIGN KEY)
- type (problem, hypothesis, test, solution)
- content
```
