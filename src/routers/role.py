from fastapi import APIRouter, Body, Depends, Path, Query, Security, status
from fastapi.responses import JSONResponse
from typing import List
from src.config.database import SessionLocal
from src.schemas.role import Role
from src.models.role import Role as RoleModel
from src.repositories.role import RoleRepository
from fastapi.encoders import jsonable_encoder

role_router = APIRouter()

@role_router.get('/',
    tags=['Role'],
    response_model=List[Role],
    description="Returns all Roles")
def get_all_roles() -> List[Role]:
    db = SessionLocal()
    result = RoleRepository(db).get_all_roles()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@role_router.get('/{id}',
    tags=['Role'],
    response_model=Role,
    description="Returns data of one specific role")
def get_role_by_id(id: int = Path(ge=0, le=5000)) -> Role:
    db = SessionLocal()
    element = RoleRepository(db).get_role(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested role was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element), status_code=200)

@role_router.post('/',
    tags=['Role'],
    response_model=dict,
    description="Creates a new role")
def create_role(role: Role) -> dict:
    db = SessionLocal()
    new_role = RoleRepository(db).create_role(role)
    return JSONResponse(content={
        "message": "The role was successfully created",
        "data": jsonable_encoder(new_role)
    }, status_code=201)

@role_router.put('/{id}',
    tags=['Role'],
    response_model=dict,
    description="Update an existing role")
def update_role(id: int = Path(ge=1), role: Role = Body()) -> dict:
    db = SessionLocal()
    updated_role = RoleRepository(db).update_role(id, role)
    return JSONResponse(
        content={        
            "message": "The role was successfully updated",        
            "data": jsonable_encoder(updated_role)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@role_router.delete('/{id}',
    tags=['Role'],
    response_model=dict,
    description="Removes a specific role")
def remove_role(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = RoleRepository(db).get_role(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested role was not found",
            "data": None
        }, status_code=404)
    RoleRepository(db).delete_role(id)
    return JSONResponse(content={
        "message": "The role was removed successfully",
        "data": None
    }, status_code=200)
