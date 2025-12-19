from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Drivers(db.Model, IDto):

    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    license_number = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.first_name}, {self.last_name}, {self.license_number}, {self.phone_number}, {self.hire_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "license_number": self.license_number,
            "phone_number": self.phone_number,
            "hire_date": self.hire_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Drivers:
        obj = Drivers(**dto_dict)
        return obj
