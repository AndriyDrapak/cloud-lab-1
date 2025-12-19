from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import driver_assignments_controller
from lab4.app.my_project.auth.domain import DriverAssignments

driver_assignments_bp = Blueprint('driver_assignments', __name__, url_prefix='/driver-assignments')


@driver_assignments_bp.get('')
def get_all_driver_assignments() -> Response:
    return make_response(jsonify(driver_assignments_controller.find_all()), HTTPStatus.OK)


@driver_assignments_bp.post('')
def create_driver_assignments() -> Response:
    content = request.get_json()
    driver_assignments = DriverAssignments.create_from_dto(content)
    driver_assignments_controller.create(driver_assignments)
    return make_response(jsonify(driver_assignments.put_into_dto()), HTTPStatus.CREATED)


@driver_assignments_bp.get('/<int:driver_assignments_id>')
def get_driver_assignments(driver_assignments_id: int) -> Response:
    return make_response(jsonify(driver_assignments_controller.find_by_id(driver_assignments_id)), HTTPStatus.OK)


@driver_assignments_bp.put('/<int:driver_assignments_id>')
def update_driver_assignments(driver_assignments_id: int) -> Response:
    content = request.get_json()
    driver_assignments = DriverAssignments.create_from_dto(content)
    driver_assignments_controller.update(driver_assignments_id, driver_assignments)
    return make_response("driver_assignments updated", HTTPStatus.OK)


@driver_assignments_bp.patch('/<int:driver_assignments_id>')
def patch_driver_assignments(driver_assignments_id: int) -> Response:
    content = request.get_json()
    driver_assignments_controller.patch(driver_assignments_id, content)
    return make_response("driver_assignments updated", HTTPStatus.OK)


@driver_assignments_bp.delete('/<int:driver_assignments_id>')
def delete_driver_assignments(driver_assignments_id: int) -> Response:
    driver_assignments_controller.delete(driver_assignments_id)
    return make_response("driver_assignments deleted", HTTPStatus.OK)


@driver_assignments_bp.get('/get-drivers-by-bus-route/<int:bus_route_id>')
def get_drivers_by_bus_route(bus_route_id: int) -> Response:
    return make_response(jsonify(driver_assignments_controller.get_drivers_by_bus_route(bus_route_id)), HTTPStatus.OK)


@driver_assignments_bp.get('/get-bus-routes-by-driver/<int:driver_id>')
def get_bus_routes_by_driver(driver_id: int) -> Response:
    return make_response(jsonify(driver_assignments_controller.get_bus_routes_by_driver(driver_id)), HTTPStatus.OK)