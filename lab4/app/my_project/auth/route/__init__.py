from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.bus_maintenance_route import bus_maintenance_bp
    from .orders.bus_routes_route import bus_routes_bp
    from .orders.buses_route import buses_bp
    from .orders.driver_assignments_route import driver_assignments_bp
    from .orders.drivers_route import drivers_bp
    from .orders.owners_route import owners_bp
    from .orders.routes_route import routes_bp
    from .orders.schedules_route import schedules_bp
    from .orders.stops_route import stops_bp
    from .orders.tickets_route import tickets_bp
    from .orders.owner_city_route import owner_city_bp

    app.register_blueprint(bus_maintenance_bp)
    app.register_blueprint(bus_routes_bp)
    app.register_blueprint(buses_bp)
    app.register_blueprint(driver_assignments_bp)
    app.register_blueprint(drivers_bp)
    app.register_blueprint(owners_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(schedules_bp)
    app.register_blueprint(stops_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(owner_city_bp)
    
