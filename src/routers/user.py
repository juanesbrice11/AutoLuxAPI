from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.encoders import jsonable_encoder
from src.repositories.user import UserRepository
from src.config.database import SessionLocal
from src.schemas.user import UserCreate as UserCreateSchema
from src.auth.has_access import has_access, security
from src.auth import auth_handler

user_router = APIRouter()

@user_router.get('/',
    tags=['User'],
    response_model=List[UserCreateSchema],
    description="Returns all Users ")
def get_all_users() -> List[UserCreateSchema]:
    db = SessionLocal()
    result = UserRepository(db).get_users()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@user_router.get('/{id}',
    tags=['User'],
    response_model=UserCreateSchema,
    description="Returns data of one specific User")
def get_user_by_id(id: int) -> UserCreateSchema:
    db = SessionLocal()
    result = UserRepository(db).get_user_by_id(id)
    if not result:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@user_router.put('/',
    tags=['User'],
    response_model=UserCreateSchema,
    description="Update a new User")
def update_user(credentials: Annotated[HTTPAuthorizationCredentials,
    Depends(security)], user: UserCreateSchema = Body()) -> UserCreateSchema:
    db= SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token)
    if payload:
        user_id = payload.get("user_id")
        result = UserRepository(db).edit_user(user_id, user)
        return JSONResponse(
            content={        
            "message": "The User was successfully updated",        
            "data": jsonable_encoder(result)    
        }, status_code=200)

@user_router.delete('/',
    tags=['User'],
    response_model=UserCreateSchema,
    description="Delete a User")
def delete_user(credentials: Annotated[HTTPAuthorizationCredentials,
    Depends(security)]) -> UserCreateSchema:
    db= SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token)
    if payload:
        user_id = payload.get("user_id")
        result = UserRepository(db).delete_user(user_id)
        return JSONResponse(
            content={        
            "message": "The User was successfully deleted",        
            "data": jsonable_encoder(result)    
        }, status_code=200)