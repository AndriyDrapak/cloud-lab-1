from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Schedules(db.Model, IDto):

    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    route = db.relationship("Routes", backref="schedules")
    departure_time = db.Column(db.Date, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.route_id}, {self.departure_time}, {self.arrival_time}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Schedules:
        obj = Schedules(**dto_dict)
        return obj
