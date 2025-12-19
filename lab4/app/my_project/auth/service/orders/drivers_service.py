from lab4.app.my_project.auth.dao import drivers_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class DriversService(GeneralService):

    _dao = drivers_dao