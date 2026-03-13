from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import products
from app.routers import products, auth, orders


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce API",
    description="A full e-commerce backend API",
    version="1.0.0"
)

app.include_router(products.router)
app.include_router(auth.router)
app.include_router(orders.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "E-commerce API is running"}