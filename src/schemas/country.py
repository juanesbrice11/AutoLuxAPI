from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Country(BaseModel):
    name: str = Field(min_length=2, title="Nombre del Pais", max_length=50, example="Italia")


    

