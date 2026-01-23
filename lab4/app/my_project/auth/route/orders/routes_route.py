from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import routes_controller
from lab4.app.my_project.auth.domain import Routes

routes_bp = Blueprint('routes', __name__, url_prefix='/routes')


@routes_bp.get('')
def get_all_routes() -> Response:
    """
    GET /routes
    ---
    tags:
      - Routes
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(routes_controller.find_all()), HTTPStatus.OK)


@routes_bp.post('')
def create_routes() -> Response:
    """
    POST /routes
    ---
    tags:
      - Routes
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
    routes = Routes.create_from_dto(content)
    routes_controller.create(routes)
    return make_response(jsonify(routes.put_into_dto()), HTTPStatus.CREATED)


@routes_bp.get('/<int:routes_id>')
def get_routes(routes_id: int) -> Response:
    """
    GET /routes/<int:routes_id>
    ---
    tags:
      - Routes
    parameters:
      - name: routes_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    return make_response(jsonify(routes_controller.find_by_id(routes_id)), HTTPStatus.OK)


@routes_bp.put('/<int:routes_id>')
def update_routes(routes_id: int) -> Response:
    """
    PUT /routes/<int:routes_id>
    ---
    tags:
      - Routes
    parameters:
      - name: routes_id
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
    routes = Routes.create_from_dto(content)
    routes_controller.update(routes_id, routes)
    return make_response("routes updated", HTTPStatus.OK)


@routes_bp.patch('/<int:routes_id>')
def patch_routes(routes_id: int) -> Response:
    """
    PATCH /routes/<int:routes_id>
    ---
    tags:
      - Routes
    parameters:
      - name: routes_id
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
    routes_controller.patch(routes_id, content)
    return make_response("routes updated", HTTPStatus.OK)


@routes_bp.delete('/<int:routes_id>')
def delete_routes(routes_id: int) -> Response:
    """
    DELETE /routes/<int:routes_id>
    ---
    tags:
      - Routes
    parameters:
      - name: routes_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: OK
    """
    routes_controller.delete(routes_id)
    return make_response("routes deleted", HTTPStatus.OK)
