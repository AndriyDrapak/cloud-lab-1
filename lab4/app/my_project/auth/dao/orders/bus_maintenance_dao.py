from typing import List, Dict, Any

import sqlalchemy


from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import BusMaintenance


class BusMaintenanceDAO(GeneralDAO):
    _domain_type = BusMaintenance

    def get_bus_maintenances_by_bus(self, bus_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_bus_maintenances_by_bus(:p1)"),
                                       {'p1': bus_id}).mappings().all()
        return [dict(row) for row in result]
