from .orders.bus_maintenance_dao import BusMaintenanceDAO
from .orders.bus_routes_dao import BusRoutesDAO
from .orders.buses_dao import BusesDAO
from .orders.driver_assignments_dao import DriverAssignmentsDAO
from .orders.drivers_dao import DriversDAO
from .orders.owners_dao import OwnersDAO
from .orders.routes_dao import RoutesDAO
from .orders.schedules_dao import SchedulesDAO
from .orders.stops_dao import StopsDAO
from .orders.tickets_dao import TicketsDAO
from .orders.owner_city_dao import OwnerCityDAO

bus_maintenance_dao = BusMaintenanceDAO()
bus_routes_dao = BusRoutesDAO()
buses_dao = BusesDAO()
driver_assignments_dao = DriverAssignmentsDAO()
drivers_dao = DriversDAO()
owners_dao = OwnersDAO()
routes_dao = RoutesDAO()
schedules_dao = SchedulesDAO()
stops_dao = StopsDAO()
tickets_dao = TicketsDAO()
owner_city_dao = OwnerCityDAO()
