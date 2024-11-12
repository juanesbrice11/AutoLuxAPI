from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    year_of_establishment = Column(Integer, nullable=False)
    image = Column(String(length=250), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    Rcountry = relationship("Country", back_populates="Rbrands")
    Rvehicles = relationship("Vehicle", back_populates="Rbrand")


