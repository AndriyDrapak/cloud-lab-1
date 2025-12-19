from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class BusRoutes(db.Model, IDto):

    __tablename__ = "bus_routes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"), nullable=False)
    bus = db.relationship("Buses", backref="bus_routes")
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    route = db.relationship("Routes", backref="bus_routes")
    assignment_date = db.Column(db.Date, nullable=False)
    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.bus_id}, {self.route_id}, {self.assignment_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "bus_id": self.bus_id,
            "route_id": self.route_id,
            "assignment_date": self.assignment_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BusRoutes:
        obj = BusRoutes(**dto_dict)
        return obj
