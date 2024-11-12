from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Country(BaseModel):
    id: int = Field(title="Numero de identificacion del pais", example=1)
    name: str = Field(min_length=2, title="Nombre del Pais", max_length=50, example="Italia")

    

