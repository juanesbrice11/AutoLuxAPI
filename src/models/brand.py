from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base

class Brand(Base):
    __tablename__ = "brand"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(length=64), unique=True, index=True)
    name = Column(String(length=50))
    password = Column(String(length=64))
    is_active = Column(Boolean)
    products = relationship("Product", back_populates="owner")