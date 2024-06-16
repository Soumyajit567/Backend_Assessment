# User Service

This is a user management microservice built with FastAPI, SQLAlchemy, and PostgreSQL. It provides endpoints for creating, reading, updating, and deleting user records.

## Table of Contents

- [User Service](#user-service)
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

   DATABASE_URL=postgresql://postgres:<password>@host.docker.internal:5432/user_service_db


`.env.local` (for local development):
   
   DATABASE_URL=postgresql://postgres:<password>@localhost:5432/user_service_db

   Replace `<password>` with your PostgreSQL password.

## Running the Service

### Using Docker

1. **Build the Docker Image:**
    ```sh
    docker build -t user_service .
    ```

2. **Run the Docker Container:**
    ```sh
    docker run -d --name user_service -p 8000:8000 --env-file .env user_service
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
    uvicorn app.main:app --reload
    ```

5. **Access the API:**
    - Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## API Endpoints

- **Create User:**
  - `POST /api/v1/users/`
  - Request body example:
    ```json
    {
      "name": "Bob",
      "mobile_no": "8123456789",
      "email": "bob@example.com",
      "password": "newpassword123"
    }
    ```

- **Read Users:**
  - `GET /api/v1/users/`

- **Read User by ID:**
  - `GET /api/v1/users/{user_id}`

- **Update User:**
  - `PUT /api/v1/users/{user_id}`

- **Delete User:**
  - `DELETE /api/v1/users/{user_id}`

## Project Structure

    user_service/
    ├── app/
    │ ├── init.py
    │ ├── main.py
    │ ├── models.py
    │ ├── schemas.py
    │ ├── crud.py
    │ ├── db.py
    │ └── routers/
    │ └── users.py
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