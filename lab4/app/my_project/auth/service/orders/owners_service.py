from lab4.app.my_project.auth.dao import owners_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class OwnersService(GeneralService):

    _dao = owners_dao