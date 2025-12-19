from typing import List

from lab4.app.my_project.auth.dao import bus_routes_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BusRoutesService(GeneralService):

    _dao = bus_routes_dao

    def get_busses_by_route(self, route_id: int) -> List[object]:
        return self._dao.get_busses_by_route(route_id)

    def get_routes_by_bus(self, bus_id: int) -> List[object]:
        return self._dao.get_routes_by_bus(bus_id)
