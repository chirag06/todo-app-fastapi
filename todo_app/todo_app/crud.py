from sqlalchemy.orm import Session

from . import schemas
from .models import Todo

def get_todo(db: Session, item_id: int):
    return db.query(Todo).filter(Todo.id == item_id).first()


def get_todo_by_status(db: Session, item_status: bool):
    return db.query(Todo).filter(Todo.status == item_status).all()

def get_all_todo(db: Session):
    return db.query(Todo).all()

def create_todo(db: Session, item: schemas.Create_Item):
    todo = Todo(**item.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, item: schemas.Item):
    todo = db.query(Todo).filter(Todo.id == item.id).first()
    if todo:
        todo.title = item.title
        todo.status = item.status
        todo.description = item.description
        db.commit()
        db.refresh(todo)
    return todo

def delete_todo(db: Session, item_id: int):
    todo = db.query(Todo).filter(Todo.id == item_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo
