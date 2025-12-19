from typing import List

from lab4.app.my_project.auth.service import buses_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BusesController(GeneralController):

    _service = buses_service

    def get_buses_by_owner(self, owner_id) -> List[object]:
        return self._service.get_buses_by_owner(owner_id)
