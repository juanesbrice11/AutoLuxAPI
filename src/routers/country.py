from fastapi import APIRouter
from src.schemas.country import Country
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from src.config.database import SessionLocal
from src.repositories.country import CountryRepository
from fastapi.encoders import jsonable_encoder

country_router = APIRouter()

@country_router.get('/',
    tags=['country'],
    response_model=List[Country],
    description="Returns all Country ")
def get_all_countries() -> List[Country]:
    db = SessionLocal()
    result = CountryRepository(db).get_all_countries()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@country_router.get('/{id}',
    tags=['country'],
    response_model=Country,
    description="Returns data of one specific country")
def get_country_by_id(id: int = Path(ge=0, le=5000),) -> Country:
    db = SessionLocal()
    element = CountryRepository(db).get_country(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested country was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element), status_code=200)

@country_router.post('/',
    tags=['country'],
    response_model=dict,
    description="Creates a new country")
def create_country(country: Country,) -> dict:
    db = SessionLocal()
    new_country = CountryRepository(db).create_country(country)
    return JSONResponse(content={
        "message": "The country was successfully created",
        "data": jsonable_encoder(new_country)
    }, status_code=201)

@country_router.put('/{id}', tags=['country'],
    response_model=dict,
    description="Update a country")
def update_country(id:int = Path(ge=1), country: Country = Body()) -> dict:
    db = SessionLocal()
    updated_country = CountryRepository(db).update_country(id, country)
    return JSONResponse(
        content={        
            "message": "The country was successfully updated",        
            "data": jsonable_encoder(updated_country)    
        }, 
        status_code=201
    )


@country_router.delete('/{id}',
    tags=['country'],
    response_model=dict,
    description="Removes a specific country")
def remove_country(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CountryRepository(db).get_country(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested country was not found",
            "data": None
        }, status_code=404)
    CountryRepository(db).delete_country(id)
    return JSONResponse(content={
        "message": "The country was removed successfully",
        "data": None
    }, status_code=200)
