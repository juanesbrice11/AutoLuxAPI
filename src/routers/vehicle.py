from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.config.database import SessionLocal
from fastapi.encoders import jsonable_encoder
from src.schemas.vehicle import Vehicle
from src.models.vehicle import Vehicle as Vehicles
from src.repositories.vehicle import VehicleRepository

vehicle_router = APIRouter(tags=['Vehicles'])

# CRUD vehicle

@vehicle_router.get('/', response_model=List[Vehicle], description="Devuelve todos los vehículos")
def get_vehicles() -> List[Vehicle]:
    db = SessionLocal()
    result = VehicleRepository(db).get_all_vehicles()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@vehicle_router.get('/{id}', response_model=Vehicle, description="Devuelve la información de un solo vehículo")
def get_vehicle(id: int = Path(ge=1)) -> Vehicle:
    db = SessionLocal()
    element = VehicleRepository(db).get_vehicle_by_id(id)
    if not element:
        return JSONResponse(
            content={
                "message": "The requested vehicle was not found",
                "data": None
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(
        content=jsonable_encoder(element),
        status_code=status.HTTP_200_OK
    )

@vehicle_router.post('/', response_model=dict, description="Crea un nuevo vehículo")
def create_vehicle(vehicle: Vehicle = Body()) -> dict:
    db = SessionLocal()
    new_vehicle = VehicleRepository(db).create_new_vehicle(vehicle)
    return JSONResponse(
        content={
            "message": "The vehicle was successfully created",
            "data": jsonable_encoder(new_vehicle)
        },
        status_code=status.HTTP_201_CREATED
    )

@vehicle_router.delete('/{id}', response_model=dict, description="Elimina un vehículo específico")
def remove_vehicle(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = VehicleRepository(db).delete_vehicle(id)
    if not element:
        return JSONResponse(
            content={
                "message": "The requested vehicle was not found",
                "data": None
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(
        content={
            "message": "The vehicle was successfully removed",
            "data": jsonable_encoder(element)
        },
        status_code=status.HTTP_200_OK
    )

@vehicle_router.put('/{id}', response_model=dict, description="Actualiza un vehículo específico")
def update_vehicle(id: int = Path(ge=1), vehicle: Vehicle = Body()) -> dict:
    db = SessionLocal()
    element = VehicleRepository(db).update_vehicle(id, vehicle)
    if not element:
        return JSONResponse(
            content={
                "message": "The requested vehicle was not found",
                "data": None
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(
        content={
            "message": "The vehicle was successfully updated",
            "data": jsonable_encoder(element)
        },
        status_code=status.HTTP_200_OK
    )
