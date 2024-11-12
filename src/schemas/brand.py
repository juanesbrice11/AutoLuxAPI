from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Brand(BaseModel):
    id: int = Field(title="Numero de identificacion de la marca", example=1)
    name: str = Field(min_length=2, title="Nombre de la marca", max_length=50, example="Ferrari")
    country_id: int = Field(title="Pais de origen de la marca", max_length=50, example= 1)
    year_of_establishment: int = Field(title="Año de fundacion de la marca", example= 2004 )
    image: str = Field(min_length=6, title="Imagen de la marca", max_length=250, example="ferrari.png")
    
