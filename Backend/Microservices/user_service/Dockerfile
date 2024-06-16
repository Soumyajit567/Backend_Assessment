FROM python:3.8-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000


ENV DATABASE_URL=postgresql://postgres:yourpassword@host.docker.internal:5432/user_service_db


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
