from typing import List

from lab4.app.my_project.auth.dao import driver_assignments_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class DriverAssignmentsService(GeneralService):

    _dao = driver_assignments_dao

    def get_bus_routes_by_driver(self, driver_id: int) -> List[object]:
        return self._dao.get_bus_routes_by_driver(driver_id)

    def get_drivers_by_bus_route(self, bus_route_id: int) -> List[object]:
        return self._dao.get_drivers_by_bus_route(bus_route_id)
