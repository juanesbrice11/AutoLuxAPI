from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=64), nullable=False)
    last_name = Column(String(length=64), nullable=False)
    email = Column(String(length=250), unique=True, nullable=False)
    password = Column(String(length=60), nullable=False)
    age = Column(Integer, index=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    Rrole = relationship("Role", back_populates="Rusers")
    Rcomment = relationship("Comment", back_populates="Ruser")









