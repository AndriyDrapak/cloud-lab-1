from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Stops


class StopsDAO(GeneralDAO):
    _domain_type = Stops

    def get_stops_by_route(self, route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_stops_by_route(:p1)"),
                                       {'p1': route_id}).mappings().all()
        return [dict(row) for row in result]
