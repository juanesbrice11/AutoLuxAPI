from fastapi import APIRouter
from src.schemas.article import Article
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.article import Article as ArticleModel
from fastapi.encoders import jsonable_encoder
from src.repositories.article import ArticleRepository
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
Article_router = APIRouter()


@Article_router.get('/',
    tags=['Article'],
    response_model=List[Article],
    description="Returns all Article ")
def get_all_Articles() -> List[Article]:
    db = SessionLocal()
    result = ArticleRepository(db).get_all_Articles()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@Article_router.get('/{id}',
    tags=['Article'],
    response_model=Article,
    description="Returns data of one specific Article")
def get_Article_by_id(id: int = Path(ge=0, le=5000),) -> Article:
    db = SessionLocal()
    element = ArticleRepository(db).get_Article(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested Article was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@Article_router.post('/',
    tags=['Article'],
    response_model=dict,
    description="Creates a new Article")
def create_Article(Article: Article,) -> dict:
    db = SessionLocal()
    new_Article = ArticleRepository(db).create_Article(Article)
    return JSONResponse(content={
        "message": "The Article was successfully created",
        "data": jsonable_encoder(new_Article)
    }, status_code=201)

@Article_router.put('{id}', tags=['Article'],
    response_model=dict,
    description="Update a new Article")
def update_Article(id:int = Path(ge=1), Article: Article = Body()) -> dict:
    db= SessionLocal()
    update_Article = ArticleRepository(db).update_Article(id,Article)
    return JSONResponse(
        content={        
        "message": "The Article was successfully updated",        
        "data": jsonable_encoder(update_Article)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@Article_router.delete('/{id}',
    tags=['Article'],
    response_model=dict,
    description="Removes specific Article")
def remove_Article(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = ArticleRepository(db).get_Article(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested Article was not found",
            "data": None
        }, status_code=404)
    ArticleRepository(db).delete_Article(id)
    return JSONResponse(content={
        "message": "The Article was removed successfully",
        "data": None
    }, status_code=200)