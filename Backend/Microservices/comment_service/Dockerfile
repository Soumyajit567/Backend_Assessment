# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install the dependencies required for building psycopg2
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV DATABASE_URL=postgresql://postgres:password@db:5432/comment_service_db
ENV DOCKER_ENV=docker

# Expose the port the app runs on
EXPOSE 8002

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
