##  Setup Instructions

###  1. Clone and Create Virtual Environment

```bash
git clone https://github.com/SabalM/fastapi-book-library.git
cd fastapi-book-library

python -m venv venv
./venv/Scripts/activate

pip install -r requirements.txt
```

### 2. Run with Docker

```bash
docker-compose up --build
```

Visit: http://localhost:8000/ui

### 3. Run without Docker

```bash
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/ui