# Task Manager API

A RESTful API for managing tasks, built with Python, Flask, and PostgreSQL. Supports CRUD operations and can be deployed with Docker.

## Features

- Create, Read, Update, Delete tasks
- PostgreSQL as database
- Configurable using `config.py`
- Dockerized for easy deployment
- Nginx reverse proxy support

## Project Structure

app/
├── app.py              # Main Flask application
├── config.py           # App configuration
├── models.py           # Database models
├── __init__.py         # App initialization
├── instance/           # Instance folder for environment-specific settings
├── nginx.conf          # Nginx configuration
├── Dockerfile          # Dockerfile for backend service
├── docker-compose.yaml # Docker Compose file
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── __pycache__/        # Compiled Python files

## Installation

### Clone the repository
git clone <your-repo-url>
cd todoApi/app

### Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run the API locally
python app.py
The API will run on `http://localhost:5000`.

## Docker Setup

### Build Docker image
docker build -t task-manager-api .

### Run with Docker Compose
docker compose up -d --build

### Accessing
- http://flaskapp.work.gd/tasks
- API: `http://localhost:5000`
- Nginx (if configured): `http://localhost`

## Environment Variables

Add any required variables in `.env` file or `config.py`:
- DB_USER
- DB_PASS
- DB_NAME
- DB_HOST

## API Endpoints

| Method | Endpoint        | Description          |
|--------|----------------|--------------------|
| GET    | /tasks         | Get all tasks       |
| GET    | /tasks/<id>    | Get task by ID      |
| POST   | /tasks         | Create a new task   |
| PUT    | /tasks/<id>    | Update a task       |
| DELETE | /tasks/<id>    | Delete a task       |

1. Get all tasks (Read)
curl -X GET http://flaskapp.work.gd/tasks

2. Get a specific task by ID (Read)
curl -X GET http://flaskapp.work.gd/tasks/1

3. Create a new task (Create)
curl -X POST http://flaskapp.work.gd/tasks \
-H "Content-Type: application/json" \
-d '{
  "title": "New Task",
  "description": "This is a test task"
}'

4. Update a task by ID (Update)
curl -X PUT http://flaskapp.work.gd/tasks/1 \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Task",
  "description": "Updated description"
}'

5. Delete a task by ID (Delete)
curl -X DELETE http://flaskapp.work.gd/tasks/1

✅ Tips:

- Replace 1 with the actual task ID.
- Replace localhost:5000 with your deployed domain, e.g., flaskapp.work.gd.
- Use -v with curl to see detailed request and response info:
  curl -v -X GET http://flaskapp.work.gd/tasks

