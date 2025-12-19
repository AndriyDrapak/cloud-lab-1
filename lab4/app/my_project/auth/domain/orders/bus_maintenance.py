from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class BusMaintenance(db.Model, IDto):

    __tablename__ = "bus_maintenance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"), nullable=False)
    bus = db.relationship("Buses", backref="bus_maintenance")
    maintenance_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.bus_id}, {self.maintenance_date}, {self.description}, {self.cost}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "bus_id": self.bus_id,
            "maintenance_date": self.maintenance_date,
            "description": self.description,
            "cost": self.cost
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BusMaintenance:
        obj = BusMaintenance(**dto_dict)
        return obj
