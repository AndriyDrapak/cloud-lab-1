from lab4.app.my_project.auth.service import drivers_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class DriversController(GeneralController):

    _service = drivers_service
