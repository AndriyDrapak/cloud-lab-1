from lab4.app.my_project.auth.service import routes_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RoutesController(GeneralController):

    _service = routes_service
