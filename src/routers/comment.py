from fastapi import APIRouter
from src.schemas.comment import Comment
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.comment import Comment as CommentModel
from fastapi.encoders import jsonable_encoder
from src.repositories.comment import CommentRepository
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
Comment_router = APIRouter()


@Comment_router.get('/',
    tags=['Comment'],
    response_model=List[Comment],
    description="Returns all Comment ")
def get_all_Comments() -> List[Comment]:
    db = SessionLocal()
    result = CommentRepository(db).get_all_Comments()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@Comment_router.get('/{id}',
    tags=['Comment'],
    response_model=Comment,
    description="Returns data of one specific Comment")
def get_Comment_by_id(id: int = Path(ge=0, le=5000),) -> Comment:
    db = SessionLocal()
    element = CommentRepository(db).get_Comment(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested Comment was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@Comment_router.post('/',
    tags=['Comment'],
    response_model=dict,
    description="Creates a new Comment")
def create_Comment(Comment: Comment,) -> dict:
    db = SessionLocal()
    new_Comment = CommentRepository(db).create_Comment(Comment)
    return JSONResponse(content={
        "message": "The Comment was successfully created",
        "data": jsonable_encoder(new_Comment)
    }, status_code=201)

@Comment_router.put('{id}', tags=['Comment'],
    response_model=dict,
    description="Update a new Comment")
def update_Comment(id:int = Path(ge=1), Comment: Comment = Body()) -> dict:
    db= SessionLocal()
    update_Comment = CommentRepository(db).update_Comment(id,Comment)
    return JSONResponse(
        content={        
        "message": "The Comment was successfully updated",        
        "data": jsonable_encoder(update_Comment)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@Comment_router.delete('/{id}',
    tags=['Comment'],
    response_model=dict,
    description="Removes specific Comment")
def remove_Comment(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CommentRepository(db).get_Comment(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested Comment was not found",
            "data": None
        }, status_code=404)
    CommentRepository(db).delete_Comment(id)
    return JSONResponse(content={
        "message": "The Comment was removed successfully",
        "data": None
    }, status_code=200)