from typing import List

from lab4.app.my_project.auth.service import tickets_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class TicketsController(GeneralController):

    _service = tickets_service

    def get_routes_by_stop(self, stop_id) -> List[object]:
        return self._service.get_routes_by_stop(stop_id)

    def get_stops_by_route1(self, route_id) -> List[object]:
        return self._service.get_stops_by_route1(route_id)
