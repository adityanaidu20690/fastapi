from sqlalchemy.orm import Session
from model.item import Item
from schema.item_schema import ItemCreate

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
