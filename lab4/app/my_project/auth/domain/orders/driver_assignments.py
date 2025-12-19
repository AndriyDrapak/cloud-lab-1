from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class DriverAssignments(db.Model, IDto):

    __tablename__ = "driver_assignments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.id"), nullable=False)
    driver = db.relationship("Drivers", backref="driver_assignments")
    bus_route_id = db.Column(db.Integer, db.ForeignKey("bus_routes.id"), nullable=False)
    bus_route = db.relationship("BusRoutes", backref="driver_assignments")
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.driver_id}, {self.bus_route_id}, {self.start_date}, {self.end_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "driver_id": self.driver_id,
            "bus_route_id": self.bus_route_id,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DriverAssignments:
        obj = DriverAssignments(**dto_dict)
        return obj
