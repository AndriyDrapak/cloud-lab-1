from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import owners_controller
from lab4.app.my_project.auth.domain import Owners

owners_bp = Blueprint('owners', __name__, url_prefix='/owners')


@owners_bp.get('')
def get_all_owners() -> Response:
    return make_response(jsonify(owners_controller.find_all()), HTTPStatus.OK)


@owners_bp.post('')
def create_owners() -> Response:
    content = request.get_json()
    owners = Owners.create_from_dto(content)
    owners_controller.create(owners)
    return make_response(jsonify(owners.put_into_dto()), HTTPStatus.CREATED)


@owners_bp.get('/<int:owners_id>')
def get_owners(owners_id: int) -> Response:
    return make_response(jsonify(owners_controller.find_by_id(owners_id)), HTTPStatus.OK)


@owners_bp.put('/<int:owners_id>')
def update_buses(owners_id: int) -> Response:
    content = request.get_json()
    buses = Owners.create_from_dto(content)
    owners_controller.update(owners_id, buses)
    return make_response("owners updated", HTTPStatus.OK)


@owners_bp.patch('/<int:owners_id>')
def patch_buses(owners_id: int) -> Response:
    content = request.get_json()
    owners_controller.patch(owners_id, content)
    return make_response("owners updated", HTTPStatus.OK)


@owners_bp.delete('/<int:owners_id>')
def delete_owners(owners_id: int) -> Response:
    owners_controller.delete(owners_id)
    return make_response("owners deleted", HTTPStatus.OK)
