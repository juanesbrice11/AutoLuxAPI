from typing import List
from src.schemas.vehicle import Vehicle
from src.models.vehicle import Vehicle as Vehicles

class VehicleRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_vehicles(self) -> List[Vehicle]:
        query = self.db.query(Vehicles)
        return query.all()
    
    def get_vehicle_by_id(self, id: int):
        element = self.db.query(Vehicles).filter(Vehicles.id == id).first()
        return element
    
    def delete_vehicle(self, id: int) -> dict:
        element: Vehicle = self.db.query(Vehicles).filter(Vehicles.id == id).first()
        if element:
            self.db.delete(element)
            self.db.commit()
        return element

    def create_new_vehicle(self, vehicle: Vehicle) -> dict:
        new_vehicle = Vehicles(**vehicle.model_dump())
        self.db.add(new_vehicle)
        self.db.commit()
        self.db.refresh(new_vehicle)
        return new_vehicle
    
    def update_vehicle(self, id: int, vehicle: Vehicle) -> dict:
        element = self.db.query(Vehicles).filter(Vehicles.id == id).first()
        if element:
            element.name = vehicle.name
            element.description = vehicle.description
            self.db.commit()
            self.db.refresh(element)
        return element
