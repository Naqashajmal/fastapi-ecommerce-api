from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order, OrderItem, Product
from app.schemas import OrderCreate, OrderResponse
from app.oauth2 import get_current_user
from typing import List

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_order = Order(user_id=current_user.id)
    db.add(new_order)
    db.flush()
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(order_item)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Order).filter(Order.user_id == current_user.id).all()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order