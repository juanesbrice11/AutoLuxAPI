from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.config.database import Base

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(50), nullable=False)
    user_id = Column(String(64), ForeignKey("user.id"), nullable=False)
    content = Column(String(50), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=False)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)
    Ruser = relationship("User", back_populates="Rcomment")
    Rvehicle = relationship("Vehicle", back_populates="Rcomment")