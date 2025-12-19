from typing import List

from lab4.app.my_project.auth.dao import schedules_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class SchedulesService(GeneralService):

    _dao = schedules_dao

    def get_schedules_by_route(self, route_id: int) -> List[object]:
        return self._dao.get_schedules_by_route(route_id)
