from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import drivers_controller
from lab4.app.my_project.auth.domain import Drivers

drivers_bp = Blueprint('drivers', __name__, url_prefix='/drivers')


@drivers_bp.get('')
def get_all_drivers() -> Response:
    return make_response(jsonify(drivers_controller.find_all()), HTTPStatus.OK)


@drivers_bp.post('')
def create_drivers() -> Response:
    content = request.get_json()
    drivers = Drivers.create_from_dto(content)
    drivers_controller.create(drivers)
    return make_response(jsonify(drivers.put_into_dto()), HTTPStatus.CREATED)


@drivers_bp.get('/<int:drivers_id>')
def get_drivers(drivers_id: int) -> Response:
    return make_response(jsonify(drivers_controller.find_by_id(drivers_id)), HTTPStatus.OK)


@drivers_bp.put('/<int:drivers_id>')
def update_drivers(drivers_id: int) -> Response:
    content = request.get_json()
    drivers = Drivers.create_from_dto(content)
    drivers_controller.update(drivers_id, drivers)
    return make_response("drivers updated", HTTPStatus.OK)


@drivers_bp.patch('/<int:drivers_id>')
def patch_drivers(drivers_id: int) -> Response:
    content = request.get_json()
    drivers_controller.patch(drivers_id, content)
    return make_response("drivers updated", HTTPStatus.OK)


@drivers_bp.delete('/<int:drivers_id>')
def delete_drivers(drivers_id: int) -> Response:
    drivers_controller.delete(drivers_id)
    return make_response("drivers deleted", HTTPStatus.OK)
