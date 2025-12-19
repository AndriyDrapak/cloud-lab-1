from typing import List

from lab4.app.my_project.auth.dao import tickets_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class TicketsService(GeneralService):

    _dao = tickets_dao

    def get_routes_by_stop(self, stop_id: int) -> List[object]:
        return self._dao.get_routes_by_stop(stop_id)

    def get_stops_by_route1(self, route_id: int) -> List[object]:
        return self._dao.get_stops_by_route1(route_id)
