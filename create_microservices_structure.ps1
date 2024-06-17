# Create directories and files for users service
$services = @("users", "discussions", "comments", "likes", "follows")

foreach ($service in $services) {
    mkdir -p "Backend/Microservices/$service/app/routers" -Force
    New-Item -Path "Backend/Microservices/$service/app/__init__.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/main.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/models.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/schemas.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/crud.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/db.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/dependencies.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/routers/__init__.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/app/routers/$service.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/.env" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/requirements.txt" -ItemType File -Force
    mkdir "Backend/Microservices/$service/alembic" -Force
    New-Item -Path "Backend/Microservices/$service/alembic/env.py" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/alembic/README" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/alembic/script.py.mako" -ItemType File -Force
    New-Item -Path "Backend/Microservices/$service/alembic.ini" -ItemType File -Force
    mkdir "Backend/Microservices/$service/alembic/versions" -Force
}

Write-Output "Directories and files created successfully."