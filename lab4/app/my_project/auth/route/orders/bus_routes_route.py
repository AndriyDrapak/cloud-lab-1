from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import bus_routes_controller
from lab4.app.my_project.auth.domain import BusRoutes

bus_routes_bp = Blueprint('bus_routes', __name__, url_prefix='/bus-routes')


@bus_routes_bp.get('')
def get_all_bus_routes() -> Response:
    return make_response(jsonify(bus_routes_controller.find_all()), HTTPStatus.OK)


@bus_routes_bp.post('')
def create_bus_routes() -> Response:
    content = request.get_json()
    bus_routes = BusRoutes.create_from_dto(content)
    bus_routes_controller.create(bus_routes)
    return make_response(jsonify(bus_routes.put_into_dto()), HTTPStatus.CREATED)


@bus_routes_bp.get('/<int:bus_routes_id>')
def get_bus_routes(bus_routes_id: int) -> Response:
    return make_response(jsonify(bus_routes_controller.find_by_id(bus_routes_id)), HTTPStatus.OK)


@bus_routes_bp.put('/<int:bus_routes_id>')
def update_bus_routes(bus_routes_id: int) -> Response:
    content = request.get_json()
    bus_routes = BusRoutes.create_from_dto(content)
    bus_routes_controller.update(bus_routes_id, bus_routes)
    return make_response("bus_routes updated", HTTPStatus.OK)


@bus_routes_bp.patch('/<int:bus_routes_id>')
def patch_bus_routes(bus_routes_id: int) -> Response:
    content = request.get_json()
    bus_routes_controller.patch(bus_routes_id, content)
    return make_response("bus_routes updated", HTTPStatus.OK)


@bus_routes_bp.delete('/<int:bus_routes_id>')
def delete_bus_routes(bus_routes_id: int) -> Response:
    bus_routes_controller.delete(bus_routes_id)
    return make_response("bus_routes deleted", HTTPStatus.OK)


@bus_routes_bp.get('/get-busses-by-route/<int:route_id>')
def get_busses_by_route(route_id: int) -> Response:
    return make_response(jsonify(bus_routes_controller.get_busses_by_route(route_id)), HTTPStatus.OK)


@bus_routes_bp.get('/get-routes-by-bus/<int:bus_id>')
def get_routes_by_bus(bus_id: int) -> Response:
    return make_response(jsonify(bus_routes_controller.get_routes_by_bus(bus_id)), HTTPStatus.OK)
