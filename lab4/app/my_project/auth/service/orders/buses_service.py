from typing import List

from lab4.app.my_project.auth.dao import buses_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BusesService(GeneralService):

    _dao = buses_dao

    def get_buses_by_owner(self, owner_id: int) -> List[object]:
        return self._dao.get_buses_by_owner(owner_id)
