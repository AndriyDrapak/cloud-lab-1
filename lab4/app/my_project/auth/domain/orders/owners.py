from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Owners(db.Model, IDto):

    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Owners('{self.id}', '{self.name}', '{self.contact}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "contact": self.contact,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owners:
        obj = Owners(**dto_dict)
        return obj
