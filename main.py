from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

def get_users():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

@app.get("/users/")
def read_users():
    users = get_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
