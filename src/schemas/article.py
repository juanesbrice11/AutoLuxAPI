from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Article(BaseModel):
    id: int = Field(title="Numero de identificacion del articulo", example=1)
    date: str = Field(min_length=2, title="Fecha de creacion del articulo", max_length=50, example="12-12-2024")
    vehicle_id: int = Field(title="Numero de identificacion del vehiculo", example=1)
    title: str = Field(min_length=2, title="Nombre del articulo", max_length=50, example="Ferrari F40")
    content: str = Field(min_length=2, title="Contenido del articulo", max_length=50, example="Este articulo...")
    update_date: str = Field(min_length=2, title="Fecha de actualizacion", max_length=50, example="12-12-2024")
    

