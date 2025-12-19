from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import DriverAssignments


class DriverAssignmentsDAO(GeneralDAO):
    _domain_type = DriverAssignments

    def get_drivers_by_bus_route(self, bus_route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_drivers_by_bus_route(:p1)"),
                                       {'p1': bus_route_id}).mappings().all()
        return [dict(row) for row in result]

    def get_bus_routes_by_driver(self, driver_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_bus_routes_by_driver(:p1)"),
                                       {'p1': driver_id}).mappings().all()
        return [dict(row) for row in result]
