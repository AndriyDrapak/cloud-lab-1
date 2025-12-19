from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import stops_controller
from lab4.app.my_project.auth.domain import Stops

stops_bp = Blueprint('stops', __name__, url_prefix='/stops')


@stops_bp.get('')
def get_all_stops() -> Response:
    return make_response(jsonify(stops_controller.find_all()), HTTPStatus.OK)


@stops_bp.post('')
def create_stops() -> Response:
    content = request.get_json()
    stops = Stops.create_from_dto(content)
    stops_controller.create(stops)
    return make_response(jsonify(stops.put_into_dto()), HTTPStatus.CREATED)


@stops_bp.get('/<int:stops_id>')
def get_stops(stops_id: int) -> Response:
    return make_response(jsonify(stops_controller.find_by_id(stops_id)), HTTPStatus.OK)


@stops_bp.put('/<int:stops_id>')
def update_stops(stops_id: int) -> Response:
    content = request.get_json()
    stops = Stops.create_from_dto(content)
    stops_controller.update(stops_id, stops)
    return make_response("stops updated", HTTPStatus.OK)


@stops_bp.patch('/<int:stops_id>')
def patch_stops(stops_id: int) -> Response:
    content = request.get_json()
    stops_controller.patch(stops_id, content)
    return make_response("stops updated", HTTPStatus.OK)


@stops_bp.delete('/<int:stops_id>')
def delete_stops(stops_id: int) -> Response:
    stops_controller.delete(stops_id)
    return make_response("stops deleted", HTTPStatus.OK)


@stops_bp.get('/get-stops-by-route/<int:route_id>')
def get_stops_by_route(route_id: int) -> Response:
    return make_response(jsonify(stops_controller.get_stops_by_route(route_id)), HTTPStatus.OK)
