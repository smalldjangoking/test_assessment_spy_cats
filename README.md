# 🕵️‍♂️ Python Engineer Test Assessment - the Spy Cat Agency

## Task Statement

Build a CRUD application for the fictional Spy Cat Agency (SCA). The goal is to design a system that demonstrates your expertise in RESTful APIs, database interaction, and third-party service integration. You are expected to complete the assessment within 2 hours.

**SCA needs a management application to streamline their spy operations:**  
- **Cats:** Manage the agency's spy cats.
- **Missions:** Assign missions to cats (each cat can only have one mission at a time).
- **Targets:** Each mission consists of 1-3 targets for spying.
- **Notes:** Cats submit notes on each target, which can be updated until the target is marked complete. After that, notes are frozen.
- **Mission Completion:** When all targets are complete, the mission is marked complete.

**From the agency’s perspective:**
- Add and view new spy cats.
- Create missions and assign available cats.
- Targets are created as part of a mission (no separate target management UI).

---

## 🚀 Quick Start

Follow these steps to get the application up and running locally.

### 1. Clone the Repository

```bash
git clone https://github.com/smalldjangoking/test_assessment_spy_cats.git
cd test_assessment_spy_cats
```

### 2. Install pipenv (if not already installed)

```bash
pip install pipenv
```

### 3. Install Dependencies Using pipenv

```bash
pipenv install
```

### 4. Activate the Virtual Environment

```bash
pipenv shell
```

### 5. Initialize the Database

Before running the project, you need to create the `db_database` file required for the project to work.  
Run the provided script to initialize the database:

```bash
python db_init.py
```

### 6. Run the Server

The project is built with **FastAPI**.

```bash
uvicorn main:app --reload
```


There is a file `insomnia-export.1759061386297.zip` in this repository.  
It contains a set of API requests for the Insomnia client, which can help you quickly test endpoints.  
Just import the file into Insomnia to make manual API testing easier and faster.

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- SQL-like database (SQLite)
- pipenv for environment management
- RESTful API principles

---

## 📦 API Endpoints Overview

### 🐱 Cats (`/cats/`)
- `GET /cats/all` — List all cats  
- `GET /cats/check/name/{cat_name}` — Get cats by name (may return multiple)  
- `GET /cats/check/id/{cat_id}` — Get cat by ID  
- `POST /cats/add` — Create a new cat  
- `DELETE /cats/delete/{cat_id}` — Delete cat by ID  
- `PATCH /cats/update-salary/{cat_id}` — Update cat’s salary  

---

### 🎯 Agency Missions (`/agency/`)
- `POST /agency/mission/create` — Create a new mission (with targets)  
- `DELETE /agency/mission/delete/{mission_id}` — Delete a mission (only if not assigned to a cat)  
- `GET /agency/mission/all` — Get all missions with their targets  
- `GET /agency/mission/id/{mission_id}` — Get a mission by ID (with targets)  
- `PATCH /agency/mission/{mission_id}/change/status` — Mark mission as completed  

---

### 🕵️ Spies (`/spies/`)
- `PATCH /spies/{cat_id}/target/{target_id}` — Update a target’s notes or mark as complete  





