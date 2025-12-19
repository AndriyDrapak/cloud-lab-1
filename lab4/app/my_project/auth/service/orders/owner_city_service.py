from lab4.app.my_project.auth.dao import owner_city_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class OwnerCityService(GeneralService):

    _dao = owner_city_dao