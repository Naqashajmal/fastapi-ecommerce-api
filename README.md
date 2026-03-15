# FastAPI E-Commerce API

A full-featured e-commerce REST API built with FastAPI and Python, deployed on Railway with PostgreSQL.

## Live API
🚀 https://vivacious-flow-production.up.railway.app/docs

## Features
- JWT Authentication (register/login)
- Products CRUD with search
- Orders system
- PostgreSQL database
- Input validation with Pydantic
- Automated tests with pytest

## Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT (python-jose)
- pytest

## Installation

git clone https://github.com/Naqashajmal/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
pip install -r requirements.txt

Create .env file:
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./ecommerce.db

Run:
fastapi dev main.py

## API Endpoints

### Auth
- POST /auth/register
- POST /auth/login

### Products
- GET /products
- POST /products (auth required)
- GET /products/{id}
- PUT /products/{id} (auth required)
- DELETE /products/{id} (auth required)

### Orders
- POST /orders (auth required)
- GET /orders (auth required)
- GET /orders/{id} (auth required)

## Testing
pytest tests/ -v
