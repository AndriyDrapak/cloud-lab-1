from typing import List

from lab4.app.my_project.auth.service import bus_routes_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BusRoutesController(GeneralController):

    _service = bus_routes_service

    def get_busses_by_route(self, route_id) -> List[object]:
        return self._service.get_busses_by_route(route_id)

    def get_routes_by_bus(self, bus_id) -> List[object]:
        return self._service.get_routes_by_bus(bus_id)
