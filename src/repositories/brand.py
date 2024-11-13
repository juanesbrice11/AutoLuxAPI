from typing import List
from fastapi import HTTPException
from src.schemas.brand import Brand
from src.models.brand import Brand as BrandModel

class BrandRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_Brands(self) -> List[Brand]:
        query = self.db.query(BrandModel)
        return query.all()

    def get_Brand(self, id: int ) -> Brand:
        element = self.db.query(BrandModel).filter(BrandModel.id == id).first()
        return element
    
    def create_Brand(self, brand: Brand) -> dict:
        new_Brand = BrandModel(**brand.model_dump())
        self.db.add(new_Brand)
        self.db.commit()
        self.db.refresh(new_Brand)
        return new_Brand
    
    def update_Brand(self, id:str, brand:Brand)-> dict:
        UpdateBrand: Brand= self.db.query(BrandModel).filter(BrandModel.id == id).first()  
        if UpdateBrand is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        UpdateBrand.name = brand.name

        self.db.commit()
        self.db.refresh(UpdateBrand)
        return UpdateBrand
    
    def delete_Brand(self, id: int) -> dict:
        element: Brand = self.db.query(BrandModel).filter(BrandModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element  