from .orders.bus_maintenance_service import BusMaintenanceService
from .orders.bus_routes_service import BusRoutesService
from .orders.buses_service import BusesService
from .orders.driver_assignments_service import DriverAssignmentsService
from .orders.drivers_service import DriversService
from .orders.owners_service import OwnersService
from .orders.routes_service import RoutesService
from .orders.schedules_service import SchedulesService
from .orders.stops_service import StopsService
from .orders.tickets_service import TicketsService
from .orders.owner_city_service import OwnerCityService

bus_maintenance_service = BusMaintenanceService()
bus_routes_service = BusRoutesService()
buses_service = BusesService()
driver_assignments_service = DriverAssignmentsService()
drivers_service = DriversService()
owners_service = OwnersService()
routes_service = RoutesService()
schedules_service = SchedulesService()
stops_service = StopsService()
tickets_service = TicketsService()
owner_city_dao = OwnerCityService()
