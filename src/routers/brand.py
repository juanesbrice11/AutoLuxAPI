from fastapi import APIRouter
from src.schemas.brand import Brand
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.brand import Brand as BrandModel
from fastapi.encoders import jsonable_encoder
from src.repositories.brand import BrandRepository
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
Brand_router = APIRouter()


@Brand_router.get('/',
    tags=['Brand'],
    response_model=List[Brand],
    description="Returns all Brand ")
def get_all_Brands() -> List[Brand]:
    db = SessionLocal()
    result = BrandRepository(db).get_all_Brands()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@Brand_router.get('/{id}',
    tags=['Brand'],
    response_model=Brand,
    description="Returns data of one specific Brand")
def get_Brand_by_id(id: int = Path(ge=0, le=5000),) -> Brand:
    db = SessionLocal()
    element = BrandRepository(db).get_Brand(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested Brand was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@Brand_router.post('/',
    tags=['Brand'],
    response_model=dict,
    description="Creates a new Brand")
def create_Brand(Brand: Brand,) -> dict:
    db = SessionLocal()
    new_Brand = BrandRepository(db).create_Brand(Brand)
    return JSONResponse(content={
        "message": "The Brand was successfully created",
        "data": jsonable_encoder(new_Brand)
    }, status_code=201)

@Brand_router.put('{id}', tags=['Brand'],
    response_model=dict,
    description="Update a new Brand")
def update_Brand(id:int = Path(ge=1), Brand: Brand = Body()) -> dict:
    db= SessionLocal()
    update_Brand = BrandRepository(db).update_Brand(id,Brand)
    return JSONResponse(
        content={        
        "message": "The Brand was successfully updated",        
        "data": jsonable_encoder(update_Brand)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@Brand_router.delete('/{id}',
    tags=['Brand'],
    response_model=dict,
    description="Removes specific Brand")
def remove_Brand(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = BrandRepository(db).get_Brand(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested Brand was not found",
            "data": None
        }, status_code=404)
    BrandRepository(db).delete_Brand(id)
    return JSONResponse(content={
        "message": "The Brand was removed successfully",
        "data": None
    }, status_code=200)