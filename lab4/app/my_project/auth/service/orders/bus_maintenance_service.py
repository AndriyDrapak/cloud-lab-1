from typing import List

from lab4.app.my_project.auth.dao import bus_maintenance_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BusMaintenanceService(GeneralService):

    _dao = bus_maintenance_dao

    def get_bus_maintenances_by_bus(self, bus_id: int) -> List[object]:
        return self._dao.get_bus_maintenances_by_bus(bus_id)