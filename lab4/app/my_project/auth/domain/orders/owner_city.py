from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class OwnerCity(db.Model, IDto):

    __tablename__ = "owner_city"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Owners('{self.id}', '{self.name}', '{self.owner_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OwnerCity:
        obj = OwnerCity(**dto_dict)
        return obj
