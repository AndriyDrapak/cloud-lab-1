from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import schedules_controller
from lab4.app.my_project.auth.domain import Schedules

schedules_bp = Blueprint('schedules', __name__, url_prefix='/schedules')


@schedules_bp.get('')
def get_all_schedules() -> Response:
    return make_response(jsonify(schedules_controller.find_all()), HTTPStatus.OK)


@schedules_bp.post('')
def create_schedules() -> Response:
    content = request.get_json()
    schedules = Schedules.create_from_dto(content)
    schedules_controller.create(schedules)
    return make_response(jsonify(schedules.put_into_dto()), HTTPStatus.CREATED)


@schedules_bp.get('/<int:schedules_id>')
def get_schedules(schedules_id: int) -> Response:
    return make_response(jsonify(schedules_controller.find_by_id(schedules_id)), HTTPStatus.OK)


@schedules_bp.put('/<int:schedules_id>')
def update_schedules(schedules_id: int) -> Response:
    content = request.get_json()
    schedules = Schedules.create_from_dto(content)
    schedules_controller.update(schedules_id, schedules)
    return make_response("schedules updated", HTTPStatus.OK)


@schedules_bp.patch('/<int:schedules_id>')
def patch_schedules(schedules_id: int) -> Response:
    content = request.get_json()
    schedules_controller.patch(schedules_id, content)
    return make_response("schedules updated", HTTPStatus.OK)


@schedules_bp.delete('/<int:schedules_id>')
def delete_schedules(schedules_id: int) -> Response:
    schedules_controller.delete(schedules_id)
    return make_response("schedules deleted", HTTPStatus.OK)


@schedules_bp.get('/get-schedules-by-route/<int:route_id>')
def get_schedules_by_route(route_id: int) -> Response:
    return make_response(jsonify(schedules_controller.get_schedules_by_route(route_id)), HTTPStatus.OK)
