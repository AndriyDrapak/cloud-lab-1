from lab4.app.my_project.auth.dao import routes_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RoutesService(GeneralService):

    _dao = routes_dao