from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fake_db = {}

class User(BaseModel):
    id: int
    name: str
    age: int
    city: Optional[str] = None

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI example!"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user = fake_db.get(user_id)
    if user:
        return {"user": user}
    return {"error": "User not found"}

@app.post("/user")
def create_user(user: User):
    if user.id in fake_db:
        return {"error": "User with this ID already exists"}
    fake_db[user.id] = user.dict()
    return {"message": "User created", "user": user}

@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in fake_db:
        fake_db[user_id] = user.dict()
        return {"message": "User updated", "user": user}
    return {"error": "User not found"}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id in fake_db:
        del fake_db[user_id]
        return {"message": f"User with ID {user_id} deleted"}
    return {"error": "User not found"}
