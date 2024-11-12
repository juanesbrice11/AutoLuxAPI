from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Comment(BaseModel):
    id: int = Field(title="Numero de identificacion del comentario", example=1)
    date: str = Field(min_length=2, title="Fecha de creacion del cometario", max_length=50, example="12-12-2024")
    user_id: str = Field(min_length=6, title="Numero de identificacion del usuario", max_length=20, example="123456789")
    content: str = Field(min_length=2, title="Contenido del comentario", max_length=50, example="Me encanta este vehiculo...")
    vehicle_id: int = Field(title="Numero de identificacion del vehiculo", example=1)
    likes: Optional[int] = Field(title="Numero de likes del comentario", default=0, example=122)
    dislikes: Optional[int] = Field(title="Numero de dislikes del comentario", default=0, example=122)
    

