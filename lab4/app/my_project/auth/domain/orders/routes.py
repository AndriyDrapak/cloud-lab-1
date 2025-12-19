from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Routes(db.Model, IDto):

    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    start_address = db.Column(db.String(100), nullable=False)
    end_address = db.Column(db.String(100), nullable=False)
    total_distance = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    
    def __repr__(self) -> str:
        return f"Routes('{self.id}, {self.start_address}, {self.end_address}, {self.total_distance}, {self.total_price}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "start_address": self.start_address,
            "end_address": self.end_address,
            "total_distance": self.total_distance,
            "total_price": self.total_price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Routes:
        obj = Routes(**dto_dict)
        return obj
