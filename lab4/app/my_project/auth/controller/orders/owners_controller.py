from lab4.app.my_project.auth.service import owners_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class OwnersController(GeneralController):

    _service = owners_service
