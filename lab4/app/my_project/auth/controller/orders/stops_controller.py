from typing import List

from lab4.app.my_project.auth.service import stops_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class StopsController(GeneralController):

    _service = stops_service

    def get_stops_by_route(self, route_id) -> List[object]:
        return self._service.get_stops_by_route(route_id)
