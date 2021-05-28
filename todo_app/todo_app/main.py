import uvicorn
from sqlalchemy.orm import Session

from . import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/items/")
def create_item(item: schemas.Create_Item, db: Session = Depends(get_db)):
    return crud.create_todo(db = db, item = item)

@app.get("/all/")
def read_list(db: Session = Depends(get_db)):
    return crud.get_all_todo(db)


@app.get("/item/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db = db, item_id = item_id)
    if todo:
        return todo
    raise HTTPException(status_code=400, detail="No item found with the id")


@app.get("/items/{item_status}")
def read_item(item_status: bool, db: Session = Depends(get_db)):
    return crud.get_todo_by_status(db = db, item_status = item_status)


@app.put("/items")
def update_item(item: schemas.Item,  db: Session = Depends(get_db)):
    todo = crud.update_todo(db = db, item=item)
    if todo:
        return todo
    return {"Error": f"Todo with this id {item.task_id} was not found"}

@app.delete("/items/{task_id}")
def delete_item(task_id: int, db: Session = Depends(get_db)):
    if crud.delete_todo(db = db, item_id=task_id):
        return {"Success": f"Todo with id {task_id} deleted"}
    raise HTTPException(status_code=400, detail=f"Todo with this id {task_id} was not found")

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1', port=8000)
