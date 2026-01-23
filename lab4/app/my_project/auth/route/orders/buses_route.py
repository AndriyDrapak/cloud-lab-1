from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import buses_controller
from lab4.app.my_project.auth.domain import Buses

buses_bp = Blueprint('buses', __name__, url_prefix='/buses')


@buses_bp.get('')
def get_all_buses() -> Response:
    """
    GET /buses
    ---
    tags:
      - Buses
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(buses_controller.find_all()), HTTPStatus.OK)


@buses_bp.post('')
def create_buses() -> Response:
    """
    POST /buses
    ---
    tags:
      - Buses
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      201:
        description: OK
    """
    content = request.get_json()
    buses = Buses.create_from_dto(content)
    buses_controller.create(buses)
    return make_response(jsonify(buses.put_into_dto()), HTTPStatus.CREATED)


@buses_bp.get('/<int:buses_id>')
def get_buses(buses_id: int) -> Response:
    """
    GET /buses/<int:buses_id>
    ---
    tags:
      - Buses
    parameters:
      - name: buses_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(buses_controller.find_by_id(buses_id)), HTTPStatus.OK)


@buses_bp.put('/<int:buses_id>')
def update_buses(buses_id: int) -> Response:
    """
    PUT /buses/<int:buses_id>
    ---
    tags:
      - Buses
    parameters:
      - name: buses_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: OK
    """
    content = request.get_json()
    buses = Buses.create_from_dto(content)
    buses_controller.update(buses_id, buses)
    return make_response("buses updated", HTTPStatus.OK)


@buses_bp.patch('/<int:buses_id>')
def patch_buses(buses_id: int) -> Response:
    """
    PATCH /buses/<int:buses_id>
    ---
    tags:
      - Buses
    parameters:
      - name: buses_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: OK
    """
    content = request.get_json()
    buses_controller.patch(buses_id, content)
    return make_response("buses updated", HTTPStatus.OK)


@buses_bp.delete('/<int:buses_id>')
def delete_buses(buses_id: int) -> Response:
    """
    DELETE /buses/<int:buses_id>
    ---
    tags:
      - Buses
    parameters:
      - name: buses_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    buses_controller.delete(buses_id)
    return make_response("buses deleted", HTTPStatus.OK)


@buses_bp.get('/get-buses-by-owner/<int:owner_id>')
def get_buses_by_owner(owner_id: int) -> Response:
    """
    GET /buses/get-buses-by-owner/<int:owner_id>
    ---
    tags:
      - Buses
    parameters:
      - name: owner_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(buses_controller.get_buses_by_owner(owner_id)), HTTPStatus.OK)
