# FastAPI E-Commerce API

## Live API
https://vivacious-flow-production.up.railway.app/docs

A full-featured e-commerce REST API built with FastAPI and Python.

## Features
- JWT Authentication (register/login)
- Products CRUD
- Orders system
- SQLite database
- Input validation with Pydantic

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)

## Installation
```bash
git clone https://github.com/Naqashajmal/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
pip install -r requirements.txt
fastapi dev main.py
```

## API Endpoints

### Auth
- POST /auth/register
- POST /auth/login

### Products
- GET /products
- POST /products
- GET /products/{id}
- PUT /products/{id}
- DELETE /products/{id}

### Orders
- POST /orders
- GET /orders
- GET /orders/{id}
