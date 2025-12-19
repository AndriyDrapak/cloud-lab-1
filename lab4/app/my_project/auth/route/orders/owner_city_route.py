from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import owner_city_controller
from lab4.app.my_project.auth.domain import OwnerCity

owner_city_bp = Blueprint('owner_city', __name__, url_prefix='/owner-city')


@owner_city_bp.get('')
def get_all_owner_city() -> Response:
    return make_response(jsonify(owner_city_controller.find_all()), HTTPStatus.OK)


@owner_city_bp.post('')
def create_owner_city() -> Response:
    content = request.get_json()
    owner_city = OwnerCity.create_from_dto(content)
    owner_city_controller.create(owner_city)
    return make_response(jsonify(owner_city.put_into_dto()), HTTPStatus.CREATED)


@owner_city_bp.get('/<int:owner_city_id>')
def get_drivers(owner_city_id: int) -> Response:
    return make_response(jsonify(owner_city_controller.find_by_id(owner_city_id)), HTTPStatus.OK)


@owner_city_bp.put('/<int:owner_city_id>')
def update_owner_city(owner_city_id: int) -> Response:
    content = request.get_json()
    owner_city = OwnerCity.create_from_dto(content)
    owner_city_controller.update(owner_city_id, owner_city)
    return make_response("owner_city updated", HTTPStatus.OK)


@owner_city_bp.patch('/<int:owner_city_id>')
def patch_owner_city(owner_city_id: int) -> Response:
    content = request.get_json()
    owner_city_controller.patch(owner_city_id, content)
    return make_response("owner_city updated", HTTPStatus.OK)


@owner_city_bp.delete('/<int:owner_city_id>')
def delete_owner_city(owner_city_id: int) -> Response:
    owner_city_controller.delete(owner_city_id)
    return make_response("owner_city deleted", HTTPStatus.OK)
