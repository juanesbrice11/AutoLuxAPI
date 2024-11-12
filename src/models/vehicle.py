from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    marca_id = Column(Integer, ForeignKey('brand.id'))
    modelo = Column(Integer, nullable=False)
    top_speed = Column(Integer, nullable=False)
    article_id = Column(Integer, ForeignKey('article.id'))
    engine = Column(String(length=100), nullable=False)
    hp = Column(Integer, nullable=False)
    image = Column(String(length=100), nullable=False)
    acceleration = Column(Integer, nullable=False)
    Rbrand = relationship("Brand", back_populates="Rvehicles")
    Rarticle = relationship("Article", back_populates="Rvehicles")
    Rcomment = relationship("Comment", back_populates="Rvehicle")
