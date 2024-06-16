# Comment Service

The Comment Service is a microservice that handles comments related to discussions. It interacts with the User Service and Discussion Service to manage and associate comments with users and discussions.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Service](#running-the-service)
- [API Endpoints](#api-endpoints)
  - [Create Comment](#create-comment)
  - [Get Comments](#get-comments)
  - [Get Comment by ID](#get-comment-by-id)
  - [Update Comment](#update-comment)
  - [Delete Comment](#delete-comment)
- [Database Migrations](#database-migrations)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)

## Getting Started

These instructions will guide you to set up and run the Comment Service on your local machine for development and testing purposes.

## Prerequisites

- Python 3.8+
- PostgreSQL
- FastAPI
- Docker (for containerized setup)

## Installation

1. Clone the repository:
   ```bash
    git clone <repository_url>
    cd comment_service
    Create a virtual environment and activate it:


    python -m venv venv
    source `venv\Scripts\activate`

2. Install the dependencies:


    pip install -r requirements.txt

    Set up environment variables:

    Create a .env file in the project root and add the following variables:

    ```
    DATABASE_URL=postgresql://<username>:<password>@localhost:5432/comment_service_db
    ````
  

    Apply the database migrations:
    
    ```
    alembic upgrade head
    ```

    Start the FastAPI server:

    ```
    uvicorn app.main:app --reload --port 8002
    ```


## Database Migrations
To manage database migrations, Alembic is used.

1. Create a new migration:

    ```
    alembic revision --autogenerate -m "Migration message"
    ```

## Apply migrations:


2. alembic upgrade head

    Running Tests
    To run tests, use the following command:

    pytest

## Docker Setup

    To build and run the service using Docker, follow these steps:

        Build the Docker image:

        ```        
        docker build -t comment_service .
        ```

        Run the Docker container:

        ```
        docker run -d -p 8002:8002 --name comment_service --env-file .env comment_service
        ```

        This will start the Comment Service on port 8002.