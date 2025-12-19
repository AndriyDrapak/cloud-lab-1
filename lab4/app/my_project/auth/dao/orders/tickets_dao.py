from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Tickets


class TicketsDAO(GeneralDAO):
    _domain_type = Tickets

    def get_routes_by_stop(self, stop_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_routes_by_stop(:p1)"),
                                       {'p1': stop_id}).mappings().all()
        return [dict(row) for row in result]

    def get_stops_by_route1(self, route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_stops_by_route1(:p1)"),
                                       {'p1': route_id}).mappings().all()
        return [dict(row) for row in result]
