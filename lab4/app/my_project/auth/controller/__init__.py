from .orders.bus_maintenance_controller import BusMaintenanceController
from .orders.bus_routes_contoller import BusRoutesController
from .orders.buses_controller import BusesController
from .orders.driver_assignments_controller import DriverAssignmentsController
from .orders.drivers_controller import DriversController
from .orders.owners_controller import OwnersController
from .orders.routes_controller import RoutesController
from .orders.schedules_controller import SchedulesController
from .orders.stops_controller import StopsController
from .orders.tickets_controller import TicketsController
from .orders.owner_city import OwnerCityController

bus_maintenance_controller = BusMaintenanceController()
bus_routes_controller = BusRoutesController()
buses_controller = BusesController()
driver_assignments_controller = DriverAssignmentsController()
drivers_controller = DriversController()
owners_controller = OwnersController()
routes_controller = RoutesController()
schedules_controller = SchedulesController()
stops_controller = StopsController()
tickets_controller = TicketsController()
owner_city_controller = OwnerCityController()
