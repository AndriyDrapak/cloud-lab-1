from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import BusRoutes


class BusRoutesDAO(GeneralDAO):
    _domain_type = BusRoutes

    def get_busses_by_route(self, route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_busses_by_route(:p1)"),
                                       {'p1': route_id}).mappings().all()
        return [dict(row) for row in result]

    def get_routes_by_bus(self, bus_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_routes_by_bus(:p1)"),
                                       {'p1': bus_id}).mappings().all()
        return [dict(row) for row in result]

