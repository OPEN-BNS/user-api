from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from password_gen import generateSecurePassword
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app=FastAPI()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

origins = [
    'http://127.0.0.1:3000',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username:str
    name:str
    email:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserBase, db: db_dependency):
    _passwd = generateSecurePassword()
    db_user = models.User(username=user_data.username, password=_passwd, name=user_data.name, email=user_data.email)
    db.add(db_user)
    db.commit()

@app.get("/users", status_code=status.HTTP_200_OK)
async def all_users(db:db_dependency):
    users = db.query(models.User).all()
    if users is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="No users found!")
    return users