import sys
import os

current_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, current_path)

print("PYTHONPATH:", sys.path)


try:
    from app.routers.likes import router as likes_router
    print("Import successful!")
except ImportError as e:
    print("ImportError:", e)
