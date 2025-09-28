# 🕵️‍♂️ Python Engineer Test Assessment - the Spy Cat Agency

## Task Statement

<details>
  <summary>📌 click to open task text</summary>

# Python engineer test assessment - the Spy Cat Agency

### Overview

This task involves building a CRUD application. The goal is to create a system that showcases your understanding in building RESTful APIs, interacting with SQL-like databases, and integrating third-party services. The test assessment is expected to be done within 2 hours.

### Requirements

Spy Cat Agency (SCA) asked you to create a management application, so that it simplifies their spying work processes. SCA needs a system to manage their cats, missions they undertake, and targets they are assigned to.

From cats perspective, a mission consists of spying on targets and collecting data. One cat can only have one mission at a time, and a mission assumes a range of targets (minimum: 1, maximum: 3). While spying, cats should be able to share the collected data into the system by writing notes on a specific target. Cats will be updating their notes from time to time and eventually mark the target as complete. If the target is complete, notes should be frozen, i.e. cats should not be able to update them in any way. After completing all of the targets, the mission is marked as completed.

From the agency perspective, they regularly hire new spy cats and so should be able to add them to and visualize in the system. SCA should be able to create new missions and later assign them to cats that are available. Targets are created in place along with a mission, meaning that there will be no page to see/create all/individual targets.

### **Backend Requirements:**

</details>

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







