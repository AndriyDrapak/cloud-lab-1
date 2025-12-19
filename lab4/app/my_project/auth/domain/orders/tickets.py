from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Tickets(db.Model, IDto):

    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    route = db.relationship("Routes", backref="tickets")
    stop_from_id = db.Column(db.Integer, db.ForeignKey("stops.id"), nullable=False)
    stop_from = db.relationship("Stops", backref="tickets")
    price = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    
    def __repr__(self) -> str:
        return f"Stops('{self.id}, {self.route_id}, {self.stop_from_id}, {self.price}, {self.purchase_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "stop_from_id": self.stop_from_id,
            "price": self.price,
            "purchase_date": self.purchase_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Tickets:
        obj = Tickets(**dto_dict)
        return obj
