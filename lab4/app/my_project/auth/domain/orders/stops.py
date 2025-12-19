from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Stops(db.Model, IDto):

    __tablename__ = "stops"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    route = db.relationship("Routes", backref="stops")
    stop_order = db.Column(db.Integer, nullable=False)
    stop_name = db.Column(db.String(100), nullable=False)
    distance_to_next = db.Column(db.Integer, nullable=False)
    price_to_next = db.Column(db.Integer, nullable=False)

    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.route_id}, {self.stop_order}, {self.stop_name}, {self.distance_to_next}, {self.price_to_next}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "stop_order": self.stop_order,
            "stop_name": self.stop_name,
            "distance_to_next": self.distance_to_next,
            "price_to_next": self.price_to_next
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Stops:
        obj = Stops(**dto_dict)
        return obj
