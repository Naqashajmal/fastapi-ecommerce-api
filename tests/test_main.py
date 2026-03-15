import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from main import app

# Test database separate from real database
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Replace real database with test database
app.dependency_overrides[get_db] = override_get_db

# Create test tables
Base.metadata.create_all(bind=engine)

# Test client — makes requests to your API without running a server
client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "E-commerce API is running"}


def test_register_user():
    response = client.post("/auth/register", json={
        "email": "test@gmail.com",
        "password": "123456"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@gmail.com"
    assert "password" not in response.json()


def test_login_user():
    response = client.post("/auth/login", data={
        "username": "test@gmail.com",
        "password": "123456"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_create_product():
    # login first to get token
    login = client.post("/auth/login", data={
        "username": "test@gmail.com",
        "password": "123456"
    })
    token = login.json()["access_token"]

    response = client.post("/products/", 
        json={"name": "Laptop", "price": 999.99, "description": "Gaming laptop"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["price"] == 999.99


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product_not_found():
    response = client.get("/products/999")
    assert response.status_code == 404


def test_create_order():
    login = client.post("/auth/login", data={
        "username": "test@gmail.com",
        "password": "123456"
    })
    token = login.json()["access_token"]

    response = client.post("/orders/",
        json={"items": [{"product_id": 1, "quantity": 2}]},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "pending"
    assert len(response.json()["items"]) == 1