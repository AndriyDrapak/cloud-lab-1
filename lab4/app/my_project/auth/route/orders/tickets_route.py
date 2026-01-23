from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import tickets_controller
from lab4.app.my_project.auth.domain import Tickets

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')


@tickets_bp.get('')
def get_all_tickets() -> Response:
    """
    GET /tickets
    ---
    tags:
      - Tickets
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(tickets_controller.find_all()), HTTPStatus.OK)


@tickets_bp.post('')
def create_tickets() -> Response:
    """
    POST /tickets
    ---
    tags:
      - Tickets
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
    tickets = Tickets.create_from_dto(content)
    tickets_controller.create(tickets)
    return make_response(jsonify(tickets.put_into_dto()), HTTPStatus.CREATED)


@tickets_bp.get('/<int:tickets_id>')
def get_tickets(tickets_id: int) -> Response:
    """
    GET /tickets/<int:tickets_id>
    ---
    tags:
      - Tickets
    parameters:
      - name: tickets_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(tickets_controller.find_by_id(tickets_id)), HTTPStatus.OK)


@tickets_bp.put('/<int:tickets_id>')
def update_tickets(tickets_id: int) -> Response:
    """
    PUT /tickets/<int:tickets_id>
    ---
    tags:
      - Tickets
    parameters:
      - name: tickets_id
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
    tickets = Tickets.create_from_dto(content)
    tickets_controller.update(tickets_id, tickets)
    return make_response("tickets updated", HTTPStatus.OK)


@tickets_bp.patch('/<int:tickets_id>')
def patch_tickets(tickets_id: int) -> Response:
    """
    PATCH /tickets/<int:tickets_id>
    ---
    tags:
      - Tickets
    parameters:
      - name: tickets_id
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
    tickets_controller.patch(tickets_id, content)
    return make_response("tickets updated", HTTPStatus.OK)


@tickets_bp.delete('/<int:tickets_id>')
def delete_tickets(tickets_id: int) -> Response:
    """
    DELETE /tickets/<int:tickets_id>
    ---
    tags:
      - Tickets
    parameters:
      - name: tickets_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    tickets_controller.delete(tickets_id)
    return make_response("tickets deleted", HTTPStatus.OK)


@tickets_bp.get('/get-routes-by-stop/<int:stop_id>')
def get_routes_by_stop(stop_id: int) -> Response:
    """
    GET /tickets/get-routes-by-stop/<int:stop_id>
    ---
    tags:
      - Tickets
    parameters:
      - name: stop_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(tickets_controller.get_routes_by_stop(stop_id)), HTTPStatus.OK)


@tickets_bp.get('/get-stops-by-route/<int:route_id>')
def get_stops_by_route1(route_id: int) -> Response:
    """
    GET /tickets/get-stops-by-route/<int:route_id>
    ---
    tags:
      - Tickets
    parameters:
      - name: route_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(tickets_controller.get_stops_by_route1(route_id)), HTTPStatus.OK)
