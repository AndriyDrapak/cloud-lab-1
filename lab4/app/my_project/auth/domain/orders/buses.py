from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Buses(db.Model, IDto):

    __tablename__ = "buses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    registration_number = db.Column(db.String(20), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    ownership_type = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable=False)
    owner = db.relationship("Owners", backref="buses")

    def __repr__(self) -> str:
        return f"Buses('{self.id}, {self.registration_number}, {self.manufacturer}, {self.model}, {self.capacity}, {self.mileage}, {self.age}, {self.ownership_type}, {self.owner_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "registration_number": self.registration_number,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "capacity": self.capacity,
            "mileage": self.mileage,
            "age": self.age,
            "ownership_type": self.ownership_type,
            "owner_id": self.owner_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Buses:
        obj = Buses(**dto_dict)
        return obj
