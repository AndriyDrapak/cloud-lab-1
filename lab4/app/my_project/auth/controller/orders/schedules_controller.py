from typing import List

from lab4.app.my_project.auth.service import schedules_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class SchedulesController(GeneralController):

    _service = schedules_service

    def get_schedules_by_route(self, route_id) -> List[object]:
        return self._service.get_schedules_by_route(route_id)
