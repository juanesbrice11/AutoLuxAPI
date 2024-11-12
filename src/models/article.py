from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(length=100), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    title = Column(String(length=100), nullable=False)
    content = Column(String(length=100), nullable=False)
    update_date = Column(String(length=100), nullable=False)
    Rvehicle = relationship("Vehicle", back_populates="Rarticle")
    




