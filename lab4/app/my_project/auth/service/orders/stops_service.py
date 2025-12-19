from typing import List

from lab4.app.my_project.auth.dao import stops_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class StopsService(GeneralService):

    _dao = stops_dao

    def get_stops_by_route(self, route_id: int) -> List[object]:
        return self._dao.get_stops_by_route(route_id)
