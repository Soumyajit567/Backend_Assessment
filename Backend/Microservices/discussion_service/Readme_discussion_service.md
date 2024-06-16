# Discussion Service

This is a discussion management microservice built with FastAPI, SQLAlchemy, and PostgreSQL. It provides endpoints for creating, reading, updating, and deleting discussion records.

## Table of Contents

- [Discussion Service](#discussion-service)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [Environment Variables](#environment-variables)
  - [Running the Service](#running-the-service)
    - [Using Docker](#using-docker)
    - [Running Locally](#running-locally)
  - [API Endpoints](#api-endpoints)
  - [Project Structure](#project-structure)
  - [License](#license)

## Prerequisites

- Python 3.8 or higher
- PostgreSQL 13 or higher
- Docker (optional, for containerized setup)
- Conda (optional, for virtual environment setup)

## Setup

### Environment Variables

Create a `.env` file for Docker and a `.env.local` file for local development. Below is an example of what the contents should look like:

`.env` (for Docker):
     DATABASE_URL=postgresql://postgres:<password>@host.docker.internal:5432/discussion_service_db
      Replace `<password>` with your PostgreSQL password.

`.env.local` (for local development):
     DATABASE_URL=postgresql://postgres:<password>@localhost:5432/discussion_service_db

     Replace `<password>` with your PostgreSQL password.

## Running the Service

### Using Docker

1. **Build the Docker Image:**
    ```sh
    docker build -t discussion_service .
    ```

2. **Run the Docker Container:**
    ```sh
    docker run -d --name discussion_service -p 8000:8000 --env-file .env discussion_service
    ```

3. **Access the API:**
    - Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

### Running Locally

1. **Create a Conda Environment:**
    ```sh
    conda create -n spyne_assessment_env python=3.8
    conda activate spyne_assessment_env
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Environment Variables:**
    Ensure that `.env.local` is properly set up as described in the [Environment Variables](#environment-variables) section.

4. **Run the Application:**
    ```sh
    uvicorn app.main:app --reload --port 8001
    ```

5. **Access the API:**
    - Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## API Endpoints

- **Create Discussion:**
  - `POST /api/v1/discussions/`
  - Request body example:
    ```json
    {
      "title": "My First Discussion",
      "content": "This is the content of the discussion.",
      "user_id": 1
    }
    ```

- **Read Discussions:**
  - `GET /api/v1/discussions/`

- **Read Discussion by ID:**
  - `GET /api/v1/discussions/{discussion_id}`

- **Update Discussion:**
  - `PUT /api/v1/discussions/{discussion_id}`

- **Delete Discussion:**
  - `DELETE /api/v1/discussions/{discussion_id}`

## Project Structure

    discussion_service/
    ├── app/
    │ ├── init.py
    │ ├── main.py
    │ ├── models.py
    │ ├── schemas.py
    │ ├── crud.py
    │ ├── db.py
    │ └── routers/
    │ └── discussions.py
    ├── alembic/
    │ ├── versions/
    │ ├── env.py
    │ ├── script.py.mako
    │ └── README
    ├── Dockerfile
    ├── .env
    ├── .env.local
    ├── requirements.txt
    └── README.md