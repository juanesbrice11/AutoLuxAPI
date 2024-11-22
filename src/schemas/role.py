from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Role(BaseModel):
    name: str = Field(min_length=2, title="Nombre del Pais", max_length=50, example="Admin")
    description: str = Field(min_length=2, title="Nombre del Pais", max_length=50, example="Admin")


    

