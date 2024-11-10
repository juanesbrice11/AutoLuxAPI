from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str = Field(min_length=2, title="Nombre del usuario", max_length=50, example="Juan Perez")
    id_number: str = Field(min_length=6, title="Numero de identificacion del usuario", max_length=20, example="123456789")
    email: EmailStr = Field(min_length=6, title="Email del usuario", max_length=250, example="juanperez@gmail.com")
    password: str = Field(min_length=6,title="Contraseña del usuario", max_length=60, example="123456")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
            "name": "Pepe Pimentón",
            "email": "pepe@base.net",
            "password": "xxx",
            }
        }

class UserCreate (BaseModel):
    name: str = Field(min_length=2, title="Nombre del usuario", max_length=50, example="Juan Perez")
    id_number: str = Field(min_length=6, title="Numero de identificacion del usuario", max_length=20, example="123456789")
    email: EmailStr = Field(min_length=6, title="Email del usuario", max_length=250, example="juanperez@gmail.com")
    password: str = Field(min_length=6,title="Contraseña del usuario", max_length=60, example="123456")

class UserLogin (BaseModel):
    email: EmailStr = Field(min_length=6, max_length=64, alias="email", title="Correo del usuario")
    password: str = Field(min_length=6, title="Contraseña del usuario")