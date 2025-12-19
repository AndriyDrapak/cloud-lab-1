from lab4.app.my_project.auth.service import owner_city_dao
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class OwnerCityController(GeneralController):

    _service = owner_city_dao
