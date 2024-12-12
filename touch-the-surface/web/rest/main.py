from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = ""
    completed: bool = False

todos = []

@app.get("/todos", response_model=List[Todo])
async def read_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo.dict())
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    for t in todos:
        if t["id"] == todo_id:
            t.update(todo.dict())
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return
    raise HTTPException(status_code=404, detail="Todo not found")