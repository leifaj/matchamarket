# MatchaMarket Development Setup

This document provides step-by-step instructions for setting up the development environment for **MatchaMarket**, including installing dependencies, running services with Docker Compose, and configuring your IDE.


## 1. Prerequisites

- Docker Desktop
- Node.js & npm (for frontend development)


## 2. Clone the repository

```bash
git clone <repository-url>
cd matchamarket
```


## 3. Install backend dependencies

```bash
cd backend
python -m venv .venv               # Create virtual environment
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate           # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Install frontend dependencies

```bash
cd frontend
npm install
```


## 5. Start all services

From the root of the project:

```bash
docker compose up --build
```

## How To: Reset the Database
From the root of the project inside the virtual environment:

Open a shell in the db container. This logs you into the psql interactive console inside the container.
```bash
docker compose exec db psql -U db_user -d matchamarket
```

Drop and crecreate the public schema.
```bash
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```

Exit psql.
```bash
\q
```
## How To: Seed the Database
Make sure the services are started. In the root of the project:

```bash
docker compose exec backend python -m app.db.seed
```

