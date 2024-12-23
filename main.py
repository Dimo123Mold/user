from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str



users = [User(id= 1, username= "egor1", email="moldawan1@gmail.com"),
         User(id= 2, username= "egor2", email="moldawan2@gmail.com"),
         User(id= 3, username= "egor3", email="moldawan3@gmail.com")]


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/users", response_model=List[User])
def list_users():
    return users


def create_user(user: User):
    if any(existing_user.email == user.email for existing_user in users):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    users.append(user)
    return user