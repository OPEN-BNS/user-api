from sqlalchemy import Column, Integer, String, Sequence
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    username= Column(String(50), unique=True)
    password = Column(String(250))
    name=Column(String(150))
    email=Column(String(150))