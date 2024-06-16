# # Use the official Python image from the Docker Hub
# FROM python:3.8-slim

# # Install the dependencies required for building psycopg2
# RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file into the image
# COPY requirements.txt .

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code into the image
# COPY . .

# # Set environment variables for Alembic
# ENV DATABASE_URL=postgresql://postgres:Soumyajit123#@localhost:5432/discussion_service_db

# # Command to run Alembic migrations and start the application
# CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8001"]

# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Install the dependencies required for building psycopg2
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Set environment variables for Alembic
ENV DATABASE_URL=postgresql://postgres:Soumyajit123#@localhost:5432/discussion_service_db

# Command to run Alembic migrations and start the application
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8001"]



