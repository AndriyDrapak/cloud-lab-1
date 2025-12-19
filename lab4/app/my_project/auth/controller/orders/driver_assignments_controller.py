from typing import List

from lab4.app.my_project.auth.service import driver_assignments_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class DriverAssignmentsController(GeneralController):

    _service = driver_assignments_service

    def get_drivers_by_bus_route(self, bus_route_id) -> List[object]:
        return self._service.get_drivers_by_bus_route(bus_route_id)

    def get_bus_routes_by_driver(self, driver_id) -> List[object]:
        return self._service.get_bus_routes_by_driver(driver_id)
