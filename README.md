#  Book Library API

A FastAPI-based application that allows you to search and catalog books using the [Open Library API](https://openlibrary.org/developers/api).  
Includes a clean HTML UI, REST API, testing, Docker support, GitHub CI, and optional MkDocs documentation.

---

##  Features

-  Search books by title via Open Library
-  Simple UI using Jinja2 templates
-  Dockerized for easy deployment
-  Pytest-based test 
-  Pre-commit hooks
-  GitHub Actions CI workflow
-  MkDocs for project documentation
-  VS Code config + extensions

---

##  Setup Instructions

### 1. Clone and Create Virtual Environment

```bash
git clone https://github.com/SabalM/fastapi-book-library.git
cd fastapi-book-library

python -m venv venv
./venv/Scripts/activate

pip install -r requirements.txt
```

### 2. Create .env file
Add .env file inside root directory
Inside .env add
```bash
OPENLIBRARY_API=https://openlibrary.org
```

### 3. Run with Docker

```bash
docker compose up --build
```

Visit: http://localhost:8000/ui

### 4. Run without Docker

```bash
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/ui

### 5. Open Mkdocs

```bash
mkdocs serve
```