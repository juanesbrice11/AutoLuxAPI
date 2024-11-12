from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.role import Role
from src.models.role import Role as roles
from src.repositories.role import RoleRepository

role_router = APIRouter(tags=['Roles'])

#CRUD role

@role_router.get('/',response_model=List[Role],description="Devuelve todos los roles")
def get_roles()-> List[Role]:
    db= SessionLocal()
    result = RoleRepository(db).get_all_roles()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)