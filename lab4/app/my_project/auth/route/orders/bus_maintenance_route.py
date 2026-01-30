from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import bus_maintenance_controller
from lab4.app.my_project.auth.domain import BusMaintenance

bus_maintenance_bp = Blueprint('bus_maintenance', __name__, url_prefix='/bus-maintenance')


@bus_maintenance_bp.get('')
def get_all_bus_maintenance() -> Response:
    """
    GET /bus-maintenance
    ---
    tags:
      - Bus Maintenance
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(bus_maintenance_controller.find_all()), HTTPStatus.OK)


@bus_maintenance_bp.post('')
def create_bus_maintenance() -> Response:
    """
    POST /bus-maintenance
    ---
    tags:
      - Bus Maintenance
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
    bus_maintenance = BusMaintenance.create_from_dto(content)
    bus_maintenance_controller.create(bus_maintenance)
    return make_response(jsonify(bus_maintenance.put_into_dto()), HTTPStatus.CREATED)


@bus_maintenance_bp.get('/<int:bus_maintenance_id>')
def get_bus_maintenance(bus_maintenance_id: int) -> Response:
    """
    GET /bus-maintenance/<int:bus_maintenance_id>
    ---
    tags:
      - Bus Maintenance
    parameters:
      - name: bus_maintenance_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(bus_maintenance_controller.find_by_id(bus_maintenance_id)), HTTPStatus.OK)


@bus_maintenance_bp.put('/<int:bus_maintenance_id>')
def update_bus_maintenance(bus_maintenance_id: int) -> Response:
    """
    PUT /bus-maintenance/<int:bus_maintenance_id>
    ---
    tags:
      - Bus Maintenance
    parameters:
      - name: bus_maintenance_id
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
    bus_maintenance = BusMaintenance.create_from_dto(content)
    bus_maintenance_controller.update(bus_maintenance_id, bus_maintenance)
    return make_response("bus_maintenance updated", HTTPStatus.OK)


@bus_maintenance_bp.patch('/<int:bus_maintenance_id>')
def patch_bus_maintenance(bus_maintenance_id: int) -> Response:
    """
    PATCH /bus-maintenance/<int:bus_maintenance_id>
    ---
    tags:
      - Bus Maintenance
    parameters:
      - name: bus_maintenance_id
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
    bus_maintenance_controller.patch(bus_maintenance_id, content)
    return make_response("bus_maintenance updated", HTTPStatus.OK)


#@bus_maintenance_bp.delete('/<int:bus_maintenance_id>')
# def delete_bus_maintenance(bus_maintenance_id: int) -> Response:
    """
    DELETE /bus-maintenance/<int:bus_maintenance_id>
    ---
    tags:
      - Bus Maintenance
    parameters:
      - name: bus_maintenance_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
  #  bus_maintenance_controller.delete(bus_maintenance_id)
  #  return make_response("bus_maintenance deleted", HTTPStatus.OK)


@bus_maintenance_bp.get('/get-bus-maintenances-by-bus/<int:bus_id>')
def get_bus_maintenances_by_bus(bus_id: int) -> Response:
    """
    GET /bus-maintenance/get-bus-maintenances-by-bus/<int:bus_id>
    ---
    tags:
      - Bus Maintenance
    parameters:
      - name: bus_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(bus_maintenance_controller.get_bus_maintenances_by_bus(bus_id)), HTTPStatus.OK)
