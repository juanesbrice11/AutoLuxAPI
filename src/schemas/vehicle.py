from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Vehicle(BaseModel):
    name: str = Field(min_length=2, title="Nombre del vehiculo", max_length=50, example="Ferrari F40")
    marca_id: int = Field(title="Marca del vehiculo", example= 1 )
    modelo: int = Field(title="Modelo del vehiculo",example=2004)
    top_speed: int = Field(title="Velocidad maxima del vehiculo", example=2004)
    engine: str = Field(min_length=1, title="Motor del vehiculo", max_length=250, example="V8")
    hp: int = Field(title="Motor del vehiculo", example=500)
    image: str = Field(min_length=6, title="Imagen del vehiculo", max_length=250, example="ferrari.png")
    acceleration: int = Field(title="Imagen del vehiculo", example= 3)



