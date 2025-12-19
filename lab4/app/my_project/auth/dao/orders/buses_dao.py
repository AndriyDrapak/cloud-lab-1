from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Buses


class BusesDAO(GeneralDAO):
    _domain_type = Buses

    def get_buses_by_owner(self, owner_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_buses_by_owner(:p1)"),
                                       {'p1': owner_id}).mappings().all()
        return [dict(row) for row in result]
