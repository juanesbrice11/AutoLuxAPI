from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: str = Field(min_length=6, title="Numero de identificacion del usuario", max_length=20, example="123456789")
    name: str = Field(min_length=2, title="Nombre del usuario", max_length=50, example="Juan")
    last_name = Field(min_length=2, title="Apellido del usuario", max_length=50, example="Perez")
    email: EmailStr = Field(min_length=6, title="Email del usuario", max_length=250, example="juanperez@gmail.com")
    age: int = Field(title="Edad del usuario", example=18)
    password: str = Field(min_length=6,title="Contraseña del usuario", max_length=60, example="123456")

class UserLogin (BaseModel):
    email: EmailStr = Field(min_length=6, max_length=64, alias="email", title="Correo del usuario")
    password: str = Field(min_length=6, title="Contraseña del usuario")