from typing import List

from lab4.app.my_project.auth.service import bus_maintenance_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BusMaintenanceController(GeneralController):

    _service = bus_maintenance_service

    def get_bus_maintenances_by_bus(self, bus_id) -> List[object]:
        return self._service.get_bus_maintenances_by_bus(bus_id)
