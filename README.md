# SkillSphere Backend

SkillSphere is a student development platform aimed at helping students identify their strengths, weaknesses, and career paths.

## Current Features

- FastAPI backend setup
- Student endpoints                     ## initial stage
- Query parameter filtering
- Path parameter handling

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Run Locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

Visit:

http://127.0.0.1:8000/docs